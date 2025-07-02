#!/usr/bin/env python3

import psutil
import os
import logging
import argparse
from datetime import datetime


def get_args():
    parser = argparse.ArgumentParser(
        description='Monitorea el uso de recursos del sistema y guarda un log.')
    parser.add_argument('--destination', type=str, required=True,
                        help='Carpeta base donde se guardará el log (subcarpeta logs/)')
    return parser.parse_args()


DISK_THRESHOLD = 80
RAM_THRESHOLD = 80
CPU_THRESHOLD = 80


def setup_logging(log_dir):
    os.makedirs(log_dir, exist_ok=True)
    timestamp = datetime.now().strftime('%Y-%m-%d-%H-%M')
    log_file = f'system_metrics_{timestamp}.log'
    logging.basicConfig(
        filename=os.path.join(log_dir, log_file),
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )


def current_timestamp():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def check_disk_usage():
    partitions = psutil.disk_partitions()
    return {part.device: psutil.disk_usage(part.mountpoint).percent for part in partitions}


def check_memory_usage():
    memory = psutil.virtual_memory()
    swap = psutil.swap_memory()
    return {
        'ram_used': memory.percent,
        'ram_available_mb': memory.available / (1024 ** 2),
        'ram_total_mb': memory.total / (1024 ** 2),
        'swap_used': swap.percent
    }


def check_cpu_usage():
    return {
        'cpu_total': psutil.cpu_percent(interval=1),
        'per_core': psutil.cpu_percent(percpu=True, interval=1)
    }


def main():
    args = get_args()
    log_dir = os.path.join(args.destination, 'logs')
    setup_logging(log_dir)

    print(f'************** {current_timestamp()} ***************\n')

    disk_usage = check_disk_usage()
    for partition, usage in disk_usage.items():
        message = f"{'Alerta' if usage > DISK_THRESHOLD else 'Uso'}: Disco en {partition} - {usage}%"
        print(message)
        logging.warning(
            message) if usage > DISK_THRESHOLD else logging.info(message)

    memory_usage = check_memory_usage()
    for key in ['ram_used', 'swap_used']:
        value = memory_usage[key]
        threshold = RAM_THRESHOLD
        label = 'RAM' if 'ram' in key else 'Swap'
        message = f"{'Alerta' if value > threshold else 'Uso'}: {label} - {value}%"
        print(message)
        logging.warning(
            message) if value > threshold else logging.info(message)

    cpu_usage = check_cpu_usage()
    total_message = f"{'Alerta' if cpu_usage['cpu_total'] > CPU_THRESHOLD else 'Uso'}: CPU total - {cpu_usage['cpu_total']}%"
    print(total_message)
    logging.warning(
        total_message) if cpu_usage['cpu_total'] > CPU_THRESHOLD else logging.info(total_message)

    for i, load in enumerate(cpu_usage['per_core']):
        message = f"{'Alerta' if load > CPU_THRESHOLD else 'Carga'} en núcleo {i} - {load}%"
        print(message)
        logging.warning(
            message) if load > CPU_THRESHOLD else logging.info(message)

    logging.shutdown()


if __name__ == "__main__":
    main()

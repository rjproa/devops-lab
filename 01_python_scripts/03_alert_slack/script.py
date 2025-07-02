#!/usr/bin/env python3

import psutil
import requests
import logging
import os
import argparse
from dotenv import load_dotenv

load_dotenv()

# Configuración
SLACK_WEBHOOK_URL = os.getenv('SLACK_WEBHOOK_URL')
DISK_THRESHOLD = 70
CPU_THRESHOLD = 65
RAM_THRESHOLD = 65


def enviar_alerta_slack(mensaje):
    requests.post(SLACK_WEBHOOK_URL, json={"text": mensaje})


def verificar_uso_disco():
    for part in psutil.disk_partitions(all=False):
        if 'loop' in part.device or not part.mountpoint.startswith('/'):
            continue
        usage = psutil.disk_usage(part.mountpoint)
        porcentaje = usage.percent
        if porcentaje > DISK_THRESHOLD:
            mensaje = f"Alerta: Partición {part.device} supera {DISK_THRESHOLD}% de uso: {porcentaje}%"
            enviar_alerta_slack(mensaje)
            logging.warning(mensaje)
        else:
            logging.info(f"Disco OK - {part.device}: {porcentaje}%")


def verificar_cpu():
    cpu_percent = psutil.cpu_percent(interval=1)
    if cpu_percent > CPU_THRESHOLD:
        mensaje = f"Alerta: CPU supera {CPU_THRESHOLD}% de uso: {cpu_percent}%"
        enviar_alerta_slack(mensaje)
        logging.warning(mensaje)
    else:
        logging.info(f"CPU OK - Uso: {cpu_percent}%")


def verificar_ram():
    ram = psutil.virtual_memory()
    if ram.percent > RAM_THRESHOLD:
        mensaje = f"Alerta: RAM supera {RAM_THRESHOLD}% de uso: {ram.percent}%"
        enviar_alerta_slack(mensaje)
        logging.warning(mensaje)
    else:
        logging.info(f"RAM OK - Uso: {ram.percent}%")


def main():
    parser = argparse.ArgumentParser(
        description='Monitoreo del sistema con logging.')
    parser.add_argument('--destination', type=str, default='.',
                        help='Carpeta de destino del archivo de log')
    args = parser.parse_args()

    # Asegurarse de que la carpeta existe
    os.makedirs(args.destination, exist_ok=True)

    # Configurar logging con la ruta especificada
    logfile = os.path.join(args.destination, 'monitor_sistema.log')
    logging.basicConfig(
        filename=logfile,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    logging.info("Iniciando monitoreo del sistema")
    verificar_uso_disco()
    verificar_cpu()
    verificar_ram()


if __name__ == "__main__":
    main()

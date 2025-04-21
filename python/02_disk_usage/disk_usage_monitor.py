#!/usr/bin/env python3

import psutil
import os
import logging
from datetime import datetime

LOG_DIR = os.path.expanduser('~/devops_scripts_python/02_disk_usage/logs')
os.makedirs(LOG_DIR, exist_ok=True)

fecha_log = datetime.now().strftime('%Y-%m-%d-%H-%M')
log_file = f'system_metrics_{fecha_log}.log'

logging.basicConfig(
    filename=os.path.join(LOG_DIR, log_file),
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


UMBRAL_DISCO = 80
UMBRAL_RAM = 80
UMBRAL_CPU = 80

def get_fecha():
    fecha_actual = datetime.now()
    fecha_formateada = fecha_actual.strftime('%Y-%m-%d %H:%M:%S')
    return fecha_formateada



def verificar_uso_disco():
    particiones = psutil.disk_partitions()
    uso_disco = {}
    
    for part in particiones:
        uso = psutil.disk_usage(part.mountpoint)
        uso_disco[part.device] = uso.percent
        
    return uso_disco

def verificar_uso_memoria():
    memoria = psutil.virtual_memory()
    swap = psutil.swap_memory()
    
    return {
        'RAM_usada': memoria.percent,
        'RAM_libre': memoria.available / (1024 ** 2),
        'RAM_total': memoria.total / (1024 ** 2),   
        'swap_usado': swap.percent
    }

def verificar_uso_cpu():
    cpu_total = psutil.cpu_percent(interval=1)
    carga_nucleos = psutil.cpu_percent(percpu=True, interval=1)
    return {
        'cpu_total': cpu_total,
        'carga_nucleos': carga_nucleos
    }

def main():
    print(f'************** {get_fecha()} ***************\n')
    uso_disco = verificar_uso_disco()
    for particion, uso in uso_disco.items():
        if uso > UMBRAL_DISCO:
            mensaje = f" Alerta: Uso de disco en {particion} - {uso}%"
            print(mensaje)
            logging.warning(mensaje)
        else:
            mensaje = f" Uso de disco en {particion} - {uso}%"
            print(mensaje)
            logging.info(mensaje)

    uso_memoria = verificar_uso_memoria()
    if uso_memoria['RAM_usada'] > UMBRAL_RAM:
        mensaje = f" Alerta: Uso de RAM - {uso_memoria['RAM_usada']}%"
        print(mensaje)
        logging.warning(mensaje)
    else:
        mensaje = f" Uso de RAM - {uso_memoria['RAM_usada']}%"
        print(mensaje)
        logging.info(mensaje)

    if uso_memoria['swap_usado'] > UMBRAL_RAM:
        mensaje = f" Alerta: Uso de Swap - {uso_memoria['swap_usado']}%"
        print(mensaje)
        logging.warning(mensaje)
    else:
        mensaje = f" Uso de Swap - {uso_memoria['swap_usado']}%"
        print(mensaje)
        logging.info(mensaje)

    uso_cpu = verificar_uso_cpu()
    if uso_cpu['cpu_total'] > UMBRAL_CPU:
        mensaje = f" Alerta: Uso total de CPU - {uso_cpu['cpu_total']}%"
        print(mensaje)
        logging.warning(mensaje)
    else:
        mensaje = f" Uso total de CPU - {uso_cpu['cpu_total']}%"
        print(mensaje)
        logging.info(mensaje)

    for i, carga in enumerate(uso_cpu['carga_nucleos']):
        if carga > UMBRAL_CPU:
            mensaje = f" Alerta: Carga en núcleo {i} - {carga}%"
            print(mensaje)
            logging.warning(mensaje)
        else:
            mensaje = f" Carga en núcleo {i} - {carga}%"
            print(mensaje)
            logging.info(mensaje)

    logging.shutdown()

if __name__ == "__main__":
    main()


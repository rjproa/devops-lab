#!/usr/bin/env python3

import os
import shutil
import sys
import argparse
import logging
from datetime import datetime, timedelta

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def backups_logs(origin, base_destination, days):
    if not os.path.isdir(origin):
        logging.error(f'La carpeta de logs no existe: {origin}')
        sys.exit(1)

    date_now = datetime.now().strftime('%Y-%m-%d')
    destination = os.path.join(base_destination, f'backup_{date_now}')
    os.makedirs(destination, exist_ok=True)

    files = [f for f in os.listdir(origin) if f.endswith('.log')]
    if not files:
        logging.warning('No se encontraron archivos .log para respaldar.')
    else:
        for filew in files:
            origin_route = os.patah.join(origin, filew)
            destination_route = os.path.join(destination, filew)
            shutil.copy2(origin_route, destination_route)
            logging.info(f'Copiado: {filew} -> {destination_route}')

        logging.info(f'Backup completado en: {destination}')

    delete_logs(base_destination, days)


def delete_logs(base_destination, days):
    limit = datetime.now() - timedelta(days=days)
    for folder in os.listdir(base_destination):
        fl_path = os.path.join(base_destination, folder)
        if os.path.isdir(fl_path) and folder.startswith('backup_'):
            try:
                date_str = folder.replace('backup_', '')
                date = datetime.strptime(date_str, '%Y-%m-%d')
                if date < limit:
                    shutil.rmtree(fl_path)
                    logging.info(f'Backup antiguo eliminado: {fl_path}')
            except ValueError:
                continue


def main():
    parser = argparse.ArgumentParser(
        description='Script de respaldo de archivos .log')
    parser.add_argument(
        '--origin',
        type=str,
        required=True,
        help='Ruta de la carpeta de logs'
    )
    parser.add_argument(
        '--destination',
        type=str,
        required=True,
        help='Ruta base de la carpeta de backups'
    )
    parser.add_argument(
        '--retention',
        type=int,
        default=7,
        help='Días de retención de backups antiguos'
    )

    args = parser.parse_args()
    backups_logs(args.origin, args.destination, args.retention)


if __name__ == '__main__':
    main()

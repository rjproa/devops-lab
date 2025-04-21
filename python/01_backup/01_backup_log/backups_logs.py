#!/usr/bin/env python3

import os
import shutil
from datetime import datetime

base = os.path.expanduser('~/devops_scripts_python')
origen = os.path.join(base, 'logs')

if not os.path.isdir(origen):
    print(f'Error: la carpeta de logs no existe en: {origen}')
    sys.exit(1)

fecha_actual = datetime.now().strftime('%Y-%m-%d')
destino_base = os.path.join(base, 'backups_logs')
destino = os.path.join(destino_base, f'backup_{fecha_actual}')

os.makedirs(destino, exist_ok=True)

archivos = [f for f in os.listdir(origen) if f.endswith('.log')]
if not archivos:
    print('No se encontraron los archivos .log para respaldar.')
else:

    for archivo in archivos:
        ruta_origen = os.path.join(origen, archivo)
        ruta_destino = os.path.join(destino, archivo)
        shutil.copy2(ruta_origen, ruta_destino)
        print(f'Copiado: {archivo} -> {ruta_destino}')


    print(f'\n Backup completado en: {destino}')

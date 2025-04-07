# Script de Backup de Archivos .log

Este script en python copia todos los archigos '.log' de una carpeta origen a una carpeta de de backup
con nombre basado en la fecha actual.


## ¿Qué hace?

- Busca todos los archivos con extensión '.log' en '~/devops_scripts_python/logs'
- Crea una carpeta 'backups_logs/backup_<fecha>' si no existe
- Copia los archivos allí y muestra el progreso por terminal

## Estructura esperadafech

~/devops_scripts_python/
|
|--logs/
|  |-ejemplo1.log
|  |-ejemplo2.log
|
|
|--backups_logs/
|  |backup_2025-04-07/
|  |-ejemplo1.log
|  |-ejemplo2.log
|
|
|-01_backup-log/
  |-backups_logs.py


- La carpera 'logs/' hace referencia al contenedor de los archivos '.log' que deseas respaldar.

## ¿Cómo ejecutar?

1. Asegúrate de estar en su sesión de usuario (no como root).
2. Ejecutar el script desde la terminal: 
- cd ~/devops_scripts_python/01_backup_log
- python3 backups_logs.py

## Requisitos

- Python 3
- Sistema Linux
## Autor

- Vega Proa Richard 

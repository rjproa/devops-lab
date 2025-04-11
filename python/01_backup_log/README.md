# 🛡️ Script de Backup de Archivos `.log`

Este script en **Python 3** realiza una copia de seguridad de todos los archivos con extensión `.log` desde un directorio de origen hacia un directorio de respaldo, organizando los backups por fecha.

---

## ⚙️ ¿Qué hace?

- Busca todos los archivos `.log` en el directorio:  
  `~/devops_scripts_python/logs/`
- Crea un directorio de respaldo con la estructura:  
  `~/devops_scripts_python/backups_logs/backup_<AAAA-MM-DD>/`
- Copia los archivos al nuevo directorio de backup
- Muestra información del progreso directamente en la terminal

---

## 📁 Estructura Esperada del Proyecto

```bash

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

```

> La carpeta `logs/` contiene los archivos `.log` que se desean respaldar.  
> El script se encuentra en `01_backup_log/` y debe ejecutarse desde ahí.

---

## ¿Cómo ejecutar?

1. Asegúrate de estar en tu sesión de usuario (no usar `root`)
2. Abre la terminal y navega al directorio del script:
   ```bash
   cd ~/devops_scripts_python/01_backup_log
3. Ejecuta el script
   ```bash
   python3 backups_logs.py
---
   
## 📦 Requisitos

- Python 3
- Sistema Linux
- Permisos de lectura en el directorio logs/ y escritura en backups_logs/


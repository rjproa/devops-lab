# 🗄️ Script de Respaldo de Archivos `.log`

La función es automatizar el respaldo de archivos `.log` desde una carpeta origen hacia una carpeta destino organizada por fecha. También limpia automáticamente los respaldos antiguos según el número de días definido por el usuario.

---

## 🚀 Uso

### 📌 Requisitos

- Python 3.6+
- 🚧 **(Importante)** Permisos de lectura sobre la carpeta de origen
- 🚧 **(Importante)** Permisos de escritura en la carpeta destino 

---

### 📂 Estructura del comando

```bash
python3 script.py --origin /ruta/a/logs --destination /ruta/a/backups --retention dias
```

> Por defecto `--retention` tiene el valor de `7`.

### ✅ Ejemplo de uso

```bash
python3 script.py --origin /var/log --destination /home/usuario/backups --retention 5
```

- ✅ Flujo de procesos del script
  - 1️⃣ Inicio: El script se ejecuta desde la terminal con argumentos:

    - `--origin`: ruta de la carpeta donde están los .log

    - `--destination`: ruta base donde se guardarán los backups

    - `--retention`: cantidad de días para conservar backups antiguos
  
  - 2️⃣ Validación inicial
    - Verifica que la carpeta de origen exista.
    - Si no existe, muestra un error y termina.  

  - 3️⃣ Creación del respaldo

    - Obtiene la fecha actual (YYYY-MM-DD).

    - Crea una carpeta de backup con nombre: backup_YYYY-MM-DD dentro del destino.

    - Copia todos los archivos .log desde la carpeta de origen a esa nueva carpeta.
  
  - 4️⃣ Limpieza de backups antiguos

    - Calcula la fecha límite según el número de días indicado.

    - Recorre todas las carpetas en la ruta de destino.

    - Si alguna carpeta tiene nombre tipo backup_YYYY-MM-DD y es anterior al límite, la elimina.

  - 5️⃣ Fin

    - Termina el script dejando el respaldo actualizado y eliminando los antiguos.

### 📊 Ejemplo visual de resultado

```bash
/home/usuario/backups/
├── backup_2025-06-28/
│   ├── syslog.log
│   └── error.log
├── backup_2025-06-29/
│   └── access.log
```
> En este ejemplo visual se usa el valor de `/home/usuario/backups` como parámetro para el valor de `--destination`.


# 🖥️ Script de Monitoreo de Recursos del Sistema

Este script monitorea el uso de **disco**, **memoria RAM**, **swap** y **CPU** del sistema, generando un archivo `.log` con la información recolectada. Si alguno de los recursos supera un umbral predefinido, se registra como una alerta.

---

## 🚀 Uso

### 📌 Requisitos

* Python 3.6+
* 📦 Librería `psutil` instalada (`pip install psutil`)
* 🚧 **(Importante)** Permisos de escritura en la carpeta destino donde se guardarán los logs

---

### 📂 Estructura del comando

```bash
python3 script.py --destino /ruta/a/carpeta
```

> Los logs se almacenarán automáticamente en una subcarpeta `logs/` dentro de la ruta proporcionada.

### ✅ Ejemplo de uso

```bash
python3 script.py --destino /home/usuario/monitoreo
```

* ✅ Flujo de procesos del script

  * 1️⃣ Inicio: El script se ejecuta desde la terminal con el argumento:

    * `--destino`: ruta base donde se guardará el log (en una subcarpeta `logs/`)

  * 2️⃣ Configuración del log

    * Crea la carpeta `logs/` si no existe.

    * Genera un archivo log con nombre `system_metrics_YYYY-MM-DD-HH-MM.log`.

  * 3️⃣ Monitoreo del sistema

    * 📦 **Disco**: revisa el porcentaje de uso por partición.

    * 💾 **Memoria**: revisa RAM usada, libre, total y uso de swap.

    * 🧠 **CPU**: mide el uso total y por núcleo.

    * Se imprimen y registran mensajes de uso o alerta si superan el 80%.

  * 4️⃣ Fin

    * Finaliza el log y cierra correctamente el archivo.

---

### 📊 Ejemplo visual de resultado

```bash
/home/usuario/monitoreo/logs/
└── system_metrics_2025-06-30-14-25.log
```
Lectura del archivo guardado:
```lua
$ cat system_metrics_2025-06-30-14-25.log

2025-06-30 10:04:28,245 - INFO - Uso: Disco en /dev/mapper/rl-root - 56.5%
2025-06-30 10:04:28,245 - WARNING - Alerta: Disco en /dev/sda1 - 92.8%
2025-06-30 10:04:28,245 - WARNING - Alerta: Disco en /dev/sr0 - 100.0%
2025-06-30 10:04:28,246 - WARNING - Alerta: RAM - 80.8%
2025-06-30 10:04:28,247 - INFO - Uso: Swap - 1.4%
2025-06-30 10:04:30,254 - INFO - Uso: CPU total - 0.5%
2025-06-30 10:04:30,254 - INFO - Carga en núcleo 0 - 0.0%
2025-06-30 10:04:30,254 - INFO - Carga en núcleo 1 - 0.0%
```
> En este archivo log se almacena la información de recursos del sistema con marca de tiempo y alertas si es necesario.

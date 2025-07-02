# 📡 Script de Monitoreo del Sistema con Alertas en Slack

Este script monitorea el uso de **disco**, **CPU** y **memoria RAM**, generando un archivo `.log` con los resultados y enviando **alertas a un canal de Slack** si se superan ciertos umbrales críticos.

---

## 🚀 Uso

### 📌 Requisitos

* Python 3.6+
* Librerías:
  - `psutil`
  - `requests`
  - `python-dotenv`
* Webhook de Slack válido
* Permisos de escritura en la carpeta destino donde se guardarán los logs

> 📦 Instalar dependencias:
```bash
pip install psutil requests python-dotenv
````

---

### ⚙️ Configuración del archivo `.env`

Para enviar alertas a Slack, se requiere configurar un webhook en un archivo `.env` en la raíz del proyecto:

```env
SLACK_WEBHOOK_URL=https://hooks.slack.com/services/tu/webhook/url
```

---

### 📂 Estructura del comando

```bash
python3 script.py --destination /ruta/a/carpeta
```

> El archivo de log `monitor_sistema.log` se generará dentro de la ruta especificada.

---

### ✅ Ejemplo de uso

```bash
python3 monitoreo_alertas.py --destination /home/usuario/monitoring
```

* ✅ Flujo del script:

  * 1️⃣ Inicio:

    * El script se ejecuta con el argumento:

      * `--destination`: ruta base donde se guarda el log `monitor_sistema.log`.

  * 2️⃣ Configuración de log:

    * Crea la carpeta si no existe.
    * Genera el archivo log `monitor_sistema.log` en la ruta destino.

  * 3️⃣ Monitoreo y alertas:

    * 📦 **Disco**: analiza todas las particiones montadas y envía alerta si superan el **70%** de uso.
    * 🧠 **CPU**: evalúa el uso total del CPU, alerta si excede el **65%**.
    * 💾 **RAM**: mide el uso de memoria, alerta si supera el **65%**.
    * Si se excede algún umbral, se genera un log **WARNING** y se envía una alerta por Slack. Si no, se registra un **INFO**.

  * 4️⃣ Finalización:

    * Cierra el log con estado general del sistema.

---

### 📊 Ejemplo visual del resultado

```bash
/home/usuario/monitoring/
└── monitor_sistema.log
```

Contenido del log generado:

```log
2025-06-30 14:56:00,123 - INFO - Iniciando monitoreo del sistema
2025-06-30 14:56:00,456 - INFO - Disco OK - /dev/sda1: 45.2%
2025-06-30 14:56:01,231 - WARNING - Alerta: CPU supera 65% de uso: 82.5%
2025-06-30 14:56:01,874 - INFO - RAM OK - Uso: 48.1%
```

> Las alertas son enviadas al canal de Slack vinculado al webhook configurado en `.env`.

---

### ⚠️ Notas importantes

* 🔒 Asegúrate de **no subir tu archivo `.env`** al repositorio público.
* 🔧 Puedes modificar los umbrales en el script: `DISK_THRESHOLD`, `CPU_THRESHOLD`, `RAM_THRESHOLD`.
* 📁 El parámetro `--destination` es opcional. Por defecto, el archivo log se guardará en el directorio actual.


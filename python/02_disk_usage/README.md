# 📊 Monitor de Uso de Recursos del Sistema

Este script desarrollado en **Python 3** permite monitorear de forma sencilla y efectiva el uso de **CPU**, **RAM**, **Swap** y **espacio en disco** en un sistema Linux. Está diseñado para ejecutarse manualmente o integrarse a tareas automáticas como `cron`.

Todos los resultados se registran en archivos `.log`, organizados por fecha, y almacenados en una carpeta dedicada.

---

## 🚀 ¿Qué hace?

El script realiza las siguientes tareas:

- Verifica el porcentaje de uso de disco en todas las particiones montadas
- Mide el uso actual de **RAM**, **memoria swap** y **CPU** total
- Evalúa la carga individual de cada núcleo del procesador
- Genera alertas si algún valor supera los umbrales establecidos (80% por defecto)
- Imprime y guarda en logs los resultados del escaneo

---

## ⚙️ Umbrales de Alerta

Por defecto, los siguientes umbrales activan alertas:

- 💾 Disco: > **80%**
- 🧠 RAM: > **80%**
- 🔁 Swap: > **80%**
- ⚙️ CPU (total y por núcleo): > **80%**

Estos valores pueden modificarse fácilmente editando las constantes `UMBRAL_DISCO`, `UMBRAL_RAM`, y `UMBRAL_CPU` en el script.

---

## 🗃️ Estructura Esperada


```bash
~/DevOps-Lab/python
|--01_backup
|
|--02_disk_usage
   |
   |--disk_usage_monitor.py
   |--logs
   |  |
   |  |--system_metrics_2025-04-17-21-42.log
   |
   |--README.md

```

> El directorio `logs/` se crea automaticamente si no existe y almacena los archivos `.log` generados.


---

## 🖥️  ¿Cómo ejecutar?

1. Abre la terminal y navega al directorio del script:

   ```bash
   cd ~/DevOps-Lab/python/02_disk_usage
   ```	

2. Ejecuta el sctipr con python 3:
   
   ```bash
   python3 disk_usage_monitor.py
   ```
   
---

## 🧪  Requisitos

1. Python 3
2. SIstema operativo Linux
3. Módulo psutil (instalar con: pip install psutil)







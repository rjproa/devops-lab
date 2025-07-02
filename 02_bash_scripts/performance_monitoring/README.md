# 📊 VMSTAT

Es una herramienta de la línea de comandos de Linux que reporta los siguientes datos del sistemas:
- 📈 Uso del CPU
- 🧠 Uso de memoria
- 🔄️ Actividad de swap
- 💾 Actividad de E/S
- ⌛ Procesos activas e inactivos

## USO

✍🏻 La sintáxis de `vmstat` es: `vmstat [OPCIONES] [RETRASO [CONTEO]]`
- RETRASO: intervalo en segundos entre muestras
- CONTEO: número de muestras

Ejemplo: 
- `$ vmstat 2 5` : muestra el reporte del comando 5 veces con intervalor de 2 segundos entre reporte y reporte. 

- ⚙️ OPCIONES: 
  - `-a` : muestra la memoria activa e inactiva del sistema.
  - `-f` : muestra el número de bifurcaciones desde el arranque.   
  - `-s` : muestra varias estadísticas de memoria y contradores de eventos de CPU y IO, desde el inicio de arranque de la máquina (sirve para un análisis general rápido).
  - `-d` : muestra estadísticas de lectura y escritura para varios discos.
  - `-t` : muestra el reporte de la máquina + una columna con la marca de tiempo del reporte.

## 📤 Salida del comando
![Resultado de ejecución del comando vmstat](https://inovanex.com/blog/wp-content/uploads/2017/12/vmstat.jpg)
> 📷 Imagen tomada de: [INOVANEX blog](https://inovanex.com/blog/vmstat-para-que-sirve/)

  - 🛠️ procs
    - `r` : número de procesos corriendo o esperando tiempo de CPU
    - `b` : muestra cuántos procesos están esperando a que termine una operación de hardware
  
  - 🧠 memory
    - `swpd` : cantidad de memoria virtual en uso
    - `free` : cantidad de memoria RAM libre
    - `buff` : memoria usada como buffer por el kernel
    - `cache` : memoria usada como caché de páginas
    - `inact` : cantidad de memoria que puede liberarse si es que hace falta
    - `active` : cantidad de memoria activa
  
  - 🔄️ swap
    - `si` : memoria traida del disco a la RAM
    - `so` : memoria movida de la RAM a la disco
  
  - 📀 io
    - `bi` : bloques de lectura de disco
    - `bo` : bloques de escritura en disco
  
  - 🧠 system
    - `in` : interrupciones por segundo
    - `cs` : cambios de contexto por segundo (stress -> htop -> find -> ...)

  - 💾 CPU
    - `us` : uso de la CPU en procesos de usuarios (programas, scripts)
    - `sy` : uso del CPU por el kernel, drivers, etc
    - `id` : tiempo en que el CPU no está haciendo nada
    - `wa` : tiempo en que el CPU espera a que el disco o red respondan
    - `st` : tiempo en que la VM quiere CPU pero el host no se lo da

---

## Referencia destacada

> 📘 *Linux commands: exploring virtual memory with vmstat*  
> ✍️ Escrito por **Tyler Carrigan** | 🗓️ Publicado el **10 de junio de 2020**  
> 🌐 Disponible en Red Hat: [redhat.com/blog/linux-commands-vmstat](https://www.redhat.com/en/blog/linux-commands-vmstat)  

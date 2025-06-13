# 🛠️ Monitoreo de Procesos en Linux (Nivel Avanzado)

## 🔍 Monitoreo de Procesos

### `ps aux | grep <proceso>`
Busca procesos activos por nombre. Muestra PID, uso de CPU y memoria, usuario, entre otros.

- `ps` → Muestra procesos activos.
- Opciones `aux`:
  - `a` → Todos los procesos de todos los usuarios.
  - `u` → Incluye el usuario que ejecuta el proceso.
  - `x` → Incluye procesos sin terminal asociada.
- `grep <nombre>` → Filtra los resultados por nombre.

📌 Ejemplo:
```bash
ps aux | grep jenkins
````

---

### `pidstat`

Monitorea el uso de recursos por PID.

* Requiere paquete `sysstat`.
* Mide uso de CPU, memoria, disco, entre otros.

📌 Ejemplo:

```bash
pidstat -p 1234          # Muestra estadísticas para PID 1234
pidstat 1 5 -p 1234      # Cada 1 segundo, 5 veces
```

Opciones útiles:

* `-r` → Memoria.
* `-d` → I/O de disco.
* `-u` → CPU (por defecto).
* `-h` → No mostrar encabezado.

---

## 📈 Monitoreo de CPU y Memoria

### `top`

Interfaz interactiva en tiempo real para monitorear el sistema.

* Muestra procesos ordenados por uso de CPU.
* Muestra uso de CPU, RAM, carga promedio, tiempo de actividad.

📌 Teclas útiles dentro de `top`:

* `P` → Ordenar por uso de CPU.
* `M` → Ordenar por uso de memoria.
* `k` → Matar un proceso.

📌 Alternativa mejorada: `htop`

---

### `nproc`

Muestra el número de núcleos de CPU disponibles.

📌 Ejemplo:

```bash
nproc
```

---

### `vmstat [intervalo] [repeticiones]`

Muestra estadísticas de procesos, memoria, swap, CPU e I/O.

📌 Ejemplo:

```bash
vmstat 2 5   # Muestra cada 2s, 5 veces
```

Campos comunes:

* `r` → procesos en espera.
* `b` → procesos bloqueados.
* `si/so` → swap in/swap out.
* `us`, `sy`, `id`, `wa` → uso de CPU.

---

### `sar`

Reporte detallado del sistema: CPU, RAM, disco, red (requiere `sysstat`).

📌 Ejemplo:

```bash
sar -u 1 5        # Uso de CPU cada 1s, 5 veces
sar -r 1 3        # Uso de RAM
sar -n DEV 1 3    # Estadísticas de red
```

✅ Ideal para monitoreo histórico o análisis post-mortem.

---

### `free [opciones]`

Muestra uso de memoria RAM y swap.

Opciones:

* `-b`, `-k`, `-m`, `-g` → Tamaños (bytes, KB, MB, GB).
* `-h` → Formato legible.
* `-t` → Total (RAM + swap).
* `-s N` → Actualiza cada N segundos.

📌 Ejemplo:

```bash
free -h -s 5
```

---

## 📦 Administración de Servicios y Tareas

### `systemctl`

Administra servicios en sistemas con `systemd`.

📌 Comandos comunes:

```bash
sudo systemctl start nginx
sudo systemctl stop nginx
sudo systemctl restart nginx
sudo systemctl enable nginx
sudo systemctl status nginx
```

📌 Consultas útiles:

```bash
systemctl list-units --type=service
systemctl list-units --state=running
systemctl list-units --state=failed
```

---

### `cron`

Sistema clásico para tareas programadas recurrentes.

📌 Sintaxis:

```
* * * * * /ruta/comando.sh
│ │ │ │ └── Día de la semana (0-6)
│ │ │ └──── Mes (1-12)
│ │ └────── Día del mes (1-31)
│ └──────── Hora (0-23)
└────────── Minuto (0-59)
```

📌 Editar tareas:

```bash
crontab -e
```

---

### `systemd timers`

Alternativa moderna a `cron`, integrada con `systemd`. Permite ejecutar unidades `.service` con más control.

📌 Archivos necesarios:

* `nombre.timer`
* `nombre.service`

📌 Ejemplo de `.timer`:

```ini
[Timer]
OnCalendar=*-*-* 06:00:00
Persistent=true

[Install]
WantedBy=timers.target
```

📌 Activación:

```bash
systemctl --user daemon-reload
systemctl --user enable --now nombre.timer
```

---

## 🧠 Herramientas de Sistema y Logs

### `journalctl`

Muestra los logs del sistema bajo `systemd`.

📌 Ejemplos:

```bash
journalctl -xe                # Últimos errores
journalctl -u nginx.service   # Logs de un servicio
journalctl --since today
```

---

## 🧰 Utilidades Complementarias

### `tail`

Muestra las últimas líneas de un archivo.

📌 Ejemplo:

```bash
tail -f /var/log/syslog    # Sigue en tiempo real
tail -n 50 archivo.log     # Últimas 50 líneas
```

---

### `head`

Muestra las primeras líneas de un archivo.

📌 Ejemplo:

```bash
head -n 10 archivo.log
```

---

### `less`

Paginador para visualizar archivos largos.

📌 Ejemplo:

```bash
less /var/log/syslog
```

Teclas útiles: `q` para salir, `/texto` para buscar.

---

## 🧾 Conclusión

* Usa `ps`, `pidstat` y `top/htop` para procesos.
* Usa `sar`, `vmstat` y `free` para análisis de rendimiento.
* Usa `systemctl`, `cron`, y `systemd timers` para tareas automáticas.
* Usa `journalctl` y comandos como `tail` y `less` para monitoreo de logs.

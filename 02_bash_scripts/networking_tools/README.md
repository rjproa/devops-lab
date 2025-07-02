# Comando SCP
## Copiar archivos

### Copiar directorio de un host local al servidor remoto

- `scp -r .\Desktop\carpeta_prueba\ rjproa@192.168 1.30:/home/rjproa/Escritorio`

  - `-r` : esta bandera se usa para copiar directorios.

### Copiar archivo de un host local al servidor remoto

- `scp -v .\Desktop\archivo_prueba.txt rjproa@192.168.1.30:/home/rjproa/Escritorio`

  - `-v` : esta bandera se usa para copiar archivos.

### Copiar archivos de un host remoto a otro

- `scp -v tecmint@192.168.0.183 :/home/ravi/ssh-cheatsheet.pdf tecmint@192.168.0.102 :/home/anusha/.
`

### Copiar archivos con fecha y hora de creación originales

- `scp -p scp-cheatsheet.pdf tecmint@192.168.0.183 :/inicio/tecmint/.`

### Compresión SCP al copiar archivos

- `scp -Cpv mensajes.log mraranto@202.xxx :.`

### Limitar el uso de ancho de banda con el comando SCP

- `$ scp -l 400 Etiqueta.pdf mraranto@202.xxx :.`
  - `-l 400` :  el valor después de `-l` indica el ancho de banda del proceso SCP a solo 50KB/seg. El ancho de banda se expresa en kilobits por segundo (kbps), 8 bits equivale 1 byte. SCP se contabiliza en kilobytes por segundo (KB/s) 

### Cambiar el puerto para SCP

- `scp -P 2249 Etiqueta.pdf mraranto@202.xxx :.`

### Deshabilitar mensajes de progreso

- `scp -q Etiqueta.pdf mraranto@202.xxx :.`
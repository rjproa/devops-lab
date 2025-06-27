## Tuberías y Redirecciones
### Tuberías
Establece una relación entre la salida de un comando con la entrada de otro. Permite usar la respuesta de salida de un comando como la entrada de otro comando y de esa manera combinar y automatizar ejecuciones.

Ejemplo: 
- `$ echo "Hello World" | tr [a-z] [A-Z]`
  - salida: `HELLO WORLD`, combina la salida del primer comando y luego a eso aplica el segundo comando `tr` que coloca en mayúsculas todas las palabras.

### Redirección
En sistemas unix puede usarse un archivo como entrada o puede ser la salida de un comando. Así mismo, se puede escribir la salida de un comando en un archivo.
Ejemplo:
- `$ curl -L https://GitHub.com/earthly/earthly/raw/main/README.md > README.md`
  - (>) : este comando lee el archivo README de la url y escribe el texto en nuestro archivo local README.

- `$ cat numbers.txt one two` -> aquí se crea un archivo numbers.txt con el contenido de 'one' y 'two'.
  - `echo "three" >> numbers.txt`
    - (>>) : este comando toma la salida de un comando y lo coloca al final del contenido del archivo. Si el archivo no existe, crea el archivo y guarda esa información.
    - Si solo se usa (>) reemplaza todo el contenido por el nuevo.

- `wc -1 < numbers.txt > lines.txt`
  - (<) : se usa para leer un archivo y luego actuar sobre él.
  - (wx -1) : cuenta las líneas en el archivo numbers.txt y guarda ese número en el archivo lines.txt.
      - Variantes:
        - `wc -w` : palabras
        - `wc -c` : bytes
        - `wc -m` : caracteres
  
- `$ kubectl apply -f namespace.yaml 2> error.txt`
  - (2>) : si por alguna razón al ejecutar un script o un comando se produce un error, este operador redirige el mensaje de salida hacia un archivo para su posterior análisis.
 

 ## Expresiones Regulares

 - Carácteres especiales 

    | Símbolo | Significado               | Ejemplo   | Qué hace                                     |
    | ------- | ------------------------- | --------- | -------------------------------------------- |
    | `{n}`   | Exactamente n veces       | `\d{3}`   | Tres dígitos                                 |
    | `.`     | Cualquier carácter        | `c.t`     | Coincide con `cat`, `cut`, `cot`, etc.       |
    | `()`    | Agrupación                | `(ab)+`   | Coincide con `ab`, `abab`, etc.              |
    | `^`     | Inicio de línea           | `^Hola`   | Coincide con líneas que comienzan con "Hola" |
    | `$`     | Fin de línea              | `mundo$`  | Coincide con líneas que terminan en "mundo"  |
    | `*`     | Cero o más veces          | `lo*`     | Coincide con `l`, `lo`, `loo`, etc.          |
    | `+`     | Una o más veces           | `lo+`     | Coincide con `lo`, `loo`, no con `l`         |
    | `?`     | Cero o una vez            | `colou?r` | Coincide con `color` o `colour`              |
    | `[]`    | Conjunto de caracteres    | `[aeiou]` | Coincide con una vocal                       |
    | `[^]`   | Negación                  | `[^0-9]`  | Cualquier carácter **no numérico**           |
    | \`      | \`                        | O lógico  | \`error                                      |
    | `\`     | Escapar carácter especial | `\.`      | Coincide con el punto literal `.`            |

- Ejemplos:
  - `grep -E "\b[0-9]{1,3}(\.[0-9]{1,3}){3}\b" archivo.txt` : Busca IPs como 192.168.0.1
  - `grep -oE "\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b" archivo.txt` : extrer correos electrónicos.
  - `find . -regex '.*[0-9]+.*'` : encuentra archivos que tengan números en su nombres.

## Comando de Procesamiento de Texto

- `cut` :  corta secciones de la fila de salida del resultado de alguna operación en terminal. Puede usarse para extraer una columna específica.
  - `cat demo.csv` :
    ```bash
    name,age,language,hobby
    john,21,golang,painting
    jane,22,python,singing
    jack,25,java,reading
    jill,23,python,cooking
    ```
  
  - `cut -d ',' -f 1 demo.csv` : 
    ```bash
    name
    john
    jane
    jack
    jill
    ```
  - `cut -d ',' -f 2-3 demo.csv` : muestra las columnas 2 y 3

- `sort` : organiza las lineas de un archivo de texto en un orden específico. Por defecto en orden ascendente.

  - `sort -r` : ordena de forma descendente.
  - `sort -f -o` : ignora mayúsculas (-f) y minúsculas (-o).

- `tac` : imprime el contenido de un archivo, similar al comando `cat`, pero con la diferencia que lo hace de manera invertida, del final hacia el inicio.

- `unique` : se utiliza para reportar u omitir líneas repetidas. El comando `unique` solo elimina solo las líneas repetidas adyacentes.
  - `sort names.txt | uniq -u` : este comando combina dos ejecuciones para eliminar líneas repetidas en todo el archivo, estén o no adyacentes.

  - `uniq -c` : (-c) esta bandera se usa para contar el número de ocurrencias de cada línea.

- `sed` : se utiliza para realizar diversas operaciones en secuencias de texto, cómo búsqueda y reemplazo.
  - `sed 's/k8s/kubernetes/g' blog.md` : `s` significa que queremos sustituir la palabra, `k8s` es la palabra que será sustituida, `kubernetes` es la palabra que se colocará en lugar de `k8s`, `g` significa que queremos que este comando se ejecute de manera general, si no se usa `g` el reemplazo solo ocurre en la primera coincidencia.

- `awk` : es un lenguaje de procesamiento de texto orientado a columnas.
  ```bash
  name,age,language,hobby
  john,21,golang,painting
  jane,22,python,singing
  jack,25,java,reading
  jill,23,python,cooking
  jake,12,rust,hiking  
  ```
  - `awk -F , '{print $2}' demo.csv` : 
      ```bash
      age
      21  
      22
      25
      23
      12
      ```
      - `-F` establece el delimitador de las filas que en este caso sería `,`. Con `{print $2}` imprime el segundo campo de la fila, en este caso sería la edad.
      - `awk -F , '{sum+=$2} END {print sum}' demo.csv` : suma las edades. `{sum+=$2}` examina el segundo valor del campo y lo suma a la variable suma. `END {print sum}` se ejecutará cuando se procesan todas las líneas e imprimirá el valor final de la variable `sum`.
      - `awk -F , 'NR>1 {print $2}' demo.csv` : (NR>1), `NR` se refiere al número de registros. `NR>1` no incluye el primer registro, que es el encabezado y no datos numéricos.

- `tr` : permite traducir o eliminar caracteres de la entrada y escribir el resultado en la salida. Sus usos más comunes son: convertir de mayúscula a minúscula, viceversa. Eliminar caracteres repetidos o simplemente akgún caracter.

  - `echo 'Hello World' | tr [A-Z] [a-z]` : convierte el texto a minúscula.

- `wc` : es un comando que permite contar el número de líneas, palabras y caracteres de un archivo. Por defecto el comando devuelve los 3 valores.
  - `wc markdown.md`
    - salida : `1 14 97 markdown.md`
  
  - Se puede usar banderas para obtener los valores individualmente:
    - `wc -w markdown.md` : contador de palabras
    - `wc -c markdown.md` : contador de caracteres
    - `wc -l markdown.md` : contador de líneas

- `tee` : permite redirigir la salida de un comando a otro, funciona bajo el mismo concepto que 'tuberías' pero permite conectar una salida como la entrada a uno o varios archivos.

- `xargs` : permite pasar la salida de un comando como parámetro para un segundo comando.
  - `ls | xargs rm` : el primer comando lista los archivos de la carpeta, `xargs` toma esa salida y actúa cobre cada fila aplicando el comando `rm`. 

### Comandos Modernos en la Terminal

- `rg` : es una alternativa moderna al comando `grep`, busca patrones en todos los archivos, archivos específicos y usar expresiones regulares para búsquedas avanzadas.

- `bat` : es una alternativa moderna al comando `cat`, admite resaltado de sintáxis y otras opciones de personalización. Su archivo de configuración es `~/.config/bat/config`.

- `fd` : es la versión moderna de `find`. 
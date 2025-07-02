# ⚡Automatización y productividad
## 🎥 Macros

Las macros permiten grabar una secuencia de acciones para repetirlas fácilmente.

Para grabar una macro: `q[a-z]`
 
 - `qa` : comienza a grabar en el registro `a`.
 - Realiza las acciones que deseas automatizar.
 - `q` : finaliza la grabación de la macro.
 - `@a` : ejecuta la macro.
 - `5@a` : ejecuta 5 veces la macro guardad en `a`.
 - `@@` : ejecuta la ultima macro usada.

Ejemplo:

Imagina que tienes una lista como:
```bash
juan
pedro
luis
mario
```

Y quieres que cada nombre quede así:
```bash
Nombre: juan
Nombre: pedro
Nombre: luis
Nombre: mario
```

Podrías grabar una macro así:
- Colócate en la primera línea.
- Escribe `qa` → Empieza a grabar en el registro a.
- Escribe `I` (para insertar al inicio de la línea), luego escribe Nombre: y presiona Esc.
- Escribe `j` (para bajar a la siguiente línea).
- Escribe `q` → Finaliza la grabación.

Ahora puedes ejecutar esa macro en las siguientes líneas con: `@a` y luego repetirla facilmente con: `@@`

<!-- 
> Es importante recordar que las macros grabadas solo viven dentro de la sesión de Vim. En caso se sale del archivo y se vuelve abrir se perderán las macros grabadas.

### Grabación de macros en el archivo `.vimrc`

Podemos inspeccionar los comandos guardados en nuestras macros, para consultar los comandos de una macro usamos: `:reg a`, esto inspecciona la macro guardada en `a`. Para ver todos los registros de nuestras macros usamos: `:reg`
-->

## 🔁 Repetir último comando (.)

En el modo normal de Vim se pueden realizar muchos cambios y ejecutar comandos. Por ejemplo, si queremos reemplazar una palabra, partimos del siguiente texto:

```bash
hola mundo
```
- Primero colocamos el cursor al inicio de la palabra `hola`.
- Luego ejecutamos el comando `cwtexto<Esc>`. 
  - `c` comienza un cambio. 
  - `w` indica que el cambio se aplicará hasta el final de la palabra.
  - `texto` es la nueva palabra que reemplazará a `hola`.
  - `<Esc>` es la tecla Escape, que se presiona para salir del modo de inserción y volver al modo normal.

Resultado:
```bash
texto mundo
```

Además, el comando `.` (punto) en modo normal repite la última acción realizada.
Por lo tanto, si colocamos el cursor al inicio de otra palabra y presionamos `.`, se repetirá el cambio anterior (`cwtexto`), facilitando ediciones rápidas.

## 🧠 Registros: manipular contenido

Tipos principales de registros:
- 📋 1. Registro no nombrado ("):
Es el registro por defecto. Cada vez que copias, cortas o pegas, Vim guarda el contenido aquí automáticamente.

- 🔡 2. Registros nombrados ("a - "z):
Puedes guardar contenido en registros específicos usando comillas + letra.
Ejemplo:

  - "ayy → copia la línea al registro a.

  - "ap → pega el contenido del registro a.

- 🔢 3. Registros numerados ("0 - "9):
Vim guarda un historial de eliminaciones.

  - "0 → lo último que copiaste con y.

  - "1 → lo último que cortaste (d o x), y así sucesivamente.

- ✍️ 4. Registro de comandos (:):
Usa q: para ver los comandos Ex recientes.

- 🔍 5. Registro de búsqueda (/):
Usa q/ o q? para ver búsquedas anteriores.

- 🖊️ 6. Registro de expresiones (=): Permite evaluar expresiones. Ejemplo:
  - En modo normal: :put =5+3 → pone 8 en el buffer.

> En otras palabras, los registros nos permiten tener múltiples portapapteles al alcance de comandos, esto es útil para oganizar el trabajo y mejorar la eficiencia.

## 📏 Comandos de rango (:2,5s/old/new/g) 

Es posible aplicar comandos a un rango de líneas específicas.

-   Sintaxis general:
    ```bash
    :[rango]s/viejo/nuevo/[opciones]
    ```
- Ejemplos:
  - `:2,5s/error/ok/g` → reemplaza "error" por "ok" en las líneas 2 a 5
  - `:%s/http/https/g` → reemplazo global en todo el archivo
  - `:10,$s/foo/bar/` → reemplaza de la línea 10 al final del archivo

-  Opciones útiles:
   - `g` → reemplaza todas las ocurrencias en la línea
   - `c` → confirma cada cambio
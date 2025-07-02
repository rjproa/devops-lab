# ⌨️ Comandos esenciales

## 🚶 Navegación

### Moverse por carácter, palabra, línea y bloque

- `h` → mover el cursor a la izquierda
- `l` → mover a la derecha
- `j` → bajar una línea
- `k` → subir una línea
- `w` → avanzar al inicio de la siguiente palabra
- `e` → ir al final de la palabra
- `b` → retroceder al inicio de la palabra
- `{ y }` → saltar entre párrafos
- `gg` → ir al inicio del archivo
- `G` → ir al final del archivo

### 🔍 Buscar (/, ?, n, N)

- `/texto` → busca hacia adelante la palabra texto

- `?texto` → busca hacia atrás

- `n` → siguiente coincidencia en la misma dirección

- `N` → coincidencia anterior (dirección opuesta)

- `:noh` → desactiva el resaltado de búsqueda

## ✏️ Edición:
### Insertar, borrar, reemplazar

- `i` → insertar antes del cursor

- `a` → insertar después del cursor

- `o` → nueva línea debajo

- `O` → nueva línea arriba

- `x` → borrar el carácter bajo el cursor

- `r<char>` → reemplaza el carácter bajo el cursor por <char>

- `R` → reemplazo continuo (modo overwrite)

### Copiar, cortar, pegar (y, d, p)

- `yy` → copiar la línea actual

- `dd` → cortar (borrar) la línea actual

- `p` → pegar debajo del cursor

- `P` → pegar encima del cursor

- `v`, `V` → seleccionar texto (modo visual) para luego usar `y` o `d`

### Deshacer (u), rehacer (Ctrl+r)

- `u` → deshacer el último cambio

- `Ctrl+r` → rehacer lo deshecho

### Reemplazos con regex (:s/.../.../)

Usa :s para hacer sustituciones:

- `:s/viejo/nuevo/` → reemplaza solo en la línea actual

- `:s/viejo/nuevo/g` → reemplaza todas las apariciones en la línea

- `:%s/viejo/nuevo/g` → reemplaza en todo el archivo

- `:%s/viejo/nuevo/gc` → reemplaza con confirmación en cada coincidencia

## 💾 Guardado y salida:
### :w, :q, :wq, :q!

- `:w` → guardar el archivo

- `:q` → salir (solo si no hay cambios)

- `:wq` o ZZ → guardar y salir

- `:q!` → salir sin guardar

- `:x` → guardar y salir (solo si hubo cambios)
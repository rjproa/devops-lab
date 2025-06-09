# 🗂️ Gestión de múltiples archivos

Trabajar con múltiples archivos en Vim es muy común en tareas de administración, ya sea editando varios scripts, archivos de configuración o logs. Vim tiene tres formas principales de hacerlo: `buffers`, `splits` y `tabs`.

## 📂 Abrir varios archivos (buffers)

Cuando abres varios archivos en Vim, cada uno se carga en un buffer. Un buffer es básicamente un archivo abierto en memoria.

- Para abrir varios archivos al iniciar Vim:

  ```bash
  vim archivo1.txt archivo2.txt archivo3.txt
  ```
- Para abrir un archivo adicional desde dentro de Vim:

  ```bash
  :e nombre_archivo
  ```

- Para ver todos los buffers abiertos:
  ```bash
  :ls
  ```


### 🔁 Cambiar entre buffers

Puedes moverte entre buffers abiertos fácilmente:

- `:bnext` o `:bn` → siguiente buffer

- `:bprev` o `:bp` → buffer anterior

- `:bNOMBRE` → ir directamente al buffer que coincida con ese nombre

- `:bd` → cerrar (borrar) el buffer actual

- `:ls` → lista de buffers con su número

- `:b#` → alternar entre el buffer actual y el anterior

## 🪟 Splits horizontales y verticales

Los splits permiten ver y editar múltiples archivos en la misma ventana dividiendo la pantalla.

- Split horizontal:
  ```bash
  :split archivo.txt
  ```
  o abre un nuevo archivo con:
  ```bash
  :sp archivo.txt
  ```

- Split vertical:
  ```bash
  :vsplit archivo.txt
  ```
  o

  ```bash
  :vsp archivo.txt
  ```

Para moverse entre splits:

- `Ctrl+w h` → izquierda

- `Ctrl+w l` → derecha

- `Ctrl+w j` → abajo

- `Ctrl+w k` → arriba

Para cerra un split:
```bash
:q
```

## 🧩 Uso de tabs

Vim también soporta pestañas (tabs), aunque funcionan diferente a los de navegadores: cada tab puede contener múltiples splits y buffers.

- Crear una nueva tab vacía:
  ```bash
  :tabnew
  ```

- Abrir un archivo en una nueva tab:
  ```bash
  :tabedit archivo.txt
  ```

- Navegar entre tabs:

  - `:tabnext` o `:tabn` → siguiente tab

  - `:tabprev` o `:tabp` → tab anterior

  - `gt` → siguiente tab (en modo normal)

  - `gT` → tab anterior

- Cerrar la tab actual:
  ```bash
  :tabclose
  ```
- Ver todas las tabs abiertas:
  ```bash
  :tabs
  ```
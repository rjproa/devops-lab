# 🧭 Modos de operación

🧠 Vim tiene 4 modos principales. Cambiar entre ellos es la clave para aprovechar su poder.



## 🅽 Modo Normal

- Usos: navegar, copiar, pegar, eliminar, ejecutar comandos
- Cómo entrar: presiona Esc desde cualquier otro modo

    |   Comando | Acción                   |
    | --------: | ------------------------ |
    |      `dd` | 🗑️ Eliminar línea       |
    |      `yy` | 📋 Copiar línea          |
    |       `p` | 📥 Pegar                 |
    |       `u` | ↩️ Deshacer              |
    | `h/j/k/l` | ⬅️➡️⬆️⬇️ Mover el cursor |


## 🅸 Modo Insert

- ✍️ Como un editor de texto tradicional.
- 🔹 Cómo entrar (desde modo Normal):
  | Tecla | Acción                      |
  | ----: | --------------------------- |
  |   `i` | Insertar antes del cursor   |
  |   `a` | Insertar después del cursor |
  |   `o` | Nueva línea debajo          |
  |   `O` | Nueva línea arriba          |

  🔙 Cómo salir: presiona Esc

## 🅥 Modo Visual

- Sirve para seleccionar texto y aplicar acciones como copiar, cortar o indentar.
- Cómo entrar:

  |      Tecla | Tipo de selección                 |
  | ---------: | --------------------------------- |
  |        `v` | Carácter por carácter             |
  |        `V` | Línea por línea                   |
  | `Ctrl + v` | 🧱 Selección en bloque (columnas) |

🛠️ Una vez seleccionado, puedes usar:

- ``y`` : copiar

- ``d`` : cortar

- ``>`` : indentar

- ``=`` : autoformatear


## 🅒 Modo Línea de comandos

- Para guardar, salir, buscar, configurar y más.
- Cómo entrar: presiona : desde el modo Normal

🛠️ Comandos útiles:

  |       Comando | Acción                      |
  | ------------: | --------------------------- |
  |          `:w` | 💾 Guardar                  |
  |          `:q` | 🚪 Salir                    |
  |         `:wq` | 💾 + 🚪 Guardar y salir     |
  | `:set number` | 🔢 Mostrar números de línea |
  |       `:help` | 📖 Ayuda integrada de Vim   |

# 🧠 Guía de Vim 

## ⚙️ ¿Qué es Vim?

Vim es un editor de texto ligero y eficiente, diseñado para usarse desde la terminal. Está disponible por defecto en la mayoría de sistemas Unix y Linux.
Vim permite editar archivos de configuración, scripts, logs, códigos y automatizaciones de forma rápida, sin depender de entornos gráficos.
Entre las funcionalidades que posee están:
- Múltiples nodos de edición.
- Navegación avanzada de texto.
- Grabación de macros.
- Soporte para expresiones regulares.
- Uso de plugins. 

---

## 📚 Índice de la Guía

### ⚙️ 1. [Instalación y configuración inicial](./01_instalacion_configuracion/)
- ✅ Verificar si Vim está instalado
- 💻 Instalación en Linux / MacOS / Windows
- 🛠️ Configuración básica en `~/.vimrc`:
  - 📌 Números de línea
  - 🎨 Resaltado de sintaxis
  - 🔧 Autoidentación
  - ↔️ Espacios vs tabs
  - 💡 Otras opciones útiles

### 🧭 2. [Modos de operación](./02_modos_operacion/)
- 🅽 Modo Normal
- 🅸 Modo Insert
- 🅥 Modo Visual
- 🅒 Modo Línea de comandos

### ⌨️ 3. [Comandos esenciales](./03_comandos_especiales/)
- 🚶 Navegación:
  - Moverse por carácter, palabra, línea y bloque
  - 🔍 Buscar (`/`, `?`, `n`, `N`)
- ✏️ Edición:
  - Insertar, borrar, reemplazar
  - Copiar, cortar, pegar (`y`, `d`, `p`)
  - Deshacer (`u`), rehacer (`Ctrl+r`)
  - Reemplazos con regex (`:s/.../.../`)
- 💾 Guardado y salida:
  - `:w`, `:q`, `:wq`, `:q!`

### 🗂️ 4. [Gestión de múltiples archivos](./04_gestion_archivos/)
- 📂 Abrir varios archivos (buffers)
- 🔁 Cambiar entre buffers
  - 🪟 Splits horizontales y verticales
- 🧩 Uso de tabs


### ⚡ 5. [Automatización y productividad](./06_automatizacion_productividad/)
- 🎥 Macros
- 🔁 Repetir último comando (`.`)
- 🧠 Registros: manipular contenido
- 📏 Comandos de rango (`:2,5s/old/new/g`)

### 🌐 6. [Vim en el flujo DevOps](./07_vim_devops/)
- 🧳 Editar vía SSH.
- 🐳 Usar Vim dentro de contenedores Docker
- 🔀 Integración con Git (commit, merge, rebase)
- 📈 Leer logs en caliente
- 🧪 Combinar Vim con `tmux` para multitarea

### 🔌 7. [Plugins recomendados (opcional)](./08_plugins/)
- 🧩 ¿Qué son los plugins y por qué usarlos?
- 📦 Gestores de plugins (`vim-plug`, `vundle`)
- 🧰 Plugins útiles para DevOps:
  - 🌲 Explorador de archivos (`NERDTree`)
  - 🤖 Autocompletado (`coc.nvim`, `YouCompleteMe`)
  - 📄 Sintaxis YAML/JSON mejorada
  - 🔧 Git integrado con `vim-fugitive`

### 🧨 8. [Comandos y errores comunes](./09_comandos_devops/)
- ✅ Top 10 comandos que debes dominar:
  - `:e archivo`, `:w`, `:q`, `:wq`, `i`, `Esc`, `:set number`, `/`, `yy`, `:!comando`
- ⚠️ Errores típicos y cómo evitarlos:
  - No saber salir (¡pasa!)
  - Confusión de modos
  - Indentación rota en YAML
  - No guardar cambios
  - Usar el mouse 😅

---

## 💬 ¿Te gusta la guía?

Si esta guía te ha ayudado, dale una ⭐, compártela o contribuye con ideas, mejoras o correcciones. Puedes abrir un `Issue` o hacer un `Pull Request` para colaborar. ¡Tu aporte es bienvenido! 🙌

---

> 📌 *Esta guía aún se encuentra en desarrollo*

---

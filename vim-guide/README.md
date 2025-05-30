# 🧠 Guía de Vim para DevOps

Esta guía está pensada para profesionales y estudiantes del área DevOps que quieren dominar Vim, un editor de texto potente, ligero y presente en casi todos los sistemas Unix/Linux. Aprender Vim te permitirá ser más rápido, autónomo y eficiente al trabajar con archivos de configuración, logs, scripts y tareas de automatización.

---

## 📌 Índice de Contenidos

### 1. Instalación y configuración inicial
- 1.1 Verificar si Vim está instalado
- 1.2 Instalación en sistemas Linux / MacOS / Windows.
- 1.3 Configuración básica inicial (`~/.vimrc`)
    - Activar números de línea
    - Resaltado de sintaxis
    - Autoidentación
    - Espacios vs tabs
    - Otras opciones útiles

### 2. Modos de operación
- 2.1 Modo Normal
- 2.2 Modo Insert
- 2.3 Modo Visual
- 2.4 Modo Línea de comandos

### 3. Comandos esenciales
- 3.1 Navegación
  - Movimiento por carácter, palabra, línea, bloque
  - Ir al inicio, final, número de línea
  - Buscar texto (`/`, `?`, `n`, `N`)

- 3.2 Edición
  - Insertar, eliminar, reemplazar
  - Copiar, cortar, pegar (`y`, `d`, `p`)
  - Deshacer y rehacer (`u`, `Ctrl+r`)
  - Reemplazo con expresiones regulares (`:s/.../.../`)

- 3.3 Guardado y salida
  - `:w`, `:q`, `:wq`, `:q!`

### 4. Gestión de archivos múltiples
- 4.1 Abrir varios archivos (buffers)
- 4.2 Cambiar entre buffers
- 4.3 Uso de ventanas (splits) horizontales y verticales
- 4.5 Uso de tabs

### 5. Edición de archivos de configuración
- 5.1 Archivos YAML (sangrías, recomendaciones)
- 5.2 Archivos JSON
- 5.3 Archivos `.conf` (nginx, apache, etc.)
- 5.4 Buenas prácticas para editar archivos sensibles

### 6. Automatización y productividad
- 6.1 Grabar y ejecutar macros (`q`, `@`)
- 6.2 Repetir comandos (`.`)
- 6.3 Uso de registros
- 6.4 Comandos de rango (`:2,5s/old/new/g`)

### 7. Vim en el flujo DevOps
- 7.1 Edición rápida vía SSH
- 7.2 Usar Vim dentro de contenedores Docker
- 7.3 Integración con Git (commit, merge, rebase)
- 7.4 Trabajar con logs del sistema
- 7.5 Vim en combinación con `tmux`

### 8. Plugins esenciales (opcional)
- 8.1 Introducción breve a los plugins
- 8.2 Gestores de plugins (`vim-plug`, `vundle`)
- 8.3 Plugins recomendados para DevOps
  - Explorador de archivos
  - Autocompletado básico
  - Sintaxis YAML/JSON
  - Integración con Git


### 9. Comandos de Vim para DevOps
- 10.1 Lista comentada de comandos esenciales para tareas frecuentes
- 10.2 Errores comunes y cómo evitarlos

---

> 🛠️ Esta guía está en desarrollo y se irá completando por secciones. Puedes contribuir o hacer sugerencias creando un Issue o Pull Request.


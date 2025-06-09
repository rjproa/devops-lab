# ⚙️Instalación y configuración de Vim
## ✅ Verificar si Vim está instalado

El editor `vim` viene preinstalado en la mayoría de distribuciones de Linux, así como también en macOS, por lo que no es necesario instalarlo manualmente, a diferencia de Windows.

Para verifcar si tenemos instalado `Vim` ingresamos a la terminal de nuestro sistema y ejecutamos el comando: `vim --version`

## 💻 Instalación por sistema operativo

En caso necesitemos instalar `Vim` en nuestro sistema lo hacemos con los siguientes comandos:
- Linux:
  - Debian, Ubuntu y derivados
    ```bash
    sudo apt update           # 🗂️ Actualiza lista de paquetes
    sudo apt install vim      # 🚀 Instala (o actualiza) Vim
    ``` 
  - RHEL, CentOS, Rocky, AlmaLinux:
    ```bash
    sudo dnf check-update     # 🔎 Verifica actualizaciones
    sudo dnf install vim      # 🚀 Instala Vim
    ``` 

- macOS:
  ```bash
  # usando Homebrew
  brew install vim
  ```

- Windows:
  - Ir a la página de vim: https://www.vim.org/download.php
  - Descargar el instalador para windows.
  - Ejecutar el instalador y seguir los pasos.
  

> En windows el archivo de personalización de vim se llama `_vimrc` y accedemos al mismo con el comando `vim $HOME\_vimrc`

## 🛠️ Configuración básica en `~/.vimrc`:

El archivo `~/.vimrc` es el archivo de configuración personal de vim que se encuentra en el directorio home del usuario. Aquí puedes definir cómo se comporta Vim cada vez que lo abres. Esto incluye apariencia, teclas personalizadas, opciones de edición, etc.

Para acceder al archivo `~/.vimrc` usamos el comando: `vim ~/.vimrc`

Personalización en el archivo `~/.vimrc`: 

### 1. 📌 Números de línea
Mostrar los números de linea, facilita moverse por el archivo.
```bash
set number
```
### 2. 🎨 Resaltado de sintaxis
Resalta el código de colores según el lenguaje que estés editando.
```bash
syntax on
```
### 3. 🔧 Autoidentación
`set autoindent` hace que cuando presiones `Enter`, la nueva línea copie la identación de la linea anterior.
`set smartindent` es una mejora del anterior, además de copiar la indentación anterior, Vim intenta adivinar si la nueva línea debe tener más sangría, basado en el lenguaje.
```bash
set autoindent
set smartindent
```
> 💡 Recomendado usar ambas juntas.

### 4. 💡 Otras opciones útiles
```bash
set mouse=a               # Habilita uso del mouse (si tu terminal lo permite)

set clipboard=unnamedplus # Permite copiar/pegar con el portapapeles del sistema

set showmatch             # Resalta paréntesis y llaves coincidentes

set incsearch             # Muestra los resultados mientras escribes una búsqueda

set ignorecase            # Búsqueda sin distinguir mayúsculas/minúsculas

set smartcase             # Pero si usas mayúsculas, distingue

set wildmenu              # Autocompletado de comandos en la línea de comandos

set cursorline            # Resalta la línea donde está el cursor

set wrap                  # Hace que las líneas largas se ajusten al ancho de pantalla
```


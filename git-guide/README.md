# Guía de Git y GitHub

## 01 Fundamentos

### 1.1 Conceptos básicos
Git es un sistema de control de versiones distribuido que permite gestionar cambios en proyectos de manera eficiente, rápida y segura. Cada usuario trabaja con una copia completa del repositorio, incluyendo historial y ramas, lo que permite el trabajo autónomo sin conexión a un servidor central.
 
Las principales ventajas de Git incluyen:

- Creación rápida de ramas
- Historial detallado de cambios
- Reversión segura de errores
- Resolución de conflictos en fusiones
- Cultura de commits frecuentes y colaboración fluida

Git puede integrarse con plataformas como **GitHub**, **GitLab** o **Bitbucket**, facilitando la colaboración en línea, documentación, automatización de tareas (CI/CD), control de versiones en la nube y mucho más.

### 1.2 Instalación y configuración

1. Visita: [https://git-scm.com/downloads](https://git-scm.com/downloads)
2. Según tu sistema operativo: 
- **Windows**: Descarga el instalador, executa el archivo .exe y sigue los pasos del asistente de instalación
- **Linux**: usa `# apt-get install git`.
- **MacOS**: instala [hombrew](https://brew.sh/) y luego ejecuta el comando `$ brew install git`

### 1.3 Configuración básica
```bash
git config --global user.name "Tu Nombre"
git config --global user.email tunombre@ejemplo.com
git config --list  # Verifica configuración
```
### 1.4 Configuración extra
```bash
# Elegir editor por defecto
git config --global core.editor "code --wait"      # Visual Studio Code
git config --global core.editor "nano"             # Nano (Linux)

# Activar colores en terminal
git config --global color.ui auto

# Alias útiles
git config --global alias.st status
git config --global alias.ci commit
git config --global alias.co checkout
git config --global alias.br branch
```
--- 
## 02 Repositorio
### 2.1 Iniciar un repositorio 
1. Iniciar el repositorio en local:
    ```bash 
    cd /ruta/proyecto # moverse a la carpeta del proyecto
    git init # iniciar git 
    git add . # agregar los cambios al staging
    git commit -m "first commit" # realizar el commit
    ```
 2. Crear el repositorio en GitHub:
    - Crear el repositorio y agregar un README si no tienes el archivo en local.
    - copiar la `url SSH` del repositorio
        ``` bash
        git remote add origin https://github.com/usuario/repo.git # conecta el repositorio local con el remoto
        git push -u origin main #envia los cambios al repositorio remoto
        ```

### 2.2 Conectar con GitHub vía SSH
Una clase `SSH` es un par de archivos que incluye clave pública y una privada. Sirven para autenticarte de forma segura sin necesidad de escribir usuario y contraseña cada vez.

La seguridad en GitHub es importante ya que controla quien puede hacer push, pull o leer código privado de tu repositorio, además de eso cada acción queda registrada con el usuario autenticado, lo que permite saber quién hizo el cambio.

Existe dos formas de autenticarse en GitHub:
- `HTTPS`: En cada acctión de push, pull, otros, por HTTPS GitHub te pedirá autenticarte con tu usuario de GitHub y un **token personal (PAT)**, este token puedes generarlo en setting > Developer settings > personal acces tokens. Crear un nuevo token. Luego cada vez que realices una acción de git push o git pull, deberás ingresar tu usuario y token.

- `SSH`: Una clave SSH es la forma recomendable para autenticarte en GitHub, sin usar usuario ni contraseña. En su lugar usas claves públicas y privadas.
    - `ls ~/.ssh`: verifica si ya tienes claves SSH. Deberías ver archivos como: `id_rsa.pub`, `id_ed25519.pub`. En caso no veas esto tendrás que crearlos.
    - `ssh-keygen -t ed25519 -C "tunombre@ejemplo.com"`
    - Agregar la clave al agente SSH: `eval "$(ssh-agent -s)" `,luego 
`ssh-add ~/.ssh/id_ed25519`.
    - Copia tu clave pública: `cat ~/.ssh/id_ed25519.pub`.
    - Ve a GitHub > Settings > SSH and GPG keys > New SSH Key y pega el contenido.
    - Listo. Ahora podrás realizar git push y git pull de manera correcta.
  

### 2.3 Clonar un repositorio
En ocasiones tendremos la necesidad de trabajar con proyectos que ya están en remoto en algún repositorio de GitHub, por tanto lo que tendremos que hacer es traer ese repositorio a nuestro entorno local de trabajo, para esto hacemos los siguiente:
   - Obtener la URL desde GitHub (HTTPS o SSH)
   - `cd ~/proyectos`: moverse a la carpeta que almacenará el repositorio clonado.
   - `git clone https://github.com/usuario/repo.git`: clonar el repositorio.
   - `cd repor`: entrar a la carpeta clonada `repor`.
   - Listo. Puedes trabajar en el proyecto y luego realizar un pull push o un pull request.

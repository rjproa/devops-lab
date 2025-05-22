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
## [Repositorios](./02_repositorios/README.md)

# 5. 🤝 Trabajo colaborativo
Colaborar con otras personas en GitHub implica que varias personas trabajen en el mismo proyecto, en diferentes ramas, sin conflictos, y aportando valor sin sobrescribir el trabajo de otros.

Git + GitHub ofrecen flujos de trabajo seguros y ordenados para esto. Veamos los más comunes:


## 5.1 🍴 Forks y Pull Requests
### 5.1.1 Fork
Fork es una copia completa de un repositorio público que se encuentra en tu cuenta de GitHub.

🔧¿Para qué sirve?
- Para proponer cambios en un proyecto del que no eres miembro.
- Para experimentar sin afectar el repositorio original.
- Modificar libremente un proyecto open source.

🔄 Flujo típico:

1. Ir a un repositorio público.
2. Darle click a ```fork```-> GitHub lo copia en tu cuenta como: ```github.com/tunombre/proyecto```.
3. Clonar ese fork en tu máquina local: ```git clone git@github.com:tunombre/proyecto.git```.
4. Hacer cambios, commits, pushes.. y cuando estás listo, hacer un ```pull requests```.

   ```bash
   # Cuando el repo original cambia, puede traer esos cambios a tu fork usando:

   # Agrega el repo original como remoto
    git remote add upstream https://github.com/original  autor.git

    # Trae los últimos cambios del original
    git fetch upstream

    # Fusiona los cambios en tu rama principal
    git merge upstream/main
   ```
### 5.1.2 Pull Requests
Un pull request es una solicitud para que los cambios que hiciste en tu fork (o rama) sean revisados y fusionados al repositorio original.

🧩 ¿Para qué sirve?
- Para colaborar en proyectos donde no tienes permisos directos.
- Para que otros revisen tus cambios antes de integrarlos.
- Para iniciar una discusión técnica sobre tu código.

🎯 ¿Cómo se crea?

1. Ya tienes tus cambios subidos en tu fork.
2. Vas a tu repositorio en GitHub → Botón “Pull Request”.
3. Eliges:
   - Base repo: el proyecto original
   - Compare: tu rama con los cambios
4. Agregas un título y descripción.
5. Envíalo para revisión.

🧠 Consejo: un buen pull request incluye:
- Qué se hizo
- Por qué se hizo
- Screenshots o ejemplos (si aplica)

## 5.2 🔄 Push & Pull  
### 5.2.1 ⬇️ Git Pull
Descarga los últimos cambios desde el repositorio remoto y los fusiona automáticamente con tu rama actual. Es como pedirle a Git: "Tráeme lo nuevo que hay en el servidor y mézclalo con mi trabajo."

Importante:
- Antes de cualquier ```push``` siempre debe hacerse un ```pull```.
- Sintáxis: ```git pull <remoto> <rama>```. Esto hace un ```git fetch origin``` y luego un ```git merge origin/main```.

🔁 ¿Cuál es la diferencia entre pull, fetch y merge?
- git fetch: solo descarga los cambios remotos, pero NO los fusiona.
- git merge: fusiona los cambios descargados.
-   git pull: hace ambos pasos: fetch + merge.

    >🧠 Entonces, si quieres más control, puedes hacer:
      ```git fetch origin```
      ```git merge origin/main```

### 5.2.2 ⬆️ Git Push (subir tus cambios al servidor remoto)

Envía los commits que tienes en tu repositorio local hacia un repositorio remoto. Es decir, "empujas" tu trabajo al servidor para que otros lo vean o para hacer respaldo.

📦 Flujo típico:
- Haces cambios → ```git add``` → ```git commit```
- Subes los commits al remoto con:
  ```bash
  git push origin nombre_rama
  ```

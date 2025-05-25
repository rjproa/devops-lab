# 6. 🛠️ Recomendaciones y extras

## 6.1 ✨ Alias útiles  
Un alias es como un sobrenombre que tú le das a un comando de Git. En lugar de escribir un comando largo como:
```bash
git log --oneline --graph --all --decorate
```
Puedes crear un alias llamada ```hist``` y luego solo ejecutarlo:
```bash
git hist
```

⚙️¿Cómo crear un alias?
1. Desde la línea de comandos:
   ```bash
   git config --global alias.nombre_alias 'comando_git'
   git config --global alias.st status
   ```
   Esto crear un alias ```git st``` que reemplaza al comando ```git status```.

2. Editando el archivo ```.gitconfig```:
   ```bash
   [alias]
   co = checkout
   br = branch
   ci = commit
   st = status
   hist = log --oneline --graph --decorate --all
   ```
   >🚧 Al usar '--global', el alias sirve para todos tus proyectos.</br>
   >🚧 Si lo haces sin '--global', será solo para la repo actual.

## 6.2 📂 Uso de `.gitignore`  
Es un archivo de texto que le dice a Git qué archivos o carpetas debe ignorar, es decir, que no debe incluir ni rastrear en el control de versiones. Esto es importante porque:
1. Evitar que archivos innecesarios o sensibles lleguen a GitHub.
2. Mantener el repositorio ligero y ordenado.
3. Prevenir problemas de seguridad y conflictos entre entornos.
>🟢 El archivo .gitignore debe estar en la raiz del repositorio.

La manera de escribir archivos y carpetas dentro de .gitignore es:
```bash
# Ignorar archivos específicos
secreto.txt

# Ignorar todas las imágenes PNG
*.png

# Ignorar carpetas
carpeta_oculta/

# Ignorar todo excepto un archivo
*.log
!important.log

# Ignorar archivos en cualquier subcarpeta
**/temp.txt
```

### 🛠️¿Qué hago si subí al repositorio un archivo sensible?
Si por algún error agregaste un archivo sensible al repositorio haciendo algo parecido a lo siguiente:
```bash
git add clave.txt
git commit -m "Agregué clave.txt"
```
Lo siguiente que intentarás hacer es agregar este archivo a  ```.gitignore```. El problema es que Git ya esta rastreando al archivo ```clave.txt``` porque ya fue añadido al repo.

Este problema se puede resolver con el siguiente comando:
```bash
# Esto le dice a Git que deje de seguir ese archivo, pero no lo borra de tu carpeta de trabajo en local.
git rm --cached clave.txt

#Luego se debe confirmar el cambio realizando un commit.
git commit -m "Elimine clave.txt del repositorio"
```
Esto ordena a Git que deje de seguir al archivo ```clave.txt``` y luego confirmas el cambio realizando un ```commit```. Además como al inicio ya agregaste el archivo ```clave.txt``` al archivo ```.gitignore```, luego de confirmar que Git deje de seguir el archivo, el archivo ```.gitignore``` ignorará al archivo ```clave.txt``` y no dejará que Git versione ese archivo.


## 6.3 ❗ Errores comunes y cómo solucionarlos  


### ⚠️ 1. `fatal: not a git repository`

 📌 Causa: estás ejecutando comandos Git fuera de un proyecto iniciado con `git init`.

✅ Solución:

* Verifica que estés dentro de un proyecto con Git:

  ```bash
  git status
  ```
* Si no lo es, inicialízalo:

  ```bash
  git init
  ```

---

### ⚠️ 2. `error: failed to push some refs to ...`

📌 Causa:

* Tu rama local está desactualizada respecto a la remota.
* Hubo cambios en remoto que aún no tienes.

✅ Solución:
Actualiza antes de hacer push:

```bash
git pull origin nombre_rama --rebase
git push origin nombre_rama
```

---

### ⚠️ 3. Cambié algo, pero no aparece en el `git status`

📌 Causa: el archivo está en `.gitignore` o no ha sido guardado.

✅ Solución:

* Asegúrate de haberlo guardado.
* Verifica `.gitignore`.
* Usa `git add -f archivo` si quieres forzarlo.

---

### ⚠️ 4. Subí archivos que no quería (como `.env` o `node_modules`)

📌 Causa: no configuraste `.gitignore` antes de hacer commit.

✅ Solución:
```bash
git rm --cached archivo_secreto
echo "archivo_secreto" >> .gitignore
git commit -m "Quita archivos sensibles"
```

---

### ⚠️ 5. Me equivoqué de rama al hacer commits

✅ Solución: guarda los commits en un stash:

```bash
git stash
git switch rama_correcta
git stash pop
```

---

### ⚠️ 6. Quiero deshacer el último commit (sin perder los cambios)

✅ Solución:

```bash
git reset --soft HEAD~1
```

---

### ⚠️ 7. Archivos con conflicto tras un `merge`
✅ Solución:

* Abre el archivo y busca los símbolos:

  ```
  <<<<<<< HEAD
  ...
  =======
  ...
  >>>>>>> rama
  ```
* Elimina las marcas y elige qué mantener.
* Luego:

  ```bash
  git add archivo
  git commit
  ```

Si no quieres seguir con el merge:

```bash
git merge --abort
```

---

### ⚠️ 8. `Permission denied (publickey)` al hacer `git push` o `git pull`

📌 Causa: gitHub no reconoce tu llave SSH.

✅ Solución:

1. Genera una llave SSH si no tienes:

   ```bash
   ssh-keygen -t ed25519 -C "tu_email@example.com"
   ```

2. Agrega la clave pública a GitHub:
   Copia con:

   ```bash
   cat ~/.ssh/id_ed25519.pub
   ```

3. Añádela en GitHub → **Settings > SSH and GPG keys**


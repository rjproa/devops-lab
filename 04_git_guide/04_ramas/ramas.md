# 🌿Ramas
Una rama es una línea paralela de trabajo dentro de tu proyecto, es como una rama que crece desde el tronco principal.
## 4.1 🔧 Administración de ramas
```bash
git branch nombre_rama         # crea una rama

git checkout nombre_rama       # cambiarse de rama
git checkout -b nombre_rama    # crear y moverse a esa rama

# versiones modernas
git switch nombre_rama         # cambiarse de rama
git switch -c nombre_rama      # crear y moverse a esa rama

git branch                     # listar ramas
git branch -m nombre_antiguo nombre_nuevo  # renombrar rama local
git branch -d nombre_rama      # eliminar rama local

git push origin --delete nombre_rama  # eliminar rama remota

```
## 4.2 🔀 Fusionar ramas  
El merge es el proceso de unir dos ramas diferentes en una sola. Es la forma principal de combinar el trabajo realizado en ramas separadas para que se integren en una versión común.

>📌 Por ejemplo, si tienes una rama feature donde desarrollaste una nueva función, y quieres que esa función esté en la rama principal main, haces un merge para combinar esos cambios.

### 🌟 Tipos de merge
1. Fast-forward merge</br>Sucede cuando la rama a fusionar está adelantada respecto a la rama actual y no hay divergencias. En este caso, git no crear nuevos commits sino que mueve el puntero hacia adelante.
   ```bash
   git checkout main # moverse a la rama que recibirá los cambios
   git merge feature # hacer merge con la rama que aportará los cambios
   ```
   ✅ Es importante que ```main``` no tenga nuevos commits desde que se creó ```feature```.

2. Merge con commit de fusión</br>Sucede cuando las ramas ```main``` y ```feature``` han sufrido cambios independientes (hay divergencias), git crea un ```commit``` de merge que une ambas historias en un solo punto.
   ```bash
   git checkout main # moverse a la rama que recibirá los cambios
   git merge feature # hacer merge con la rama que aportará los cambios
   ```
   🧩En caso ```main``` y ```feature``` sufireron cambios independientes pero sin tener conflictos entre estos mismos, git crea un commit simple. En caso haya conflicto en los cambios git pedirá resolver estos conflictos antes de completar el ```merge```.

## 4.3 ⚔️ Resolver conflictos  
Durante el merge, si las dos ramas modificaron la misma línea de un archivo, Git no puede decidir cuál cambio mantener y genera un conflicto. 

📌Pasos para resolverlo:
   - Abrir el archivo en conflicto.
   - Buscar las marcas ```<<<<<<<```, ```=======``` y ```>>>>>>>```.
   - Edita el contenido para resolver qué versión queda o combina ambos cambios.
   - Guarda el archivo.
   - Añade el archivo resuelto: ```git add archivo_en_conflicto```.
   - Termina el merge en un commit automático  ```git add```.

Cuando haces un ```git merge``` y surge un conflicto, Git detiene el proceso y espera que tú resuelvas los conflictos manualmente. Mientras tanto, tu repo queda en un estado de fusión incompleto.

🧠 ¿Y si quiero cancelar el merge?
<br>Si decides que no quieres continuar con ese merge, puedes abandonarlo y volver al estado anterior (antes de haber ejecutado el merge). Para eso sirve:
```bash
git merge --abort
```
🧠 ¿Cuándo usar git merge --abort?
- Te equivocaste de rama o no querías hacer el merge.
- El conflicto es muy grande o complejo y prefieres intentarlo de otra forma.
- Necesitas hacer otro cambio antes de fusionar.

> Si el comando ```git merge --abort``` no está disponible por versiones antiguas, puede usarse: ```git reset --merge```. Hace lo mismo, vuelve al punto anterior.
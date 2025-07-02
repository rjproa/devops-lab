# 🧱 Commits y Historial

¿Qué es un **commit**?  
Es como un punto de guardado en tu proyecto 🎮. Cada vez que haces un commit, estás tomando una fotografía del estado actual de tu código: quién lo hizo, cuándo, qué cambió y por qué.

Un commit contiene:

- 📝 Mensaje descriptivo
- 🔑 Identificador único
- 🕒 Fecha y hora
- 👤 Autor del cambio

📦 **Ejemplo de un commit:**
```bash
commit 9fceb02b213765b61b7a3b8c9b0087af60c61f89
Author: Juan Pérez <juan@example.com>
Date:   Mon May 20 14:22:18 2025 -0500

    Arregla bug en la autenticación
```
---

## 3.1 Comandos claves
```bash
git status                 # Ver los cambios realizados

git add nombre_archivo     # Agregar archivo al área de staging
git add .                  # Agregar todos los cambios al staging

git commit -m "Mensaje"    # Crear un commit con un mensaje


```
## 3.2 Consultar historial de commits
```bash
git log                            # Ver el historial completo
git log --oneline                  # Verlo en formato resumido
git log --author="nombre_autor"    # Ver solo los commits de un autor
git log nombre_archivo             # Ver historial de un archivo específico
git diff --staged                  # Ver diferencia entre el staging y último commit
git blame nombre_archivo           # Ver qué linea de código cambió y quién la modificó
```

## 3.3 Deshacer cambios y commits
```bash
git restore nombre_archivo.extension # restaura el archivo desde el último commit, borra los cambios que aún no han sido añadidos con git add.

git restore --staged nombre_archivo.extension # Quitas los cambios del área del staging.

git reset --soft HEAD~1 # Deshace los cambios del último commit, el commit desaparece regresando al commit anterior, pero los cambios de este se mantienen en el staged listo hacer un commit.

gi reset --mixed HEAD~1 # Los archivos modificados vuelven al área de trabajo (working directory), y salen del staging.

git reset --hard HEAD~1 # Deshace el último commit y borra todos los cambios, pierdes el staging y las modificaciones en tu proyecto. En otras palabras, pierdes todo el último commit y regresas al anterior.

git revert <hash_del_commit> #  Crea un nuevo commit que deshace los cambios del commit que indiques. Es el más recomendado al momento de trabajar con equipos.

git commit --amend -m "nuevo mensaje del commit" # reescribe el mensaje del último commit sin cambiar su contenido.

git show <hash_del_commit> # ver los cambios que se hicieron en un commit específico
```
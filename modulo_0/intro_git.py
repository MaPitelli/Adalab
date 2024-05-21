'''
Configurando repositorio Adalab Git

git add -A

git commit -m "Mensaje del commit"

git push


Para poder almacenar la contraseña de GitHub en Mac, abrimos una terminal y escribimos el siguiente comando:

git config --global credential.helper osxkeychain

Una vez hayamos realizado ese paso, no necesitaremos hacer ningún cambio más.


Ya sabemos usar los comandos de Git clone, add, commit, pull y push. Solo nos queda por aprender un comando importante: git status.

git status nos dice el estado actual en el que está nuestro repo. Es muy útil para saber lo que tenemos que hacer, o porqué estamos teniendo un problema que no nos deja avanzar.

Supongamos que yo acabo de de subir mi código con un git add -A, git commit -m "My message" y git push al repositorio remoto. Es decir mi repo local y el remoto están igual. Si yo escribo el comando git status me aparecerá:

On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   modulo_1/teste.py

no changes added to commit (use "git add" and/or "git commit -a")

'''
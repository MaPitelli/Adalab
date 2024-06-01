
'''
ls >> list files
ls -l >> long > Enseña una lista con más info sobre los archivos, tamaño en bytes, fecha de creación, etc.
ls -lh >> human > Lectura mas humana, en Kb, Gb, etc.

cd >> change directory >> Al poner solo cd, es un shortcut para llevar al directorio raíz.
cd .. >> Vuelve atrás solo una carpeta
cd ../.. >> Vuelve atrás dos carpetas
Para usar ruta relativa: cd ./ruta relativa
pwd >> Print Working Directory >> Ruta absoluta

clear >> clear the terminal
Cmd + L >> Parece que funciona como un ctrl + Z, deshacer el último comando.

Flecha para arriba o abajo: enseña los comandos que estuve usando. Guarda unos 1000 comandos.

file + nombre del archivo incompleto: completar con tab >> Enseña las características del archivo. 
file ./Documents/screenshot.png >> Otra manera de enseñar las características de un archivo usando la ruta.


Manipulando Archivos y directorios

ls -la >> list long all > Enseña todos los archivos incluyendo los ocultos.
ls -lS >> Size order > Ordena por tamaño (lSh long Size order Human)
ls -lSr >> Reverse > Reverse Size Order
ls -lr >> Reverse > Orden alfabético contrário
ls dir1 >> Enseña lo que hay dentro de la carpeta dir1


TREE SOLO PARA BASH:
tree >> Enseña el árbol de todo
tree -L 2 >> 2 Levels only
tree -L 1 >> 1 level only


mkdir >> Make directory > Para crear carpetas > Evitar de usar espacios
mkdir dir1 dir2 dir3 >> Crea las 3 carpetas a la vez

touch >> Crear archivos
touch file1 file2 file3 >> Crea archivos a la vez
touch file.py >> Se puede especificar la extensión

cp >> Copy
cp file1 file_bk >> Copy file1 as file_bk in the same directory

mv >> Move
mv file_bk .. >> Move file_bk una carpeta atrás

mv file_bk fileCopy >> Rename file_bk as fileCopy > Funciona tambien para renombrar carpetas

rm >> Remove
rm fileCopy >> Deleta el archivo fileCopy
rm -i fileCopy >> Interactive > Pregunta antes de remover > Muy útil > Hay que contestar y para yes, si no, no deleta. 

rm -r >> Recursive
rm -rf >> Force (cuidado!!! Borrado forzado)
rm -ri >> Recursive interactive > útil y más seguro > hay que contestar y para yes para cada archivo y carpeta.

mv dir1 dir2 >> Mover la carpeta dir1 dentro de la carpeta dir2


Explorando el contenido de nuestros archivos

head filename.extension >> Enseña las primeras 10 líneas de cualquier archivo de texto
head file.py -n 15 >> Enseña las primeras 15 líneas del archivo file.py

tail file.py >> Enseña las últimas 10 líneas de file.py
tail file.py -n 20 >> Enseña las últimas 20 líneas del archivo file.py

less file.py >> Entra en el archivo de manera interactiva. Una vez dentro, se puede hacer un find usando la /palabra_a_buscar
Para salir hay que darle a q para quit. 

open file.py >> Abre el archivo file.py en el programa default

Cuando se queda algún proceso abierto en el terminal y se quiere cerrarlo, solo hay que darle a control + C


Qué es un comando?
Un comando puede ser 4 cosas: 
1. Un programa ejecutable
2. Un comando de utilidad de la shell
3. Una función de shell
4. Un alias

type >> cuál es la clase del comando

type cd >> Retorna: cd is a shell builtin
type mkdir >> Retorna: mkdir is /bin/mkdir
type ls >> Retorna: ls is /bin/ls

alias l=“ls -lh” >> Se crea un alias l que va a ejecutar el comando ls -lh
Sirve para crear mis propios comandos. Muy poderoso. 
Los alias son temporales. Se pueden guardar, lo veremos en variables de entorno.

help >> Solo para Bash
info >> Solo para Bash
Para zsh: man
man ls >> Entra en el manual de ls, hay que darle a q para quit 
whatis cd >> Resumen de lo que es el comando


Wildcards

Las wildcards o comodines son una serie de caracteres especiales que nos permiten encontrar patrones o realizar búsquedas más avanzadas. Es aplicable para archivos y directorios.

Se usa con el comando ls

ls *.txt >> Retorna todos los archivos que terminen en txt
ls datos* >> Retorna todos los archivos que empiecen por datos
ls datos? >> Retorna todos los archivos que empiecen por datos y que tengan apenas 1 carácter después de datos
ls datos??? > Retorna todos los archivos que empiecen por datos y que tengan 3 caracteres después de datos
ls *.html >> Retorna todos los archivos que terminen en html
ls [[:upper:]]* >> Retorna todos los archivos que empiecen por mayúscula hasta 2 niveles de directorios
ls -d [[:upper:]]* >> Retorna solo los directorios que empiecen por mayúscula
ls -d [[:lower:]]* >> Retorna solo los directorios que empiecen por minúscula 
ls [ad]* >> Retorna todos los archivos que empiecen por a o por d
ls [ai]* >> Retorna todos los archivos que empiecen por a o por i


Redirecciones: Cómo funciona la shell

ls Documents >> Retorna todo lo que hay dentro de la carpeta Documents
ls Documents > myfiles.txt >> Genera el archivo myfiles.txt y guarda en ese archivo el listado de Documents
ls > myfile.py >> Genera el archivo myfile.py en la carpeta en la que estoy y guarda en ese archivo el contenido de la carpeta donde estoy

ls Dowloads > myfiles.py >> Genera el archivo myfiles.py y guarda en ese archivo el listado de Downloads

Al usar el señal de mayor > se sobre escribe el archivo, no se añade a lo que ya estaba.
Para concatenar, o sea, añadir sin borrar lo que ya estaba, hay que usar 2x la señal: >>

Los file descriptors son números que identifican un recurso. Funciona asociando un número con una acción, archivo o programa, en el caso de la shell tenemos 3 file descriptors: El 2 es Standard Error, El 1 es el Standard Output, el 0 es el Standard input.

Para hacer logs, si me sale un error y lo quiero guardar: 
ls kjskdjskjdks 2> error.txt >> Esto guarda el error “No such file or directory” en el archivo error.txt, hay que usar la 2, si no, no guarda el error. (Para ver el archivo de error.txt: head error.txt)

Para añadir a un archivo tanto el error como el output normal:
ls ahkjhajkahjkah > output.py 2>&1
Esto genera un error que se guarda en output.py
ls Documents > output.py 2>&1 - Esto genera un output normal, que es el listado de lo que está en Documents, que se guarda en output.py

Importante, no olvides: Si hay un > escribe por encima, si hay dos >> concatena. 

Use touch para crear un archivo vacío o actualizar marcas de tiempo.
Use > para redirigir la salida de un comando a un archivo, creando o sobrescribiendo su contenido.


Redirecciones: Pipe Operator

echo “Hola mundo!” >> Retorna Hola mundo! echo es como el Print en Python
cat error.txt output.txt >> Concatena los archivos error y output en ese orden

Pipe operator es un operador que permite tomar la salida de un comando y pasarla como entrada de otro comando. Ejemplo: ls -lh | less >> Este comando hará el less en cima del resultado de ls -lh

ls -lh | tee output.py | less >> El listado ls -lh se crea con el tee en el archivo output.py que luego se explora con less

ls -lh Pictures | sort | tee pics.py | less >> Se hace el listado ls -lh de la carpeta Pictures, se ordena, se crea un archivo con ese listado y luego se explora con less

cowsay -t “Hola” >> Comando que imprime una vaca diciendo Hola
echo “Hola mundo” | lolcat >> imprime Hola mundo en colores 

cowsay -t “Hola amigos” | lolcat >> Vaca colorida diciendo Hola amigos


Encadenando comandos: operadores de control

Los operadores de control son símbolos reservados por la terminal que nos permiten encadenar comandos.
Si usas constantemente la tecla enter para ejecutar varios comandos, puedes evitarlo si usas el operador ; que separa los comandos que estamos ejecutando.

ls; mkdir holi; cal >> Listar contenido, después crea la carpeta holi, después imprime un calendario

cal >> imprime calendario
date >> imprime fecha y hora

Para llevar a cabo varios comandos, al mismo tiempo, usamos el operador & entre cada comando:
date & echo "Hola" & cal

Condición and (&&)
Si escribimos varios comandos separados por el operador && estamos indicando que para que estos se ejecuten, el comando anterior tuvo que ejecutarse correctamente.
mkdir test && cd test >> Para que se ejecute cd test, primero hay que ejecutarse mkdir test.

Condicional or (||)
Al condicional or no le importa si el comando anterior se ejecutó o no, simplemente va probando todos los comandos a ver cuál se ejecuta.
cd akjslkajlsj || echo “Hola” >> Esto va a saltar un error y luego se ejecuta el echo


Cómo se manejan los permisos

Los permisos son las capacidades que tiene cada usuario dentro del sistema operativo, no todos los usuarios pueden hacer todas las acciones sobre ciertos archivos y carpetas.

Tipos de archivos
El primer caracter puede ser uno de estos 3:
| - | Es un archivo normal, como un documento de texto, una foto, un video, etc. 
| d | Por directory es un directorio 
| l | Es un enlace simbólico. Es algo que veremos en próximas clases
| b | Bloque especial, son archivos que manejan información para el sistema, como la información de un disco duro


Permisos de usuario
Los siguientes caracteres se leen de 3 en 3, por cada uno de los tipos de usuario.
Owner
El dueño del archivo, si no se ha cambiado, es quien lo creo y tiene mayor jerarquía sobre los otros 3. Le corresponden los primeros 3 caracteres de los permisos.
Group
Se puede crear grupos de usuarios para darle a todos o varios los mismos permisos. A estos usuarios le corresponden el cuarto, quinto y sexto carácter de los permisos de usuarios y tienen mayor jerarquía que el último.
World
También llamado "otros", es cualquier otro usuario que no pertenezca a un grupo de usuario y tampoco sea el dueño, este tiene la menor jerarquía.


Tipos de permisos
| r | readable | Significa que puede leer su contenido 
| w | writable | El usuario puede editar el contenido del archivo, también el nombre y los permisos 
| x | executable | El usuario puede ejecutarlo en caso de que sea un programa 

Los permisos se escriben en ese orden rwx. Para indicar que el permiso no está disponible, se escribe un guion.

Ahora que sabes todo esto vamos con un ejercicio. Observa el siguiente grupo de permisos: drwxr-xr-x Recuerda que el primer caracter es el tipo y los siguientes se cuentan de 3 en 3 representando cada usuario.

| d | Esto es un directorio 
| owner | group | world | 
| rwx      | r-x      | r-x | 
El dueño puede leer, escribir y ejecutar
El grupo puede leer y ejecutar 
Los demás pueden leer y ejecutar

Vamos con otro
-rw-r--r--
| - | Esto es un archivo normal, como una imagen o un video 
| owner | group | world |
| rw-      | r--      | r--      | 
El dueño puede leer y escribir
El grupo sólo puede leer 
El resto sólo puede leer 

Representando permisos de forma octal
Si organizamos los permisos de esta forma: owner: rwx, group: r-x, world: r-x
E indicamos con un cero si el usuario no tiene el permiso y con un uno si el usuario si lo tiene, pongamos de ejemplo el permiso rwx: 1 1 1, r-x: 1 0 1, r-x: 1 0 1, la representación en modo octal sería. Para 111: 4, 2 y 1 - La suma es 7, para 101: 4, 0, 1 - la suma es 5. 

Tabla de referencia modo Octal

Octal	Binario	Permisos
0		000		---
1		001		--x
2		010		-w-
3		011		-wx
4		100		r--
5		101		r-x
6		110		rw-
7		111		rwx


Modo Simbólico

u - Solo para el usuario
g - Solo para el grupo
o - Solo para otros (es el world)
a - Aplica para todos



Modificando permisos en la terminal

Con el comando chmod podemos cambiar los permisos de los archivos de dos formas, una es usando los símbolos (rwx) y otra es con el sistema octal.


Cómo cambiar los permisos de un archivo (chmod)
Es bastante sencillo cambiar los permisos de forma simbólica. Para esto, hay que escribir después del comando chmod el símbolo del usuario, luego el operador y por último el permiso que quieres agregar o quitar.

chmod [simboloDelUsuario][operador][permiso] [archivoParaCambiarSusPermisos]

Supongamos que queremos añadirle permiso de escritura al grupo, entonces tenemos que escribir lo siguiente: chmod g+w ProyectoExplosivo.txt

Puedes cambiar varios permisos de varios usuarios al mismo tiempo, por ejemplo, si quisieras agregar el permiso de escritura y ejecución al grupo y a otros, sería así: chmod go+wx [archivo]

Y si quieres permisos diferentes para cada usuario, solo sepáralos por comas: chmod u+r,g=w [archivo]
En ese comando se le añadió el permiso de lectura al dueño y de escritura al grupo. No agregues espacio en las comas o provocarás un error.

También puedes cambiar los permisos usando su forma octal, por ejemplo el conjunto de permisos rwxr-xr-x en su forma octal es 755. chmod 755

cat > file.py >> Este comando te deja escribir en el prompt del terminal lo que va en file.py
Pra terminar de escribir hay que presionar ctrl + D

chmod u-r file.py >> Este comando quita el permiso de read del user sobre el file.py
Para volver a darle permiso, hay que usar el mismo comando con el +: chmod u+r file.py 

chmod u-x,go=w file.py >> quitar el permiso de executable del user y dar permiso de write al grupo y others, todo para el archivo file.py y todo a la vez. La señal de = sobrescribe los permisos, cuidado, para añadir se usa el +

+ Añade
- Quita
= Assigna


Cómo gestionar usuarios (whoami | su)
El comnando whoami, literalmente "¿Quien soy yo?", te muestra cual es el usuario que se está ejecutando, esto es porque a veces podemos olvidar con cual usuario estamos trabajando.
Cuando listamos los archivos con ls -l la tercera columna muestra el nombre del usuario que es propietario del archivo y la cuarta columna muestra el grupo que tiene control sobre el archivo.

whoami >> Comando que dice en que user estoy

id >> Retorna el user identity

Para cambiar de usuario se usa el comando su Switch User, seguido del usuario al que quieres cambiar, en este caso vamos a cambiar al superusuario root. Cuando ejecutes este comando te pedira que coloques su contraseña.

su root >> Esto hace switch user to root

Y aqui una advertencia: el superusuario root (sí, ese es el nombre técnico) tiene poder para hacer y deshacer con el sistema operativo, puedes eliminar cosas que no deberías eliminar y puede hacer mucho desastre. Usa los privilegios del root con cuidado.

touch ArchivoRoot.txt; ls -l >> crear un archivo con root y listarlo

sudo me permite ser el usuario root temporalmente, no hace el login como root pero sí te da los permisos. 

¿Qué hacer en caso de olvidar una contraseña?
Si estás usando Windows Subsystem for Linux (wsl) y se te olvidó la contraseña del root. Sigue estos pasos:
* Abre el cmd de windows y ejecuta este comando wsl --user root. Esto hará que se inicie en la terminal wsl con el usuario root.
* Luego ejecuta el comando passwd root el cual te permitirá cambiar la contraseña del usuario root.
Ya con esto puedes volver a la terminal de wsl y volver a ejecutar el comando su root.


Cambio de contraseña del user en el que estoy: passwd
Hay que poner la contraseña actual y la nueva. 


Cambiar el propietario (chown)
Puede que no te quieras hacer responsable de tus archivos, así que se los quieres dejar a alguien más. Para eso usa el comando chown Change Owner. La sintaxis es muy simple: chown [usuarioAlQuePertenecerá] [archivo]


Tabla de comandos whoami, su y chmod

whoami | Muesta el usuario con el que se está trabajando
su | Switch User Cambia al usuario al que le especifiques 
chmod | Cambia los permisos de un archivo 
chown | Change Owner Cambia el propietario de un archivo


** Bonus ** Links simbólicos
ln -s <ruta> <Nombre> Esto para hacer link simbólicos, que son un tipo de archivo que hacen referencia a otro lugar, básicamente es un acceso directo desde terminal.

ln -s Documents/Dev Desarrollo >> El link simbólico desarrollo apunta a la carpeta Documents/Dev

Ejemplo de uso de enlaces simbólicos:

Supongamos que tienes un archivo llamado imagen.jpg en tu directorio de imágenes (/home/usuario/imagenes). 
Puedes crear un enlace simbólico llamado imagen_enlace.jpg en tu escritorio (/home/usuario/Escritorio) que apunte al archivo original. 
Para hacerlo, ejecutarías el siguiente comando en la terminal:

ln -s /home/usuario/imagenes/imagen.jpg /home/usuario/Escritorio/imagen_enlace.jpg

Ahora, puedes abrir o acceder al archivo imagen.jpg desde tu escritorio usando el enlace simbólico imagen_enlace.jpg.

Imagina que trabajas en un proyecto que requiere acceder a archivos ubicados en un servidor remoto. 
Puedes crear enlaces simbólicos en tu computadora local que apunten a los archivos en el servidor remoto. 
Esto te permite trabajar con los archivos como si estuvieran en tu computadora local, sin tener que descargarlos y cargarlos constantemente.
Los enlaces simbólicos son una herramienta útil y versátil que puede ayudarte a organizar archivos y directorios, acceder a archivos en diferentes ubicaciones y mantener enlaces actualizados.


Variables de entorno

* La terminal tiene una configuración con diferentes valores, que se pueden acceder con las variables de entorno. Estas son muy importantes para la configuración general del sistema.
* Podemos guardar alias para que se queden de manera permanente con esto.


Cómo configurar variables de entorno

Las variables de entorno son útiles cuando necesitamos que cierta información prevalezca para poder trabajar más rápido o necesitamos guardar información para no tener que recordarla constantemente. Siempre se crean en mayúsculas.

printenv >> imprime todas las variables de entorno que tengo configuradas

echo $<variables> esto nos sirve para imprimir una variable en particular.

PATH tiene todas las rutas donde se encuentran los binarios en los que se ejecuta nuestro sistema. Hay varios manejadores de paquetes para binarios, pero no todas las veces se agregan a PATH, y se deben agregar a mano.


Ejemplos de variables de entorno comunes:
* PATH: Almacena la lista de directorios donde el sistema busca comandos ejecutables.
* HOME: Indica el directorio personal del usuario actual.
* USER: Contiene el nombre de usuario del usuario actual.
* LANG: Especifica el idioma y la configuración regional del sistema.
* TEMP: Define la ubicación predeterminada para almacenar archivos temporales.
* ZSH_VERSION: Indica la versión del zsh que estás utilizando.
* SHELL: Dirección de la shell que estás utilizando.

Cómo acceder y modificar variables de entorno:
* Acceder a variables de entorno: En la mayoría de los sistemas, se puede acceder al valor de una variable de entorno utilizando el nombre de la variable precedido por un signo de dólar ($). Por ejemplo, para obtener el valor de la variable PATH, se puede usar el comando: echo $PATH

echo $HOME

* En HOME, existe un archivo que se llama .zshrc que es donde está nuestra configuración de zsh. Lo podemos abrir con VS Code para modificarlo. En este archivo podemos crear alias.
* Estando en el directorio home, usar ls -la para confirmar que el archivo .zshrc está en esta carpeta. 
    * Luego usar el comando: code .zshrc para abrir el archivo usando VSC. 
    * Luego solo hay que añadir los alias, guardar con superusuario y contraseña y usar el comando: source ~/.zshrc para actualizar. 
    * Todo listo para usar los nuevos alias permanentes. Si no se quiere mas el alias, solo hay que borrarlo del archivo .zshrc, guardar y actualizar.

* alias <nombre>="comando" para crear un alias útil.
* Para modificar o crear una variable de entorno, se hace, por ejemplo PLATZI_MESSAGE=“Hola amigos". Siempre sin espacios !!!
* Para agregar una ruta a la variable PATH ponemos en .zshrc PATH=$PATH:<ruta>, guardamos, atualizamos zsh en la terminal, y listo.
* Es muuuy importante tener cuidado con los alias, nunca hay que nombrar un alias como un comando ya existente.

* code <archivo> para abrir un archivo en VS Code desde la terminal > Hay que estar en el directorio del archivo en la terminal !!!
* Si estoy por ejemplo en el directorio /Users/mairapitelli/git/Adalab y escribo el comando: code . me abre la carpeta Adalab en VSC. 



Comandos de Búsqueda

which cd >> Retorna which: no cd in ($PATH)
Esto ocurre porque cd no es un binario. Al hacer el comando: type cd >> retorna cd is a shell buitin. 

Ahora si hacemos: which code para ver donde está Visual Studio Code, retorna: /usr/local/bin/code

find ./ -name <nombre del archivo que busco>
El comando find va a buscar un archivo en todos los directorios del ordenador y retorna todos los directorios donde encuentra el archivo. 

Usando wildcards con find

find ./ -name *.txt >> retorna todos los archivos con extensión txt que encuentre

find ./ -name *.txt | less >> Otra opción usando less

find ./ -type d -name Documents >> Busca por tipo directorio la carpeta de nombre Documents

find ./ -type f -name *.log >> Busca por tipo file todos los archivos que tengan la extensión .log en el nombre

find ./ -size 20M >> Busca por tamaño todos los archivos que sean mayores que 20Mb



Comando grep: Usa expresiones regulares

cat unArchivoLargo.txt | grep "La línea que busco"
# cat Te listará todo el contenido de ese archivo
# grep te filtrará únicamente lo que quieres ver

grep "string" archivo_*
# grep buscará la palabra "string" en todos los archivos que comienzen por "archivo_" y te los mostrará.

ls -al | grep myFile.txt
# ls te dará la lista de todos tus archivos
# grep filtrará todos y te mostrará únicamente el que deseas

grep -i the movies.csv | less >> Retorna todos las peliculas dentro de movies.csv que empiecen por The, la i es para ignorar el case sensitive

grep -c the movies.csv >> c para count, retorna el numero de veces que hay la palabra the dentro del archivo movies.csv
Si el lugar de -c se usa -ci ignora el case sensitive y aumenta el número de resultados

grep -vi towers movies.csv >> retorna todas las peliculas, excepto las que contengan towers, ignora el case sensitive y considera Towers o towers. 

grep -vi towers movies.csv > sintowers.txt >> Esto guarda el resultado del filtro en el archivo sintowers.txt


Comando wc: word count

wc movies.csv >> retorna 3 numeros: el primer es cuantas líneas hay, el segundo es cuantas palabras hay y el tercer es el número de bits. 

wc -l  miarchivo.txt >> Retorna el número de lineas de miarchivo.txt 

wc -w  miarchivo.txt >> Retorna el número de palabras de miarchivo.txt

wc -c  miarchivo.txt >> Retorna el número de bits de miarchivo.txt


Imagina que tienes un archivo llamado test.txt y adentro contiene la siguiente frase: Imagina que quieres buscar algo
Entonces, podemos usar grep así:

grep "Imagina .* algo" test.txt

# grep buscará alguna coincidencia, la expresion .* indica que ahí dentro puede haber una o más letras, cualquier que sea, así que podrías leerla como: Imagina (cualquier cosa) algo.
Esto encontrará justo la frase que quieres: Imagina que quieres buscar algo








'''
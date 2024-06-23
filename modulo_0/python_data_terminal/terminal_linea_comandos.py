
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


Utilidades de Red 

1. ifconfig:
* Función: Muestra la información de configuración de los dispositivos de red, incluyendo la dirección IP, la máscara de red, la dirección MAC y el estado de la conexión.
* Ejemplo: ifconfig
* Salida:
lo0: flags=8000<UP,LOOPBACK,RUNNING,MULTICAST> mtu: 16384
	inet 127.0.0.1 netmask 0xff00.0000.00ff.ffff loopback
	inet6 ::1 prefixlen 128 fe80::1%lo0 scopeid 0xf000001
	ether 00:00:00:00:00:00

en0: flags=8023<UP,RUNNING,BROADCAST,MULTICAST> mtu: 1500
	inet 192.168.1.100 netmask 255.255.255.0
	inet6 fe80::20c:29ff:fe5d:972e prefixlen 64 scopeid 0x4
	ether 00:25:90:2f:2a:55

2. netstat -i:
* Función: Muestra una lista de interfaces de red activas y su estado.
* Ejemplo: netstat -i
* Salida:
Name Mtu  Receive  Transmit
lo0    16384   12432562 10812864
en0    1500    1399728   1348624

3. ping:
* Función: Envía paquetes de información a una dirección IP o nombre de host para verificar la conectividad y medir el tiempo de respuesta.
* Ejemplo: ping www.google.com
* Salida:
PING www.google.com (142.250.189.142) 56(84) bytes of data.
64 bytes from 142.250.189.142: icmp_seq=1 ttl=116 time=11.4 ms
64 bytes from 142.250.189.142: icmp_seq=2 ttl=116 time=12.2 ms
64 bytes from 142.250.189.142: icmp_seq=3 ttl=116 time=12.1 ms
64 bytes from 142.250.189.142: icmp_seq=4 ttl=116 time=11.8 ms
--- google.com ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3004ms
rtt min/avg/max/mdev = 11.377/11.972/12.508/0.400 ms

Opciones de parámetros para el comando ping:
* -c <número>: Limita el número de paquetes a enviar.
* -s <tamaño>: Especifica el tamaño de los paquetes en bytes.
Para hacer pruebas con paquetes de 20 bytes escribimos:
ping -s 20 www.google.com


4. curl:
* Función: Descarga y muestra el contenido de una URL por la consola.
* Ejemplo: curl www.google.com
* Salida:
<!DOCTYPE html>
<html lang="es"><head>
<meta charset="utf-8">
<title>Google</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="Search the world's information, including webpages, images, videos, and more.">
<meta name="keywords" content="Google, search, information, world, webpages, images, videos">
<meta name="theme-color" content="#4285f4">
<link rel="icon" href="https://www.google.com/favicon.ico" type="image/


5. wget:
* Función: Descarga archivos de una URL y los guarda en un archivo local.
* Ejemplo: `wget www.google.com`
* Salida:

--2024-06-02 15:14:34--  https://www.google.com/ [192.168.1.1]
Connecting to www.google.com (192.168.1.1):64546... connected.
HTTP request sent, awaiting response... 301 Moved Permanently
Location: https://www.google.co.uk/
--2024-06-02 15:14:35--  https://www.google.com/ [192.168.1.1]
Reusing existing connection to www.google.com (192.168.1.1):64546.
HTTP request sent, awaiting response... 200 OK
Length: 34442 (34 KiB) [image/png]
Saving to: index.html
100% [██████████████████████████████████████████████████████████] 34442/34442 (33 KiB) in 3.6s (9.38 KiB/s) 2024-06-02 15:14:37 --Downloaded: 1 file in 3.6s (9.38 KiB/s)


Opciones de parámetros para wget:

* -O <archivo>: Especifica el nombre del archivo de salida.
* -q: Silencia la salida verbose del comando.
* -c: Continúa descargando un archivo parcialmente descargado.


6. traceroute:

* Función: Muestra la ruta que toman los paquetes de datos para llegar a un destino específico, incluyendo los tiempos de respuesta de cada salto.
* Ejemplo: traceroute www.google.com
* Salida:

traceroute to www.google.com (142.250.189.142), 30 hops max, 60 byte packets
1  192.168.1.1 (192.168.1.1)  1.299 ms  1.227 ms  1.184 ms
2  router.example.com (10.0.0.1)  11.785 ms  10.902 ms  10.821 ms
3  edge-router.example.com (10.1.0.1)  22.345 ms  21.678 ms  21.501 ms
4  provider-router.example.com (10.2.0.1)  33.456 ms  32.789 ms  32.612 ms
... (26 more hops)
29  142.250.186.147 (142.250.186.147)  56.789 ms  55.012 ms  54.934 ms
30  142.250.189.142 (142.250.189.142)  57.890 ms  56.123 ms  55.456 ms


Opciones de parámetros para traceroute:

* -n: No muestra los nombres de host, solo las direcciones IP.
* -m <saltos_máximos>: Limita el número máximo de saltos a rastrear.
* -p <puerto>: Especifica el puerto al que enviar los paquetes de prueba.

Consejos adicionales:

* Para obtener ayuda detallada sobre un comando específico, use el comando man <nombre_comando>.
* Combine comandos con pipes | para procesar la salida de uno en otro.
* Use alias para crear accesos directos a comandos complejos o frecuentemente utilizados.
* Explore herramientas gráficas de red como `nmap` y `wireshark` para análisis más profundos.



Comprimiendo archivos tar y zip


Puedes aprender a crear archivos comprimidos .zip o .tar que vemos en nuestro sistema operativo. Estos encapsulan muchos archivos e incluso carpetas.
Comprimiendo archivos con formato .tar
El formato .tar es un tipo de compresión bastante usado en UNIX. Originalmente era utilizado para almacenar información en cintas magnéticas, así que está hecho especialmente para comprimir los archivos de forma lineal.
Para comprimir con este formato en la terminal usamos el comando tar que tiene ciertas opciones para aprender.
Sintaxis:
tar [opciones] [nombreDelArchivoComprimido] [archivoAComprimir]
Comprimir (-c)
Para comprimir un archivo utilizamos la opción -c. En todos los casos hay que usar la opción -f para indicar que estamos comprimiendo o descomprimiendo archivos.
tar -cf compressed.tar Documents/toCompress/

Ver lo que está haciendo el comando (-v)
Si queremos ver lo que el comando está comprimiendo a medida que se va ejecutando, usamos la opción -v. Por cierto la opción -v es de "Verbose" y muchos comandos la usan, también te la puedes encontrar como --verbose.
tar -cvf compressed.tar Documents/toCompress/ 
    tar -cvf <archivocomprimido.tar><carpeta que queremos comprimir> >> comando tar, parámetros compress, verbose, file.

Comprimir con formato ".tar.gz" (-z)
El formato ".tar.gz" o también ".tgz" es una versión extendida del formato tradicional de compresión ".zip" que puede manejar y comprimir archivos más grandes.
Para manejar la compresión de archivos ".tar.gz" o ".tgz" se usa la opción -z además de tener que especificar en el nombre de archivo la extensión que quieres usar.
tar -czvf compressed.tar.gz Documents/toCompress/
    tar -cvzf tocompress.tar.gz ToCompress >> comando tar, parámetros compress, verbose, gz tipo de compresión, file, archivo que será generado, directorio que será comprimido. 


Descomprimir (-x)
Para descomprimir es mucho más sencillo, solo hay que especificar la opción -x y el archivo comprimido que se quiere descomprimir.
Si se quiere descomprimir un archivo de extensión ".tar.gz" o ".tgz" hay que especificar la opción -z también.
tar -xzvf compressed.tar.gz 
    tar -xzvf <archivo a descomprimir>.tar.gz
    tar -xvf <archivo a descomprimir>.tar


Comprimiendo archivos .zip
Para comprimir usamos el comando zip con el nombre que quieres que tenga y lo que quieres comprimir.
Si quieres comprimir una carpeta con archivos dentro, tienes que especificar la opción -r de "recursive".
zip -r compressed.zip Documents/toCompress/
    zip -r <nombre del archivo a comprimir>.zip <directorio que se quiere comprimir>


Y para descomprimir es incluso más fácil, solo escribe el comando unzip seguido de lo que quieres descomprimir.
unzip compressed.zip
    unzip <nombre del archivo a descomprimir>.zip

Hay también el comando rar para comprimir, casi idéntico al zip, y para descomprimir se usa el unrar


Tabla de comandos tar y zip

    Opciones del comando tar
    Recuerda siempre colocar la opción -f. 

    | Opción | Función | 
    | --- | --- | 
    | c | Comprimir | 
    | x | Descomprimir | 
    | z | Especifica que lo que se va a comprimir o descomprimir tiene extensión ".tar.gz" o ".tgz" | 
    | v | Muestra lo que está comprimiendo o descomprimiendo |

    Comando zip
    Recuerda que si lo que vas a comprimir es una carpeta tienes que usar la opción -r.
    | Comando | Función | 
    | --- | --- | 
    | zip | Comprimir | 
    | unzip | Decomprimir |



Manejo de Procesos

ps >> Ver los procesos que están activos en la terminal 

Para matar procesos, se hace un ps para ver los procesos que están activos, luego se coge el ID del proceso que se quiere matar y se usa el comando kill

kill 25367
pkill -nombre >> Para matar el proceso por nombre

Comando top: Nos muestra los procesos que están usando mas recursos
Se puede teclear h cuando esté el tor ejecutándose para help, así se puede ver los parámetros.

Comando htop es aún mas completo que el top, puede que haya que instalarlo >> Investigar antes de usar




Como viste en la clase de procesos podemos correr de manera asíncrona comandos, y si estos no se completan quedarán activos dentro de los procesos de la terminal.
Cuando un proceso está en ejecución sin que sea mostrado en la terminal se dice que se está ejecutando en el background. 
Si se muestra la ejecución del comando dentro de la terminal se dice que está en el foreground. En esta clase aprenderás a cómo mover los procesos del background al foreground a tu voluntad, incluso a cómo suspenderlos.
¿Te acuerdas del truco que aprendimos para tener un editor de texto supersencillo en la terminal? Lo usaremos en esta ocasión. Imagina que queremos una nota desde la terminal y para eso usamos:
cat > mi_nota.txt 
Nuestra terminal se verá con el prompt esperando a que ingresemos texto.

Podemos escribir algo y después terminar el input del texto con CTRL+D, pero en esta ocasión no haremos eso. Lo que queremos hacer será suspender el proceso, esto lo podemos hacer con CTRL+Z. 
El resultado que nos mostrará la terminal deberá ser uno donde nos indique la suspensión del comando cat.

Ahora hemos movido nuestro comando exitosamente al background de la terminal. Para consultar todos los procesos que tenemos en background podemos hacerlo con el comando jobs.

A la izquierda aparece el número del trabajo (!!! cuidado que no es lo mismo que el process ID). 
Si queremos traer la ejecución de nuevo a la terminal, es decir, al foreground; debemos usar el comando fg y especificar qué número de trabajo queremos continuar. Para nuestro caso será el 1.
fg 1 

En caso de que estés usando ZSH como shell el formato para llamar el trabajo sería con un porcentaje. ZSH tiende a interpretar algunas cosas incluyendo las wildcards de manera diferente.
fg %1 

Una vez enviado al foreground veremos como se activa la ejecución del comando en la terminal y podremos seguir escribiendo nuestra nota. 
Recuerda que una vez terminemos de escribir presionamos CTRL+D para terminar el input y guardar.

Cuando se guarda nuestra nota nos daremos cuenta de que el proceso por fin termina y si usamos jobs no nos mostrará ningún trabajo en background.

Existen otras formas de enviar comandos al background. La primera es usando el operador de control & al final de un comando. 
Este operador nos permite enviar de manera directa un proceso al background una vez ejecutado. Por ejemplo:
cat > mi_nota.txt & 

La segunda forma es con el comando bg. Este sirve de manera similar que fg solo que en vez de traerlo al foreground este lleva un trabajo al background. Por ejemplo:
bg 1 

Bien, la pregunta ahora es ¿Cómo usamos bg? Imagina que abrimos algún programa de interfaz gráfica desde la terminal. En mi caso abriré el navegador Google Chrome. Para hacerlo desde la terminal solo ejecuta:
google-chrome-stable 
Y verás como se ejecuta pero no nos deja hacer ninguna otra tarea ya que la ventana del navegador está abierta:
Para suspender el proceso como ya sabes lo hacemos con CTRL+Z y si revisamos con jobs veremos como el proceso se encuentra en pausa. 
En este caso la ventana del navegador que se abrió no nos dejará interactuar ni escribir en ella.

Como se ve en la imagen el navegador tiene el número de trabajo 1. Para dejar nuestro navegador corriendo y al mismo tiempo seguir trabajando en la terminal tenemos que reactivar este proceso y a la vez mandarlo al background. 
Para ello ejecutamos:
bg 1 
Con esto podremos ver como nuestro proceso de Google Chrome sigue corriendo en el background dejando la terminal disponible para nosotros.



Editores de texto en la terminal

Cómo usar Vim en la terminal
Para abrir o crear un archivo utilizando Vim escribe el comando vim [nombre del archivo]

Por defecto no podrás escribir hasta que actives el modo de inserción. Para hacerlo usa la tecla i.

Para salir del modo de inserción presiona la tecla escape. En el modo normal (en el que no puedes escribir) si escribes el slash / activarás un buscador similar al del comando less.

Para borrar una línea, estando el modo normal, tienes que ubicarte sobre ella y presionar dd.

Para guardar y salir presiona estando en el modo normal, activa los comandos usando : y escribe "wq". La letra "w" es para guardar y la letra "q" es para salir, también los puedes usar por separado.

Luego podemos revisar el contenido con el comando cat.

Tabla de comandos para uso de Vim
vim >> Abre el archivo especificado. Si no existe lo crea
:q >> Cierra el editor
:w >> Guarda los cambios
/[busqueda] >> Busca dentro del texto 
dd >> En el modo normal, selecciona una línea y la borra


'''
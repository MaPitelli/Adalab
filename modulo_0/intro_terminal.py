'''
Cómo usar la terminal

Como ya hemos instalado y configurado la terminal de nuestro ordenador vamos a explicar para qué es y cómo se usa. 
Si te resulta complejo no te preocupes es algo que vamos a usar y practicar durante todo el curso. ¡¡¡Te ayudaremos a dominarla!!!

¿Por qué necesitamos usar la terminal?
Como hemos comentado, la terminal, también llamada consola de comandos o shell, es una herramienta fundamental para la programación. 
Su finalidad es ejecutar comandos u órdenes mediante instrucciones. 
Estos comandos son similares a las interacciones que haríamos en una aplicación normal (clics, escribir en campos de texto, cambiar de sección, etc.) pero en este caso se hacen escribiendo órdenes en una terminal de comandos.

Muchas de las herramientas para programación están hechas sin interfaz porque son tan sencillas que no merece la pena hacer una interfaz
o son tan complejas que no se puede hacer una interfaz gráfica que tenga todas las funcionalidades posibles. La solución es usar la terminal.

Cuando una persona utiliza un programa como Spotify o Chrome está utilizando una interfaz gráfica que transforma nuestras acciones en órdenes que le envía al sistema operativo a través de una terminal. 
Es decir las aplicaciones son intermediarias. Cuando utilizamos la terminal directamente no hay nada que se interponga entre el sistema operativo y nosotras. 
Tenemos todo el poder, y toda la responsabilidad claro, pero tranquila, no podemos romper nada 😉


Partes de la terminal

Lo primero que nos muestra la terminal es el prompt, a partir del cual podemos escribir nuestros comandos. El prompt está compuesto por:

Nombre del usuario con el que hemos iniciado sesión en el ordenador. En la imagen es migueldelmazo.

@

Nombre del equipo u ordenador. En la imagen es Miguel.

Ruta de la carpeta en la que está ahora mismo la terminal:

Puede ser la ruta absoluta de una carpeta. En la imagen es /mnt/c/Users/miguel/Desktop/dev/adalab/materiales-l.

O podría ser otra cosa como ~, que es una abreviatura de la carpeta home del ordenador de la usuaria.

Por último el símbolo del dólar, que es simplemente para saber dónde termina el prompt y dónde podemos empezar a escribir un comando.

Nota: A veces, en nuestros materiales o en Internet, encontraremos ejemplos de comandos precedidos por el símbolo del dólar, por ejemplo $ ls -la. 
Es una manera de decir que es un comando de terminal. Nosotras no debemos escribir el $ en la consola.

En el ejemplo también hemos escrito el comando ls -la y le hemos dado a intro. 
Este comando es para listar los ficheros y carpetas que están dentro de la carpeta en la que está la terminal. 
Es decir los ficheros y carpetas que están dentro de /mnt/c/Users/miguel/Desktop/dev/adalab/materiales-l. 
Por ello la terminal nos muestra el listado de ficheros y carpetas que vemos en la imagen, con información relativa a cada uno de ellos.

Y ahora que ya sabemos cómo escribir comandos en la terminal vamos a ver los más comunes y usados en programación:


Comandos (más usados) de la terminal

ls (list)
El comando ls nos muestra un listado de los archivos y carpetas que hay en la carpeta actual.

ls -la
A los comandos se les puede pasar opciones. Podemos usar la opción especial -la para listar también los ficheros y carpetas ocultos. 
La opción -l indica que queremos ver los ficheros en modo listado. La opción -a indica que queremos ver todos (all) los ficheros y carpetas, incluidos los ocultos. 
La opción -la es la suma de las dos opciones juntas. Los ficheros y carpetas ocultos empiezan por . y por defecto no se ven ;). Por ejemplo un fichero oculto es .gitignore.

Nota: Por cierto, ni Windows, ni Mac, ni Ubuntu muestran por defecto los ficheros ocultos de una carpeta. 
Pero si abrimos la carpeta desde VS Code, este sí muestra los ficheros ocultos. 
Sí quieres ver los ficheros y carpetas ocultos abre una carpeta en VS Code y pulsa en icono de arriba a la izquierda , aparecerán todos los ficheros que tenga esa carpeta.


cd (change directory)
El comando cd nos ofrece diferentes posibilidades a la hora de cambiar o movernos de carpeta. Para entrar en una carpeta hija de la carpeta actual usamos:
cd nombre-de-carpeta-hija

Podemos encadenar varios nombres de subcarpetas separadas por / para llegar hasta una ruta más profunda:
cd nombre-de-carpeta-hija/carpeta-nieta/carpeta-bisnieta

Los dos puntos .. nos permite subir a la carpeta madre, esto es, ir a la carpeta que contiene nuestra carpeta actual:
cd ..

Nota: Todo lo que aprendimos sobre rutas relativas y absolutas lo usamos mucho con los comandos de la terminal, en especial con el con el comando cd.


mkdir (make directory)
Nos permite crear una carpeta. Pero no entra en la carpeta, solo la crea.
Para crear la carpeta proyecto escribimos el comando: mkdir proyecto
Para entrar dentro de la carpeta que acabamos de crear mira el punto anterior cd.


cp (copy)
Para copiar ficheros (o carpetas) usamos el comando cp seguido del fichero (o carpeta) de origen, un espacio y la ruta del fichero (o carpeta) de destino:
cp fichero-de-origen.html carpeta-de-destino/fichero-de-destino.html


mv (move)
Para mover ficheros (o carpetas) usamos el comando mv seguido del fichero (o carpeta) de origen, un espacio y la ruta del fichero (o carpeta) de destino:
mv fichero-de-origen.html carpeta-de-destino/fichero-de-destino.html

Este comando también sirve para renombrar, ya que renombrar un fichero de a.html a b.html es lo mismo que moverlo: mv a.html b.html


clear
A veces pasa que hemos introducido muchos comandos y sería genial poder limpiar la ventana. Para eso existe el comando clear.


pwd (print working directory)
Principalmente usaremos la terminal para movernos por el sistema de archivos y carpetas del ordenador. Así que es fundamental saber dónde estamos en cada momento. 
El comando pwd se encargará de mostrarnos en qué carpeta nos encontramos. Si escribimos: pwd 
La terminal mostrará la ruta absoluta de la carpeta en la que estemos, con este aspecto: /user/nombre-de-usuario
Nos estaría indicando que nos encontramos en la carpeta nombre-de-usuario, que está dentro de la carpeta user, que está en la carpeta raíz de nuestro equipo.

Si estás trabajando en un Ubuntu integrado dentro de Windows 10 y pruebas pwd verás que el resultado es: /mnt/c/Users/nombre-de-usuario
Es decir, en Windows 10 las unidades de nuestro ordenador como c:\ se montan dentro de /mnt/, por ello la ruta c:\Users\maricarmen corresponde con /mnt/c/Users/maricarmen.


Historial de comandos
Para movernos por los últimos comandos ejecutados usamos la teclas de flecha para arriba ⬆️ y para abajo ⬇️. Así nos ahorramos volver a escribir lo mismo muchas veces.


Ayuda y opciones
Si no sabemos cómo funciona un comando podemos buscar en Internet (siempre muy útil) o pediremos ayuda a la terminal. Por ejemplo para saber cómo funciona el comando ls escribimos la opción --help:
ls --help (Enseña solo una brief description, para un help completo usar man ls (man for manual) y luego darle q para quit, salir del manual)
El terminal mostrará una explicación de cómo se utiliza el comando y las opciones. Con esta información sabremos que para listar todos los ficheros de un directorio, incluidos los ocultos usaremos:
ls -a
Es decir, las letras que pongamos después del guion - son las opciones. Y podemos poner una o varias. Y todos los comandos tienen la opción de ayuda en --help.


A practicar
Durante los primeros días del curso te explicaremos en detalle cómo se usa la terminal y sus comandos. Pero es interesante que empieces a familiarizarte un poco, así que te recomendamos que hagas el siguiente ejercicio:

Crea una carpeta en tu ordenador como lo has hecho siempre:
Botón derecho
Crear carpeta
...
Abre la carpeta desde VS Code.
Abre una terminal y desde ahí practica algunos comandos como...
Crea una subcarpeta.
Entra en la subcarpeta.
Sube desde la subcarpeta a la carpeta superior.
Lista el contenido de la carpeta.
Trastea y prueba cosas...
'''
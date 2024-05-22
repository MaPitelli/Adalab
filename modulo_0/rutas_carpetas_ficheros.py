'''
Rutas de las carpetas y ficheros

Los proyectos de analítica de datos pueden estar compuestos de muchas carpetas y ficheros (imágenes, tablas de resultados, módulos con funciones, etc.) que están relacionados entre sí. 
O dicho de otra forma unos ficheros usan otros ficheros.

Un ejemplo sería la carpeta de imágenes, para introducirlas en un informe. Imaginemos que deseamos guardar un histograma. 
Para esto nosotras escribiríamos código de Python y al realizar el guardado de la imagen(también llamado exportar) lo realizaríamos dentro de su carpeta correspondiente. 
Dentro del código para guardar la imagen escribiríamos la ruta ./output/images/histogram.jpg.

La definición de ruta es el camino que hay que recorrer para ir desde una carpeta o fichero de origen a un carpeta o fichero de destino, para relacionarlos entre sí.

También vamos a utilizar rutas cuando trabajemos con la terminal, para movernos de la carpeta en la que estamos trabajando en un momento dado a otra carpeta en la que queremos empezar a trabajar.

Hay rutas absolutas y rutas relativas.


Rutas absolutas

Las rutas absolutas indican la dirección completa de una carpeta o fichero desde la raíz del ordenador. 
Es decir el origen de la ruta es la carpeta principal del ordenador. El destino es el fichero que queremos enlazar:

Siempre empiezan con /. La / es la ruta raíz del ordenador.

Por ejemplo /user/maricarmen/adalab/proyectos/modulo-1/.

Por ejemplo /user/maricarmen/adalab/proyectos/modulo-1/python/

Por ejemplo /mnt/c/Users/maricarmen/adalab/proyectos/modulo-1/ python/leccion1.ipynb


Rutas relativas

Las rutas relativas indican el camino que hay que recorrer para ir desde la carpeta actual en la que estoy ahora mismo a otra carpeta o fichero. 
Cuando decimos "la carpeta actual en la que estoy" nos referimos a la carpeta en la que está nuestra terminal, o a la carpeta en la que está el fichero que estamos editando.

La ruta relativa más simple es ../ (dos puntos barra). Esta ruta indica la carpeta madre o carpeta superior respecto a la carpeta actual. 
Si la ruta relativa es el camino a recorrer, escribiendo la ruta ../ vamos de la carpeta actual a la carpeta madre. 
Si escribimos la ruta ../../ vamos de la carpeta actual a la carpeta abuela. Y así sucesivamente...

Otra ruta relativa muy simple es ./ (punto barra). Esta ruta indica la carpeta en la que estoy, mi carpeta actual. 
Si la ruta relativa es el camino a recorrer, escribiendo la ruta ./ vamos de la carpeta actual a la carpeta actual. 
Esto parece que no tiene mucho sentido, en seguida veremos que sí lo tiene.

Vamos a ver un ejemplo de rutas relativas. Teniendo esta estructura de carpetas y ficheros:

adalab/
├ proyectos/
├─┬ modulo-1/
│ └┬─ python/
│  │  └─ leccion1.ipynb
│  │  └─ ejercicios-py-l1.ipynb
│  ├─ sql/
│  │  └─ ejercicios-sql-l1.ipynb
│  └─ index.html
└─ modulo-2/

Pensemos que estoy en la carpeta proyectos/ y quiero caminar hasta la carpeta modulo-1/. 
La ruta a usar es ./modulo-1/. Es decir, desde proyectos/ que es la actual, entro en modulo-1/.

Ahora pensemos que estoy en la carpeta proyectos/ y quiero caminar hasta la carpeta python/. 
La ruta a usar es ./modulo-1/python/. Es decir, desde proyectos/ entro en modulo-1/. Después desde modulo-1/ entro en python/.

Ahora pensemos que estoy en la carpeta sql/ y quiero entrar en la carpeta python/. 
La ruta a usar es ../python/. Primero subo a la carpeta madre que es modulo-1/ pero no necesito indicar el nombre de la carpeta madre porque madre no hay más que una y me vale con poner ../. 
Después desde la carpeta madre entro en la carpeta python/.


Rutas dentro de ficheros

Cuando nos movemos por la terminal podemos usar rutas absolutas o relativas. 
Pero cuando escribimos la ruta desde dentro de un fichero a otro fichero debemos usar siempre rutas relativas. 
Esto se debe a que cuando estamos programando una página, los ficheros están en mi ordenador. 
Pero si los comparto con una compañera, ella los colocará donde quiera, y su ruta absoluta será diferente a la mía.

BRICONSEJO: Acuérdate de este importante consejo. Cuando pongas la ruta de un fichero dentro de otro, la ruta debe empezar con ./ o ../. Siempre. Sin excepciones. 
Si alguna vez no lo haces, antes o después tendrás problemas y acabarás acordándote de este briconsejo.

'''
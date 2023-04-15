# Parte 1

Buenas, lo ideal para todo esto es hacerlo en ubuntu, aqui como se puede ver estan subidos los archivos de dockerfile de servidor y cliente los cuales estan en dos carpetas distintas, al descargar y despues de descomprimir el archivo hay que entrar por 2 terminales distintos, de los cuales cada uno vaya a un directorio distinto osea Server y otro al Cliente, cabe recalcar que hay que tener docker instalado para este procedimiento.
Ya con lo anterior dicho ahora hay que ir al terminal del Cliente y hacer el buildeo de este con el siguiente comando:

`sudo docker build -t (nombre) .`

En este caso el nombre puedes ponerle cliente simplemente.

Ahora con la parte del servidor es lo mismo:

`sudo docker build -t (nombre) .`

Despues de completar este proceso procedemos a iniciar estos contenedores y hacer la conexion cliente servidos para ello comenzamos con el servidor.

`sudo docker run -it -p 6667:6667 (nombre imagen) bash`

y casi lo mismo para el cliente:

`sudo docker run -it (nombre imagen) bash`

y ya runeando esto en el servidor debes ver la ip que se genero con:

`hostname -I`

y tambien activas el servidor con:

`miniircd`

Por ultimo creas el server en el cliente con la ip y puerto a utilizar:

```/server add (nombre servidor) (ip)/(puerto)```

y te conectas:

`/connect (nombre servidor)`

aca ya puedes interactuar y crear salas de chat con join o desconectarte con disconnect.

##Video de Parte 1
[![Watch the video](https://i9.ytimg.com/vi/3cxRaPQ2Wj8/mq2.jpg?sqp=CNyHmpUG&rs=AOn4CLAuw1s6kPby-vElu4mbHobxs4LnfQ)](https://youtu.be/3cxRaPQ2Wj8)

#Parte 2

En primer lugar el buildeo de el polymorph el cual se hace con la siguiente linea:`

```sudo docker build -t (nombre) .```

Y ahora se procede a hacer el runeo de este:

```sudo docker run -it --privileged (nombre imagen)```

Ya estando en el contenedor para abrir el polymorph se necesita poner el nombre de este, ya teniendo abierto el polymorph hay que hacer un spoof y despues proceder a capturar los paquetes que vamos a modificar con el filtro del protocolo irc, normalmente en esta area se les dice template a cada paquete:

```spoof -t (ip cliente) -g (ip server)```

```capture -f irc```

Por consiguiente hay que buscar un template el cual sera el tipo a modificar, entonces se procede a hacer la funcion en nano con el siguiente comando:

```functions -a (nombre funcion) -e nano```

Finalmente se interceptan los datos para la modificacion de estos con la funcion puesta:

```intercept```

##Video de Parte 2
[![Watch the video](https://i9.ytimg.com/vi/4odwaBsF224/mq2.jpg?sqp=CIiKmpUG&rs=AOn4CLBFmN0bMqIKkKazObApJWb_QVxkVQ)](https://youtu.be/4odwaBsF224)

##Video de Parte 3
[![Watch the video](https://i9.ytimg.com/vi/4odwaBsF224/mq2.jpg?sqp=CIiKmpUG&rs=AOn4CLBFmN0bMqIKkKazObApJWb_QVxkVQ)](https://youtu.be/A3cpDhkupqI)

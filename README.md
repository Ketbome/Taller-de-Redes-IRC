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

`/server add (nombre servidor) (ip)/(puerto)`

y te conectas:

`/connect (nombre servidor)`

aca ya puedes interactuar y crear salas de chat con join o desconectarte con disconnect.

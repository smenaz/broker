## Aplicación que maneja un Broker con Redis:

Utiliza tres colas de mensajes (broker):
* control
* control_respuesta
* comandos

## Para ejecutar y construir el contenedor debe estar instalado Docker y docker-compose

## Se debe ejecutar el siguiente comando para construir y ejecutar el contenedor dentro de la carpeta del proyecto en la raíz:
``` docker-compose up -d --build ```

## Para verificar que el contenedor se encuentra ejeuctandose y ver los logs se puede ejecutar dentro de la carpeta del proyecto en la raíz:
``` docker-compose logs -f -t ```




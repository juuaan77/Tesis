#!/bin/bash

#Este script crea una VM con los parametros pasados y la coloca con booteo por pxe.
if [ $# -lt 5 ]; 
then
	echo "Necesitas pasar cuatro parámetros, que significan:";
	echo "1° -> IP del servidor Cobbler";
	echo "2° -> Nombre para el sistema";
	echo "3° -> Perfil para el sistema";
	echo "4° -> Hostname para las maquinas del sistema";
	echo "5° -> MAC deseada para el servidor creado";
	echo "6° -> IP Deseada para la VM";
	echo "7° -> Comentario para el sistema";
	exit;
else
	ssh root@$1 'cobbler system add  --name='$2' --profile='$3' --hostname='$4' --mac-address='$5' --ip-address='$6' --comment='$7' --gateway=192.168.122.1 --static --name-servers=8.8.8.8 8.8.4.4 --interface=eth0'

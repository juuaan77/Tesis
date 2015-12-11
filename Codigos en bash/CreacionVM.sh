#!/bin/bash

#Este script crea una VM con los parametros pasados y la coloca con booteo por pxe.
if [ $# -lt 6 ]; 
then
	echo "Necesitas pasar cuatro parámetros, que significan:";
	echo "1° -> nombre de la VM";
	echo "2° -> RAM de la  VM en MB";
	echo "3° -> Nombre de la imagen de la VM";
	echo "4° -> Tamaño del disco asignado en GB";
	echo "5° -> Direccion IP del servidor Cobbler";
	echo "6° -> Direccion IP del servidor creado";
	exit;
else
	#Ejecuto un script que accede al servidor cobbler y modifica el snippet de configuracion de red para que use la IP deseada
	echo 'ssh root@$5 sed -i 's/IPADDR.*/IPADDR=$6/g' /var/lib/cobbler/snippets/Configura;'

	#Se crea una maquina virtual con los parametros deseados.
	virt-install  --connect qemu:///system --virt-type kvm --name $1 --ram $2 --disk path=/var/lib/libvirt/images/$3.qcow2,size=$4 --network network=default --graphics vnc --boot network=on --os-type linux --os-variant rhel6;

fi

#virt-install  --connect qemu:///system --virt-type kvm --name bashi --ram 1024 --disk path=/var/lib/libvirt/images/demo.img,size=8 --network network=default --graphics vnc --boot network=on --os-type linux --os-variant rhel6;

exit;		

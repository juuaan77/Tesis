#!/bin/bash

#Este script crea una VM con los parametros pasados y la coloca con booteo por pxe.
if [ $# -lt 5 ]; 
then
	echo "Necesitas pasar cuatro parámetros, que significan:";
	echo "1° -> nombre de la VM";
	echo "2° -> RAM de la  VM en MB";
	echo "3° -> Nombre de la imagen de la VM";
	echo "4° -> Tamaño del disco asignado en GB";
	echo "5° -> MAC deseada para el servidor creado";
	exit;
else
	#Se crea una maquina virtual con los parametros deseados.
	virt-install  --connect qemu:///system --virt-type kvm --name $1 --ram $2 --disk path=/var/lib/libvirt/images/$3.qcow2,size=$4 --network default,mac=$5 --pxe --os-type linux --os-variant rhel6 --noautoconsole&

fi

#virt-install --connect qemu:///system --virt-type kvm --name bashi --ram 1024 --disk path=/var/lib/libvirt/images/demo.img,size=8 --network default,mac=12:34:56:78:90:ab --pxe --os-type linux --os-variant rhel6 --noautoconsole
exit;		

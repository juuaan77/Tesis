#!/bin/bash

#Verifico que se me haya entregado la direccion IP como parametro
if [ $# -lt 1 ]; 
then
	echo "Necesito como parametro la direccion IP de servidor.";
	exit;
else
	#Añado el repositorio EPEL
	wget http://epel.mirror.net.in/epel/6/i386/epel-release-6-8.noarch.rpm
	rpm -Uvh epel-release-6-8.noarch.rpm
	
	#Actualizo los repositorios
	yum update -y;
	
	#Desactivo el selinux. La segunda linea, es porque a veces no lo deshabilita con la 1°.
	sed -i 's/SELINUX=.*/SELINUX=disabled/g' /etc/sysconfig/selinux;
	sed -i 's/SELINUX=.*/SELINUX=disabled/g' /etc/selinux/config;

	#Desactivo el firewall
	service iptables stop;
	chkconfig iptables off;

	#Instalo los servicios necesarios
	yum install cobbler cobbler-web dhcp debmirror pykickstart system-config-kickstart dhcp mod_python tftp cman -y;

	#Activo el ftp
	sed -i 's/disable.*/disable=no/g' /etc/xinetd.d/tftp;
	#igual para el rsync
	sed -i 's/disable.*/disable=no/g' /etc/xinetd.d/rsync;

	#Me coloco en el direcotio /root/configfiles
	mkdir /root/archivos;
	cd /root/archivos;
	#Descargo todos los archivos de configuracion necesarios.
	wget https://raw.githubusercontent.com/juuaan77/Tesis/master/ArchivosConfCobbler/debmirror.conf
	wget https://raw.githubusercontent.com/juuaan77/Tesis/master/ArchivosConfCobbler/dhcp.template
	wget https://raw.githubusercontent.com/juuaan77/Tesis/master/ArchivosConfCobbler/dhcpd.conf
	wget https://raw.githubusercontent.com/juuaan77/Tesis/master/ArchivosConfCobbler/modules.conf
	wget https://raw.githubusercontent.com/juuaan77/Tesis/master/ArchivosConfCobbler/settings

	#copio el archivo ya configurado en su posicion adecuada.
	cat dhcpd.conf > /etc/dhcp/dhcpd.conf;
	
	#debo arreglar el problema del httpd añadiendo la siguiente linea.
	echo "ServerName localhost" >> 	/etc/httpd/conf/httpd.conf
	
	#Reinicio y activo los servicios
	service httpd start
	service dhcpd start
	service xinetd start
	service cobblerd start
	chkconfig httpd on
	chkconfig dhcpd on
	chkconfig xinetd on
	chkconfig cobblerd on
	
	#Utilizo el parametro para colocar la IP correcta en el archivo settings y guardarlo en su correspondite lugar.
	sed 's/next_server:@IP@/next_server:'$1'/' settings > /etc/cobbler/settings;
	sed 's/server:@IP@/server:'$1'/' settings > /etc/cobbler/settings;

	#Hago lo propio con el dhcp.template
	cat dhcp.template > /etc/cobbler/dhcp.template
	
	#Es el turno de /etc/cobbler/modules.conf
	cat modules.conf > /etc/cobbler/modules.conf

	#En este punto, debo reiniciar para continuar,entonces descargo el script PostReinicio.sh, lo hubico en /root y edito el archivo /etc/rc.local

	cd /root
	wget https://raw.githubusercontent.com/juuaan77/Tesis/master/Codigos%20en%20bash/PostReinicio.sh
	chmod +x PostReinicio.sh;
	#echo "/root/PostReinicio.sh" >> /etc/rc.local

	#reboot;
	
fi
exit;


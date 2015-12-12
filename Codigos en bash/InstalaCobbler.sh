#!/bin/bash

#Verifico que se me haya entregado la direccion IP como parametro
if [ $# -lt 1 ]; 
then
	echo "Necesito como parametro la direccion IP de servidor.";
	exit;
else

	#Desactivo el selinux
	sed -i 's/SELINUX=.*/SELINUX=disabled/g' /etc/sysconfig/selinux;

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
	mkdir /root/configfiles;
	cd /root/configfiles;
	#Descargo todos los archivos de configuracion necesarios.
	wget https://github.com/juuaan77/Tesis/blob/master/Archivos%20de%20configuracion%20de%20cobbler/dhcpd.conf;
	wget https://github.com/juuaan77/Tesis/blob/master/Archivos%20de%20configuracion%20de%20cobbler/dhcp.template;
	wget https://github.com/juuaan77/Tesis/blob/master/Archivos%20de%20configuracion%20de%20cobbler/debmirror.conf;
	wget https://github.com/juuaan77/Tesis/blob/master/Archivos%20de%20configuracion%20de%20cobbler/modules.conf;
	wget https://github.com/juuaan77/Tesis/blob/master/Archivos%20de%20configuracion%20de%20cobbler/settings;

	#copio el archivo ya configurado en su posicion adecuada.
	cp dhcpd.conf /etc/dhcp/dhcpd.conf;

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
	rm -r /etc/cobbler/dhcp.template
	cp dhcp.template /etc/cobbler/dhcp.template
	
	#Es el turno de /etc/cobbler/modules.conf
	rm -r /etc/cobbler/modules.conf
	cp modules.conf /etc/cobbler/modules.conf



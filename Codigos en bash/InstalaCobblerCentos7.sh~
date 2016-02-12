#!/bin/bash

#Verifico que se me haya entregado la direccion IP como parametro
if [ $# -lt 1 ]; 
then
	echo "Necesito como parametro la direccion IP de servidor.";
	exit;
else

	#Instalo paquetes base, que a veces no estan instalados por defecto
	yum install wget vim -y
	
	#Añado el repositorio EPEL
	wget http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-5.noarch.rpm
	rpm -ivh epel-release-7-5.noarch.rpm
	#Añado repositorio para puppet
	#rpm -ivh https://yum.puppetlabs.com/puppetlabs-release-el-7.noarch.rpm
	#yum install puppetserver -y
	#Para actualizarlo a la ultima version de puppet
	#puppet resource package puppet-server ensure=latest
	#Actualizo los repositorios
	yum update -y;
	
	#Desactivo el selinux. La segunda linea, es porque a veces no lo deshabilita con la 1°.
	sed -i 's/SELINUX=.*/SELINUX=disabled/g' /etc/sysconfig/selinux;
	sed -i 's/SELINUX=.*/SELINUX=disabled/g' /etc/selinux/config;

	#Desactivo el firewall
	systemctl stop firewalld
	systemctl disable firewalld

	#Instalo los servicios necesarios
	yum install cobbler cobbler-web dhcp pykickstart system-config-kickstart dhcp tftp httpd xinetd -y;

	#Activo el ftp
	sed -i 's/disable.*/disable=no/g' /etc/xinetd.d/tftp;
	
	#Este archivo fue eliminado en cobbler 7, ahora, hay un servicio en systemctl BUSCAR COMO ERA	
	#igual para el rsync
	#sed -i 's/disable.*/disable=no/g' /etc/xinetd.d/rsync;
	systemctl start rsyncd
	systemctl enable rsyncd 

	#Me coloco en el direcotio /root/configfiles
	mkdir /root/archivos;
	cd /root/archivos;
	
	#Descargo todos los archivos de configuracion necesarios.
	wget https://raw.githubusercontent.com/juuaan77/Tesis/master/ArchivosConfCobblerC7/dhcp.template
	wget https://raw.githubusercontent.com/juuaan77/Tesis/master/ArchivosConfCobblerC7/dhcpd.conf
	wget https://raw.githubusercontent.com/juuaan77/Tesis/master/ArchivosConfCobblerC7/settings
	
	#copio el archivo ya configurado en su posicion adecuada.
	cat dhcpd.conf > /etc/dhcp/dhcpd.conf;
	
	#debo arreglar el problema del httpd añadiendo la siguiente linea.
	echo "ServerName localhost" >> 	/etc/httpd/conf/httpd.conf
	
	#Reinicio y activo los servicios
	systemctl start httpd
	systemctl start dhcpd
	systemctl start xinetd
	systemctl start cobblerd
	systemctl enable httpd
	systemctl enable dhcpd
	systemctl enable xinetd
	systemctl enable cobblerd

	
	#Utilizo el parametro para colocar la IP correcta en el archivo settings y guardarlo en su correspondite lugar.
	sed 's/next_server:@IP@/next_server: '$1'/' settings > /etc/cobbler/settings;
	sed 's/server:@IP@/server: '$1'/' settings > /etc/cobbler/settings;

	#Hago lo propio con el dhcp.template
	cat dhcp.template > /etc/cobbler/dhcp.template
	

	#En este punto, debo reiniciar para continuar,entonces descargo el script PostReinicio.sh, lo hubico en /root y edito el archivo /etc/rc.local

	#cd /root
	#wget https://raw.githubusercontent.com/juuaan77/Tesis/master/Codigos%20en%20bash/PostReinicio.sh
	#chmod +x PostReinicio.sh;
	#echo "/root/PostReinicio.sh" >> /etc/rc.local

	reboot;
	
fi
exit;


#!/bin/bash

#Script que instala y configura automaticamente un repositorio local.

if [ $# -lt 2 ]; 
then
	echo "Necesitas pasar dos parámetros, que significan:";
	echo "1° -> Distribucion para la que se creara el repositorio (ubuntu o centos)";
	echo "2° -> Nombre seleccionado para el repositorio";
	exit;
else

	yum install -y createrepo vsftpd lftp

	mkdir /var/ftp/pub/$1
	mkdir /var/ftp/pub/$1/$2

	#en este punto, se crean las bases de datos del repositorio, pero se encuentra vacio el mismo.
	createrepo -v /var/ftp/pub/$1/$2

	echo "anon_root=/var/ftp/pub" >> /etc/vsftpd/vsftpd.conf

	systemctl start vsftpd
	systemctl enable vsftpd

fi

exit;

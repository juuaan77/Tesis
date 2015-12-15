#!/bin/bash


#Reinicio y activo los servicios
service httpd start
service dhcpd start
service xinetd start
service cobblerd start

#Obtengo los cargadores de red
cobbler get-loaders;

#me muevo a la carpeta adecuada
cd /root/archivos;
#Coloco el ultimo archivo
rm -r /etc/debmirror.conf
cp debmirror.conf /etc/debmirror.conf

#reinicio los servicios nuevamente
service httpd restart
service dhcpd restart
service xinetd restart
service cobblerd restart

exit;

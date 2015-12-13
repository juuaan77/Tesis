#!/bin/bash

#Obtengo los cargadores de red
cobbler get-loaders;

#Coloco el ultimo archivo
rm -r /etc/debmirror.conf
cp debmirror.conf /etc/debmirror.conf

#reinicio los servicios nuevamente
service httpd restart
service dhcpd restart
service xinetd restart
service cobblerd restart

exit;

#!bin/bash

#Actualzo los repositorios
yum update -y

#Deshabilita el selinux.
sed -i 's/SELINUX=.*/SELINUX=disabled/g' /etc/sysconfig/selinux;

#Deshabilt el firewall
service iptables stop
chkconfig iptables off

#Instalo los paqueres necesarios
yum install cobbler cobbler-web dhcp debmirror pykickstart system-config-kickstart dhcp mod_python tftp cman -y

#Habilito el ftp y el rsync
sed -i 's/disable.*/  disable=no/g' /etc/xinetd.d/tftp;
sed -i 's/disable.*/  disable=no/g' /etc/xinetd.d/rsync;

#Configuro el DHCP
cp /usr/share/doc/dhcp-4.1.1/dhcpd.conf.sample /etc/dhcp/dhcpd.conf


exit;

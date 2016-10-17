#!/bin/bash

#Script que instala y configura automaticamente un repositorio local.

yum install -y createrepo vsftpd lftp

mkdir /var/ftp/pub/proyectointegrador/
mkdir /var/ftp/pub/proyectointegrador/Centos7

#en este punto, se crean las bases de datos del repositorio, pero se encuentra vacio el mismo.
createrepo -v /var/ftp/pub/proyectointegrador/Centos7

echo "anon_root=/var/ftp/pub" >> /etc/vsftpd/vsftpd.conf

systemctl start vsftpd
systemctl enable vsftpd

exit;

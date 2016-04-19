#!/bin/bash
yum install -y wget vim

wget http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-6.noarch.rpm
rpm -ivh epel-release-7-6.noarch.rpm

rpm -Uvh http://li.nux.ro/download/nux/dextop/el7/x86_64/nux-dextop-release-0-5.el7.nux.noarch.rpm

rpm --import https://www.elrepo.org/RPM-GPG-KEY-elrepo.org
rpm -Uvh http://www.elrepo.org/elrepo-release-7.0-2.el7.elrepo.noarch.rpm
yum --disablerepo \* --enablerepo elrepo-kernel install -y kernel-ml

yum install -y epel-release
yum install -y ntfs-3g os-prober
grub2-mkconfig -o /boot/grub2/grub.cfg

touch Templates/NewDocument

exit

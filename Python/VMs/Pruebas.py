#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'juan'
import commands,re,fnmatch
from EstadoVM import genera_estado_html,estado

maquinas = estado()

salida = commands.getstatusoutput("cat /etc/hosts")
salida = re.split("\n", salida[1])
salida.pop(0)
salida.pop(0)
dominio=[]
for i in range(0, len(salida), 1):
    dominio =dominio + re.split(" ", salida[i])
#print dominio

#print maquinas
for i in range(1, len(dominio), 2):
    if not (dominio[i] in maquinas):
        print "no esta!\n"
        commands.getstatusoutput("echo \"`sed '/" + dominio[i] +"$/d' /etc/hosts`\" > /etc/hosts")
        print "echo \"`sed '/" + dominio[i] +"$/d' /etc/hosts`\" > /etc/hosts"


#for i in range(0, len(maquinas), 1):

#echo "`sed '/generic$/d' /etc/hosts`" > /etc/hosts
#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'juan'

import commands
import random
import time
import sys

def CreaVm (numbers_VMs,perfil):

    '''Crea la cantidad de maquinas virtuales indicadas en el parametro numbers_VMs

        numbers_Vms -> entero, Cantidad de maquinas virtuales a crear
        perfil -> indico de que tipo de perfil deseo que sea la maquina

        return: none'''
    try:
        for i in range(int(numbers_VMs)):
            #Si el perfil es alumno, la maqiuna se llamara alumno y un numero aleatorio, lo mismo para docentes y GUI

            #Debo generar un nombre aleatorio para las VM
            name = perfil + str(random.randrange(0,10000))
            #Debo generar una mac aleatoria.
            hexadecimal=[1,2,3,4,5,6,7,8,9,"a","b","c","d","e","f"]
            mac = "52:54:00:" + str(random.choice(hexadecimal)) + str(random.choice(hexadecimal))
            mac = mac + ":" + str(random.choice(hexadecimal)) + str(random.choice(hexadecimal))
            mac = mac + ":" + str(random.choice(hexadecimal)) + str(random.choice(hexadecimal))

            if perfil == "windows":
                os = "win7"
                ostype = "windows"
                disco = 25
            elif perfil == "ubuntugui":
                os = "generic"
                ostype = "linux"
                disco = 15
            else:
                os = "rhel7"
                ostype = "linux"
                disco = 15

            #Ejecuto la linea que crea la VM
            print "cobbler system add --name=" + str(name) + " --profile=" + str(perfil) + " --hostname=" + str(name) + " --mac-address=" + str(mac) + " --gateway=192.168.122.1  --static --name-servers=8.8.8.8 8.8.4.4 --interface=eth0"
            commands.getoutput("cobbler system add --name=" + str(name) + " --profile=" + str(perfil) + " --hostname=" + str(name) + " --mac-address=" + str(mac) + " --gateway=192.168.122.1  --static --name-servers=8.8.8.8 8.8.4.4 --interface=eth0")
            print "virt-install --connect qemu:///system --virt-type kvm --name " + str(name) + " --ram 1024 --disk path=/var/lib/libvirt/images/" + str(name) + ".qcow2,size=" + str(disco) + " --network network=Cobbler,mac=" + str(mac) + " --pxe --os-type " + str(ostype) +" --os-variant "+ str(os)
            commands.getoutput("virt-install --connect qemu:///system --virt-type kvm --name " + str(name) + " --ram 1024 --disk path=/var/lib/libvirt/images/" + str(name) + ".qcow2,size=" + str(disco) + " --network network=Cobbler,mac=" + str(mac) + " --pxe --os-type " + str(ostype) +" --os-variant "+ str(os))

            #Le doy tiempo (30 segundos) para que se refrezque el archivo dhcpd.lease
            time.sleep(60)

            #Una vez Creada por completo la VM llamo a la funcion parseo_IP para obtener su IPy guardarla en el /etc/hosts
            print "voy a llamar con #" + str(mac) + "# y #" + str(name) + "# \n"
            Parseo_IP(mac,name)

            commands.getoutput("cobbler system remove --name=" + str(name))
            #print "cobbler system add --name=" + str(name) + " --profile=" + str(perfil) + " --hostname=" + str(name) + " --mac-address=" + str(mac) + " --gateway=192.168.122.1  --static --name-servers=8.8.8.8 8.8.4.4 --interface=eth0"
            #print "virt-install --connect qemu:///system --virt-type kvm --name " + str(name) + " --ram 1024 --disk path=/var/lib/libvirt/images/" + str(name) + ".qcow2,size=8 --network network=Cobbler,mac=" + str(mac) + " --pxe --os-type linux --os-variant rhel7"
            #print "cobbler system remove --name=" + str(name)+";"
            return "exito"

    except ValueError:
        return "error"


def CreaVm_parametrizada (perfil, ram, disco):

    '''Crea una VM con los parametros indicados

       perfil -> indico de que tipo de perfil deseo que sea la maquina
       ram -> indica la memoria ram de la maquina
       disco -> indica la capacidad en disco duro de la maquina

        return: none'''

    #control de erorers de tipo en los parametros
    try:
        if (int(ram) < 1024):
            ram=1024
    except ValueError:
        return "error"

    try:
        if (int(disco) < 15):
            disco=15
    except ValueError:
        return "error"

    #Debo generar un nombre aleatorio para las VM
    name = perfil + str(random.randrange(0,10000))
    #Debo generar una mac aleatoria.
    hexadecimal=[1,2,3,4,5,6,7,8,9,"a","b","c","d","e","f"]
    mac = "52:54:00:" + str(random.choice(hexadecimal)) + str(random.choice(hexadecimal))
    mac = mac + ":" + str(random.choice(hexadecimal)) + str(random.choice(hexadecimal))
    mac = mac + ":" + str(random.choice(hexadecimal)) + str(random.choice(hexadecimal))

    if perfil == "windows":
        os = "win7"
        ostype = "windows"
        if (int(disco) < 25):
            disco = 25
    elif perfil == "ubuntugui":
        os = "generic"
        ostype = "linux"
        if (int(disco) < 15):
            disco = 15
    else:
        os = "rhel7"
        ostype = "linux"
        if (int(disco) < 15):
            disco = 15

    #Ejecuto la linea que crea la VM
    print "cobbler system add --name=" + str(name) + " --profile=" + str(perfil) + " --hostname=" + str(name) + " --mac-address=" + str(mac) + " --gateway=192.168.122.1  --static --name-servers=8.8.8.8 8.8.4.4 --interface=eth0"
    commands.getoutput("cobbler system add --name=" + str(name) + " --profile=" + str(perfil) + " --hostname=" + str(name) + " --mac-address=" + str(mac) + " --gateway=192.168.122.1  --static --name-servers=8.8.8.8 8.8.4.4 --interface=eth0")
    print "virt-install --connect qemu:///system --virt-type kvm --name " + str(name) + " --ram " + str(ram) + " --disk path=/var/lib/libvirt/images/" + str(name) + ".qcow2,size=" + str(disco) + " --network network=Cobbler,mac=" + str(mac) + " --pxe --os-type " + str(ostype) +" --os-variant "+ str(os)
    commands.getoutput("virt-install --connect qemu:///system --virt-type kvm --name " + str(name) + " --ram " + str(ram) + " --disk path=/var/lib/libvirt/images/" + str(name) + ".qcow2,size=" + str(disco) + " --network network=Cobbler,mac=" + str(mac) + " --pxe --os-type " + str(ostype) +" --os-variant "+ str(os))

    #Le doy tiempo (30 segundos) para que se refrezque el archivo dhcpd.lease
    time.sleep(60)

    #Una vez Creada por completo la VM llamo a la funcion parseo_IP para obtener su IPy guardarla en el /etc/hosts
    print "voy a llamar con #" + str(mac) + "# y #" + str(name) + "# \n"
    Parseo_IP(mac,name)

    commands.getoutput("cobbler system remove --name=" + str(name))
    #print "cobbler system add --name=" + str(name) + " --profile=" + str(perfil) + " --hostname=" + str(name) + " --mac-address=" + str(mac) + " --gateway=192.168.122.1  --static --name-servers=8.8.8.8 8.8.4.4 --interface=eth0"
    #print "virt-install --connect qemu:///system --virt-type kvm --name " + str(name) + " --ram 1024 --disk path=/var/lib/libvirt/images/" + str(name) + ".qcow2,size=8 --network network=Cobbler,mac=" + str(mac) + " --pxe --os-type linux --os-variant rhel7"
    #print "cobbler system remove --name=" + str(name)+";"
    return "exito"


def Parseo_IP(mac,hostname):
    '''Obtiene una IP dada de un archivo dhcpd.leases en base a la mac y el hostname de la maquina

        mac -> es la direcion fisica de la maquina.
        hsotname -> es elnombre de la maquina.

        return: none'''
    lista = commands.getoutput("cat /var/lib/dhcpd/dhcpd.leases")
    parseado = lista.split("lease ")
    print mac +"\n"
    print hostname +"\n"
    i = 0
    while i < int(len(parseado)):
        if mac in parseado[i] and hostname in parseado[i]:
            ip = parseado[i].split(" ")
            break
        else:
            ip = "naranja fanta"
        i = i+1
    print "me llamo\n"
    commands.getoutput("echo '" + str(ip[0]) + " " + str(hostname) +"' >>  /etc/hosts" )
    print "echo '" + str(ip[0]) + " " + str(hostname) +"' >>  /etc/hosts"

#if __name__ == '__main__':

    #print  "Ingrese la cantidad de maquinas alumnos, docentes, GUI que desea instalar"
    #nalumnos = int(input("¿Cuantas VM alumno desea crear?:"))
    #nGUI = int(input("¿Cuantas VM GUI desea crear?:"))
    #nubuntu = int(input("¿Cuantas VM ubuntu desea crear?:"))
    #nwindows = int(input("¿Cuantas VM windows desea crear?:"))
    #CreaVm(nalumnos,"alumno")
    #CreaVm(nGUI,"gui")
    #CreaVm(nubuntu,"ubuntugui")
    #CreaVm(nwindows,"windows")

    #CreaVm_parametrizada ("ubuntugui",1024, 20)


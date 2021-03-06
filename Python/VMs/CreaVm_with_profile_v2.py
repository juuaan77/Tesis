#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'juan'

import commands
import random
import time
import sys
import threading
mutex = threading.Lock()

def CreaVm (numbers_VMs,perfil):

    '''Crea la cantidad de maquinas virtuales indicadas en el parametro numbers_VMs

        numbers_Vms -> entero, Cantidad de maquinas virtuales a crear
        perfil -> indico de que tipo de perfil deseo que sea la maquina

        return: exito en caso de finalizar satisfactoriamente el bucle
                error en caso de presentarse algun error de valor.'''
    try:
        for i in range(int(numbers_VMs)):
            #Debo generar un nombre aleatorio para las VM
            name = perfil + str(random.randrange(0,10000))
            #Debo generar una mac aleatoria.
            hexadecimal=[1,2,3,4,5,6,7,8,9,"a","b","c","d","e","f"]
            mac = "52:54:00:" + str(random.choice(hexadecimal)) + str(random.choice(hexadecimal))
            mac = mac + ":" + str(random.choice(hexadecimal)) + str(random.choice(hexadecimal))
            mac = mac + ":" + str(random.choice(hexadecimal)) + str(random.choice(hexadecimal))

            #Segun el SO operativo hosteado, la maquina virtual debe cumplir con caracteristicas minimas, que si las dadas no son suficinetes,
            #se descartan y se utilizan las minimas.
            if perfil == "windows":
                os = "win7"
                ostype = "windows"
                disco = 25
                ram = 2048
                commands.getoutput("sed -i  '/ComputerName/c\            <ComputerName>"+str(name)+"<\/ComputerName>/' /windows/Autounattend.xml")
                commands.getoutput("sed -i 's/\r$//g' Autounattend.xml")
            elif perfil == "ubuntugui":
                os = "generic"
                ostype = "linux"
                disco = 15
                ram = 1024
            else:
                os = "rhel7"
                ostype = "linux"
                disco = 15
                ram = 1024

            #Ejecuto la linea que crea la VM
            print "cobbler system add --name=" + str(name) + " --profile=" + str(perfil) + " --hostname=" + str(name) + " --mac-address=" + str(mac) + " --gateway=192.168.122.1  --static --name-servers=8.8.8.8 8.8.4.4 --interface=eth0"
            commands.getoutput("cobbler system add --name=" + str(name) + " --profile=" + str(perfil) + " --hostname=" + str(name) + " --mac-address=" + str(mac) + " --gateway=192.168.122.1  --static --name-servers=8.8.8.8 8.8.4.4 --interface=eth0")
            print "virt-install --connect qemu:///system --virt-type kvm --name " + str(name) + " --ram "+ str(ram) +" --disk path=/var/lib/libvirt/images/" + str(name) + ".qcow2,size=" + str(disco) + " --network network=puppet,mac=" + str(mac) + " --pxe --os-type " + str(ostype) +" --os-variant "+ str(os)
            commands.getoutput("virt-install --connect qemu:///system --virt-type kvm --name " + str(name) + " --ram "+ str(ram) +" --disk path=/var/lib/libvirt/images/" + str(name) + ".qcow2,size=" + str(disco) + " --network network=puppet,mac=" + str(mac) + " --pxe --os-type " + str(ostype) +" --os-variant "+ str(os))

            #Le doy tiempo (60 segundos) para que se refrezque el archivo dhcpd.lease
            time.sleep(60)

            #Una vez Creada por completo la VM llamo a la funcion parseo_IP para obtener su IPy guardarla en el /etc/hosts
            print "voy a llamar con #" + str(mac) + "# y #" + str(name) + "# \n"
            Parseo_IP(mac,name)

            commands.getoutput("cobbler system remove --name=" + str(name))
            print "cobbler system remove --name=" + str(name)+";"

    except ValueError:
        return "error"

    return "exito"

def CreaVm_parametrizada (perfil, ram, disco):

    '''Crea una VM con los parametros indicados

       perfil -> indico de que tipo de perfil deseo que sea la maquina
       ram -> indica la memoria ram de la maquina
       disco -> indica la capacidad en disco duro de la maquina

       return: exito en caso de finalizar satisfactoriamente
                error en caso de presentarse algun error de valor.'''

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
        if (int(ram) < 2048):
            ram = 2048
        #si es una maquina de windows debo editar un archivo para que modifique dinamicamente el  hostname
        commands.getoutput("sed -i  '/ComputerName/c\            <ComputerName>"+str(name)+"<\/ComputerName>/' /windows/Autounattend.xml")
        commands.getoutput("sed -i 's/\r$//g' Autounattend.xml")

    elif perfil == "ubuntugui":
        os = "generic"
        ostype = "linux"
    else:
        os = "rhel7"
        ostype = "linux"

    #Ejecuto la linea que crea la VM
    print "cobbler system add --name=" + str(name) + " --profile=" + str(perfil) + " --hostname=" + str(name) + " --mac-address=" + str(mac) + " --gateway=192.168.122.1  --static --name-servers=8.8.8.8 8.8.4.4 --interface=eth0"
    commands.getoutput("cobbler system add --name=" + str(name) + " --profile=" + str(perfil) + " --hostname=" + str(name) + " --mac-address=" + str(mac) + " --gateway=192.168.122.1  --static --name-servers=8.8.8.8 8.8.4.4 --interface=eth0")
    print "virt-install --connect qemu:///system --virt-type kvm --name " + str(name) + " --ram " + str(ram) + " --disk path=/var/lib/libvirt/images/" + str(name) + ".qcow2,size=" + str(disco) + " --network network=puppet,mac=" + str(mac) + " --pxe --os-type " + str(ostype) +" --os-variant "+ str(os)
    commands.getoutput("virt-install --connect qemu:///system --virt-type kvm --name " + str(name) + " --ram " + str(ram) + " --disk path=/var/lib/libvirt/images/" + str(name) + ".qcow2,size=" + str(disco) + " --network network=puppet,mac=" + str(mac) + " --pxe --os-type " + str(ostype) +" --os-variant "+ str(os))

    #Le doy tiempo (60 segundos) para que se refrezque el archivo dhcpd.lease
    time.sleep(60)

    #Una vez Creada por completo la VM llamo a la funcion parseo_IP para obtener su IPy guardarla en el /etc/hosts
    print "voy a llamar con #" + str(mac) + "# y #" + str(name) + "# \n"
    Parseo_IP(mac,name)

    commands.getoutput("cobbler system remove --name=" + str(name))
    print "cobbler system remove --name=" + str(name)+";"
    return "exito"


def Parseo_IP(mac,hostname):
    '''Obtiene una IP dada de un archivo dhcpd.leases en base a la mac y el hostname de la maquina

        mac -> es la direcion fisica de la maquina.
        hsotname -> es elnombre de la maquina.

        return: none'''

    #Obtengo el archivo
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
            ip = " "
        i = i+1
    try:
        mutex.acquire()
        commands.getoutput("echo '" + str(ip[0]) + " " + str(hostname) +"' >>  /etc/hosts" )
        print "echo '" + str(ip[0]) + " " + str(hostname) +"' >>  /etc/hosts"
        mutex.release()
    except IndexError:
        print "no\n"

#if __name__ == '__main__':



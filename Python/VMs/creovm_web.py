#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'juan'

import os, time, commands,re,threading
from CreaVm_with_profile_v2 import CreaVm, CreaVm_parametrizada
from EstadoVM import genera_estado_html,estado
from bottle import get, post, request, run,route


#Pagina que muestra el estado actual (encendido/apagado) de las VMs
@get('/estados')
def estadosVM():
    return genera_estado_html()

#Metodo encargado de ejecutar el encendido o apagado de las VMs
@post('/estados')
def do_estadosVM():
    estados = estado()
    encendido = ""
    apagado = ""
    for i in range(0,len(estados)-1,2):
        if request.forms.get("Prender-"+estados[i])=="on":
            encendido= encendido + "\n" + commands.getoutput("virsh start "+estados[i])
        elif request.forms.get("Apagar-"+estados[i])=="on":
            apagado = apagado + "\n" + commands.getoutput("virsh shutdown "+estados[i])

    return encendido +"\n"+ apagado +"\n"+ estadosVM()

#Pagina que recibe datos sobre la cantidad de VMs de cada perfil que se desean crear
@get('/virtual_machine')
def creaVM():
    peticionhtml = open("/root/tesis/Tesis/Python/HTMLs/virtual_machine.html","r", 0)
    return peticionhtml

#Toma los parametros ingresados e indica si se creo o no la VM con exito.
@post('/virtual_machine')
def do_creaVM():
    #Control de error que indica si se colocaron parametros invalidos.
    try:
        ncentos = int(request.forms.get('ncentos'))
        nubuntu = int(request.forms.get('nubuntu'))
        nwindows = int(request.forms.get('nwindows'))
    except ValueError:
        frace = '''Sólo se admiten valores numéricos. \n'''
        peticionhtml = commands.getoutput("cat /root/tesis/Tesis/Python/HTMLs/virtual_machine.html")
        return frace + peticionhtml

    #CreaVm(ncentos, "centos")
    #CreaVm(nubuntu,"ubuntugui")
    #CreaVm(nwindows,"windows")
    threads = []
    t1 = threading.Thread(target=CreaVm, args=(ncentos,"centos"))
    t2 = threading.Thread(target=CreaVm, args=(nubuntu,"ubuntugui"))
    t3 = threading.Thread(target=CreaVm, args=(nwindows, "windows"))
    threads.append(t1)
    threads.append(t2)
    threads.append(t3)
    t1.start()
    time.sleep(5)
    t2.start()
    time.sleep(5)
    t3.start()

    return estadosVM()

#Pagina que recibe los parametros para crear una VM con disco y memoria a eleccion
@get('/virtual_machine_parametrizada')
def creaVM_parametrizado():
    peticionhtml = open("/root/tesis/Tesis/Python/HTMLs/virtual_machine_parametrizada.html","r", 0)
    return peticionhtml

#Toma los parametros ingresados para crear la VMs parametrizada
@post('/virtual_machine_parametrizada')
def do_creaVM_parametrizado():
    perfil = request.forms.get('boton1')
    ram = request.forms.get('ram')
    disco = request.forms.get('disco')
    #reviso que los parametros sean adecuados
    if str(perfil)=="None":
        return '''Seleccione un perfil\n'''
    if CreaVm_parametrizada(perfil,ram,disco)=="error":
        return'''Sólo se admiten valores numéricos en los parámetros RAM y disco\n'''
    return estadosVM()

#Pagina que permite seleccionar los servicios deseados.
@get('/servicios')
def servicios():
    peticionhtml = open("/root/tesis/Tesis/Python/HTMLs/servicios.html","r", 0)
    return peticionhtml

#Toma los servicios deseados y genera el correspondiente archivo de puppet para su correcto funcionamiento
@post('/servicios')
def do_servicios():
    c_eclipse = request.forms.get('c_eclipse')
    c_idle = request.forms.get('c_idle')
    c_repositorio = request.forms.get('c_repositorio')
    c_update = request.forms.get('c_update')
    c_usuarios = request.forms.get('c_usuarios')

    u_eclipse = request.forms.get('u_eclipse')
    u_idle = request.forms.get('u_idle')
    u_repositorio = request.forms.get('u_repositorio')
    u_ubuntugui = request.forms.get('u_ubuntugui')
    u_update = request.forms.get('u_update')
    u_usuarios = request.forms.get('u_usuarios')

    w_windowsus = request.forms.get('w_windowsus')

    key = {'None': "#", 'on': ""}

    #Elimino el viejo archivo
    commands.getoutput("rm -f /etc/puppetlabs/code/environments/production/manifests/z_genericos.pp")
    #coloco los nodos
    commands.getoutput("echo \"node /centos*/{\" >> /etc/puppetlabs/code/environments/production/manifests/z_genericos.pp")
    commands.getoutput("echo \"" + key[str(c_eclipse)]+"include eclipse\" >> /etc/puppetlabs/code/environments/production/manifests/z_genericos.pp")
    commands.getoutput("echo \"" + key[str(c_idle)]+"include idle\" >> /etc/puppetlabs/code/environments/production/manifests/z_genericos.pp")
    commands.getoutput("echo \"" + key[str(c_repositorio)]+"include repositorio\" >> /etc/puppetlabs/code/environments/production/manifests/z_genericos.pp")
    commands.getoutput("echo \"" + key[str(c_update)]+"include update\" >> /etc/puppetlabs/code/environments/production/manifests/z_genericos.pp")
    commands.getoutput("echo \"" + key[str(c_usuarios)]+"include usuarios\" >> /etc/puppetlabs/code/environments/production/manifests/z_genericos.pp")
    commands.getoutput("echo \"}\" >> /etc/puppetlabs/code/environments/production/manifests/z_genericos.pp")

    commands.getoutput("echo \"node /ubuntu*/{\" >> /etc/puppetlabs/code/environments/production/manifests/z_genericos.pp")
    commands.getoutput("echo \"include ubuntugui\" >> /etc/puppetlabs/code/environments/production/manifests/z_genericos.pp")
    commands.getoutput("echo \"" + key[str(u_eclipse)]+"include eclipse\" >> /etc/puppetlabs/code/environments/production/manifests/z_genericos.pp")
    commands.getoutput("echo \"" + key[str(u_idle)]+"include idle\" >> /etc/puppetlabs/code/environments/production/manifests/z_genericos.pp")
    commands.getoutput("echo \"" + key[str(u_repositorio)]+"include repositorio\" >> /etc/puppetlabs/code/environments/production/manifests/z_genericos.pp")
    commands.getoutput("echo \"" + key[str(u_update)]+"include update\" >> /etc/puppetlabs/code/environments/production/manifests/z_genericos.pp")
    commands.getoutput("echo \"" + key[str(u_usuarios)]+"include usuarios\" >> /etc/puppetlabs/code/environments/production/manifests/z_genericos.pp")
    commands.getoutput("echo \"}\" >> /etc/puppetlabs/code/environments/production/manifests/z_genericos.pp")

    commands.getoutput("echo \"node /windows*/{\" >> /etc/puppetlabs/code/environments/production/manifests/z_genericos.pp")
    commands.getoutput("echo \"" + key[str(w_windowsus)]+"include usuarios\" >> /etc/puppetlabs/code/environments/production/manifests/z_genericos.pp")
    commands.getoutput("echo \"}\" >> /etc/puppetlabs/code/environments/production/manifests/z_genericos.pp")

    commands.getoutput("echo \"node /default*/{\" >> /etc/puppetlabs/code/environments/production/manifests/z_genericos.pp")
    commands.getoutput("echo \"}\" >> /etc/puppetlabs/code/environments/production/manifests/z_genericos.pp")

    return servicios()

#Pagina que muestra las maquinas existentes y permite setear servicios a maquinas individuales.
@get('/politicas_maquinas')
def politicas():
    maquinas = estado()
    return genera_html_politicas(maquinas)

#Toma los servicios deseados y crea un archivo individual para esa VM
@post('/politicas_maquinas')
def do_politicas():
    eclipse = request.forms.get('eclipse')
    idle = request.forms.get('idle')
    repositorio = request.forms.get('repositorio')
    update = request.forms.get('update')
    usuarios = request.forms.get('usuarios')
    maquina = request.forms.get('maquina')

    key = {'None': "#", 'on': ""}

    # Elimino el viejo archivo
    commands.getoutput("rm -f /etc/puppetlabs/code/environments/production/manifests/"+maquina + ".pp")
    commands.getoutput("touch /etc/puppetlabs/code/environments/production/manifests/" + maquina + ".pp")
    # coloco los nodos
    commands.getoutput("echo \"node " + maquina + "{\" >> /etc/puppetlabs/code/environments/production/manifests/" + maquina + ".pp")
    commands.getoutput("echo \"include ubuntugui\" >> /etc/puppetlabs/code/environments/production/manifests/" + maquina + ".pp")
    commands.getoutput("echo \"" + key[str(eclipse)] + "include eclipse\" >> /etc/puppetlabs/code/environments/production/manifests/" + maquina + ".pp")
    commands.getoutput("echo \"" + key[str(idle)] + "include idle\" >> /etc/puppetlabs/code/environments/production/manifests/" + maquina + ".pp")
    commands.getoutput("echo \"" + key[str(repositorio)] + "include repositorio\" >> /etc/puppetlabs/code/environments/production/manifests/" + maquina + ".pp")
    commands.getoutput("echo \"" + key[str(update)] + "include update\" >> /etc/puppetlabs/code/environments/production/manifests/" + maquina + ".pp")
    commands.getoutput("echo \"" + key[str(usuarios)] + "include usuarios\" >> /etc/puppetlabs/code/environments/production/manifests/" + maquina + ".pp")
    commands.getoutput("echo \"}\" >> /etc/puppetlabs/code/environments/production/manifests/" + maquina + ".pp")

    return politicas()

#Genera el HTML de las politicas de las maquinas.
def genera_html_politicas(maquinas):
    html = '''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN">
<html>
	<head>
	  <title>Servidor de maquinas virtuales</title>
		<!-- Aca empieza la parte de css que va a formatear la pagina para que quede de la forma deseada -->
		<!-- Deberia ser una unica linea, que es la siguiente, pero con el bottle no anda y no se porque -->
		<!--<link rel="stylesheet" href="estilo1.css"> -->
		<style type="text/css">
			/*Esta seccion indica como debe ser el cuerpo de la pagina*/
			  body {
				padding-left: 14em;/*debe ubicarse a la derecha, para dejar espacio a la izquierda para el menu*/
				color: black;/*Indico letras negras*/
				background-color: #dcffff }/*indico color de fondo celeste*/

			/*Esta seccion indica como debe el menu, su ubicacion presisa*/
			ul.navbar {
				list-style-type: none;/*Sin el item y que no deje espacio vacio*/
				padding: 0;
				margin: 0;
				position: absolute;/*posicion independiente del cuerpo de la pagina*/
				top: 2em;/*ubicacion*/
				left: 1em;
				width: 11em }

			/*El menu tiene recuadros blancos*/
			ul.navbar li {
				background: white;
				margin: 0.5em 0;
				padding: 0.3em;
				border-right: 1em solid black }/*linea negra a la derecha*/

			/*si aun no se ingreso al enlace esta azul, sino purpura*/
			ul.navbar a {
				text-decoration: none }
				a:link {
					color: blue }
				a:visited {
					color: purple }
		</style>

	</head>
	<body>
		<form action="/politicas_maquinas" method="post">
		<H2>Seleccione una maquina virtual.</H2>
		<SELECT NAME="maquina" SIZE="1">
'''

    for i in range(0,len(maquinas)-1,2):
        html = html + '''<OPTION VALUE="'''+maquinas[i]+'''">'''+maquinas[i]+'''</OPTION>'''

    html = html + '''</SELECT>

        <H3>Marque los servicios deseados para la máquina virtual.</H3>
        <br/>
            <INPUT type="checkbox" name="eclipse">eclipse<BR>
            <INPUT type="checkbox" name="idle">idle<BR>
            <INPUT type="checkbox" name="repositorio">repositorio(solo para CentOS)<BR>
            <INPUT type="checkbox" name="update">update<BR>
            <INPUT type="checkbox" name="usuarios">usuarios<BR>
		<br>

            <hr> <input value="Aceptar" type="submit" /> <br>
		</form>
		<ul class="navbar">
		    <li><a href="virtual_machine">Crear máquinas virtuales optimizadas.</a>
			<li><a href="virtual_machine_parametrizada">Crear máquina virtual con parámetros.</a>
			<li><a href="servicios">Editar configuraciones de las máquinas virtuales.</a>
			<li><a href="estados">Ver estado actual de las máquinas virtuales.</a>
		</ul>

	</body>
</html>'''

    return html

run(host='0.0.0.0', port=8888, debug=True)

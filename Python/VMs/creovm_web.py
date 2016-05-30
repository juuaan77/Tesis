__author__ = 'juan'

import os, time, commands,re
from CreaVm_with_profile_v2 import CreaVm, CreaVm_parametrizada
from EstadoVM import genera_estado_html,estado
from bottle import get, post, request, run,route

@get('/estados') #Pagina principal, la cual pide los datos necesarios para crear la VM.
def estadosVM():
    #peticionhtml = open("/home/werner/demo/HTMLs/Peticion_parametros_CreacionVM.html","r", 0)
    return genera_estado_html()
    #return '''fruta'''

@post('/estados') #Pagina principal, la cual pide los datos necesarios para crear la VM.
def do_estadosVM():
    estados = estado()
    encendido = ""
    apagado = ""
    for i in range(0,len(estados)-1,2):
        if request.forms.get("Prender-"+estados[i])=="on":
            #encendido = encendido + "prendo" + estados[i]
            encendido= encendido + "\n" + commands.getoutput("virsh start "+estados[i])
        elif request.forms.get("Apagar-"+estados[i])=="on":
            #apagado = apagado +"apago" + estados[i]
            apagado = apagado + "\n" + commands.getoutput("virsh shutdown "+estados[i])

    return encendido +"\n"+ apagado +"\n"+ estadosVM()

@get('/virtual_machine') #Pagina principal, la cual pide los datos necesarios para crear la VM.
def creaVM():
    #peticionhtml = open("/home/werner/demo/HTMLs/Peticion_parametros_CreacionVM.html","r", 0)
    peticionhtml = open("/home/juan/Tesis/Python/HTMLs/virtual_machine.html","r", 0)
    return peticionhtml
    #return '''fruta'''

@post('/virtual_machine') #toma los parametros ingresados e indica si se creo o no la VM con exito.
def do_creaVM():
    try:
        ncentos = int(request.forms.get('ncentos'))
        nubuntu = int(request.forms.get('nubuntu'))
        nwindows = int(request.forms.get('nwindows'))
    except ValueError:
        return '''Por favor, ingrese solo el NUMERO de la cantidad de maquinas que desea crear \n'''

    if CreaVm(nubuntu,"ubuntugui")=="error" or CreaVm(ncentos,"centos")=="error" or CreaVm(nwindows,"windows")=="error":
        return'''Por favor, ingrese solo el NUMERO de la cantidad de maquinas que desea crear \n'''

    return estadosVM()

@get('/virtual_machine_parametrizada') #Pagina principal, la cual pide los datos necesarios para crear la VM.
def creaVM_parametrizado():
    #peticionhtml = open("/home/werner/demo/HTMLs/Peticion_parametros_CreacionVM.html","r", 0)
    peticionhtml = open("/home/juan/Tesis/Python/HTMLs/virtual_machine_parametrizada.html","r", 0)
    return peticionhtml
    #return '''fruta'''

@post('/virtual_machine_parametrizada') #toma los parametros ingresados e indica si se creo o no la VM con exito.
def do_creaVM_parametrizado():
    perfil = request.forms.get('boton1')
    ram = request.forms.get('ram')
    disco = request.forms.get('disco')
    if str(perfil)=="None":
        return '''Por favor, seleccione un perfil\n'''
    if CreaVm_parametrizada(perfil,ram,disco)=="error":
        return'''Por favor, ingrese solo el NUMERO en la cantidad de ram y disco\n'''
    return estadosVM()

@get('/servicios')
def servicios():
    peticionhtml = open("/home/juan/Tesis/Python/HTMLs/servicios.html","r", 0)
    return peticionhtml

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

    #Elimino el viejo site
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
    commands.getoutput("echo \"" + key[str(u_eclipse)]+"include eclipse\" >> /etc/puppetlabs/code/environments/production/manifests/z_genericos.pp")
    commands.getoutput("echo \"" + key[str(u_idle)]+"include idle\" >> /etc/puppetlabs/code/environments/production/manifests/z_genericos.pp")
    commands.getoutput("echo \"" + key[str(u_repositorio)]+"include repositorio\" >> /etc/puppetlabs/code/environments/production/manifests/z_genericos.pp")
    commands.getoutput("echo \"" + key[str(u_ubuntugui)]+"include ubuntugui\" >> /etc/puppetlabs/code/environments/production/manifests/z_genericos.pp")
    commands.getoutput("echo \"" + key[str(u_update)]+"include update\" >> /etc/puppetlabs/code/environments/production/manifests/z_genericos.pp")
    commands.getoutput("echo \"" + key[str(u_usuarios)]+"include usuarios\" >> /etc/puppetlabs/code/environments/production/manifests/z_genericos.pp")
    commands.getoutput("echo \"}\" >> /etc/puppetlabs/code/environments/production/manifests/z_genericos.pp")

    commands.getoutput("echo \"node /windows*/{\" >> /etc/puppetlabs/code/environments/production/manifests/z_genericos.pp")
    commands.getoutput("echo \"" + key[str(w_windowsus)]+"include windowsus\" >> /etc/puppetlabs/code/environments/production/manifests/z_genericos.pp")
    commands.getoutput("echo \"}\" >> /etc/puppetlabs/code/environments/production/manifests/z_genericos.pp")

    commands.getoutput("echo \"node /default*/{\" >> /etc/puppetlabs/code/environments/production/manifests/z_genericos.pp")
    commands.getoutput("echo \"}\" >> /etc/puppetlabs/code/environments/production/manifests/z_genericos.pp")

    return servicios()
    #return str(c_eclipse) + "-" + str(c_idle) + "-" + str(c_repositorio) + "-" + str(c_update) + "-" + str(c_usuarios)

@get('/politicas_maquinas')
def politicas():
    maquinas = estado()
    return genera_html_politicas(maquinas)

@post('/politicas_maquinas')
def do_politicas():
    eclipse = request.forms.get('eclipse')
    idle = request.forms.get('idle')
    repositorio = request.forms.get('repositorio')
    update = request.forms.get('update')
    usuarios = request.forms.get('usuarios')
    maquina = request.forms.get('maquina')

    key = {'None': "#", 'on': ""}

    # Elimino el viejo site
    commands.getoutput("rm -f /home/juan/"+maquina + ".pp")
    commands.getoutput("touch /home/juan/" + maquina + ".pp")
    # coloco los nodos
    commands.getoutput("echo \"node " + maquina + "{\" >> /etc/puppetlabs/code/environments/production/manifests/" + maquina)
    commands.getoutput("echo \"" + key[str(eclipse)] + "include eclipse\" >> /etc/puppetlabs/code/environments/production/manifests/" + maquina)
    commands.getoutput("echo \"" + key[str(idle)] + "include idle\" >> /etc/puppetlabs/code/environments/production/manifests/" + maquina)
    commands.getoutput("echo \"" + key[str(repositorio)] + "include repositorio\" >> /etc/puppetlabs/code/environments/production/manifests/" + maquina)
    commands.getoutput("echo \"" + key[str(update)] + "include update\" >> /etc/puppetlabs/code/environments/production/manifests/" + maquina)
    commands.getoutput("echo \"" + key[str(usuarios)] + "include usuarios\" >> /etc/puppetlabs/code/environments/production/manifests/" + maquina)
    commands.getoutput("echo \"}\" >> /etc/puppetlabs/code/environments/production/manifests/" + maquina)

    return politicas()

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

        <H3>Marque los servicios que desea que tenga la maquina virtual.</H3>
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
		    <li><a href="virtual_machine">Crear virtual machine sin parametros.</a>
			<li><a href="virtual_machine_parametrizada">Crear virtual machine con parametros.</a>
			<li><a href="servicios">Editar configuraciones de las maquinas virtuales.</a>
			<li><a href="estados">Ver estado actual de las maquinas virtuales.</a>
		</ul>

	</body>
</html>'''

    return html

#run(host='192.168.0.101', port=8080, debug=True)
run(host='0.0.0.0', port=8080, debug=True)
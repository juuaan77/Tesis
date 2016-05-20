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

    return encendido + apagado + estadosVM()

@get('/virtual_machine') #Pagina principal, la cual pide los datos necesarios para crear la VM.
def creaVM():
    #peticionhtml = open("/home/werner/demo/HTMLs/Peticion_parametros_CreacionVM.html","r", 0)
    peticionhtml = open("/home/juan/Tesis/Python/HTMLs/virtual_machine.html","r", 0)
    return peticionhtml
    #return '''fruta'''

@post('/virtual_machine') #toma los parametros ingresados e indica si se creo o no la VM con exito.
def do_creaVM():
    ncentos = request.forms.get('ncentos')
    nubuntu = request.forms.get('nubuntu')
    nwindows = request.forms.get('nwindows')

    if CreaVm(nubuntu,"ubuntugui")=="error" or CreaVm(ncentos,"ubuntugui")=="error" or CreaVm(nwindows,"ubuntugui")=="error":
        return'''Por favor, ingrese solo el NUMERO de la cantidad de maquinas que desea crear \n'''

    #CreaVm(ncentos,"ubuntugui")
    #CreaVm(nwindows,"ubuntugui")
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
    #CreaVm(ncentos,"ubuntugui")
    #CreaVm(nwindows,"ubuntugui")
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
    commands.getoutput("rm -f /home/juan/site.pp")
    #coloco los nodos
    commands.getoutput("echo \"node /centos*/{\" >> /home/juan/site.pp")
    commands.getoutput("echo \"" + key[str(c_eclipse)]+"include eclipse\" >> /home/juan/site.pp")
    commands.getoutput("echo \"" + key[str(c_idle)]+"include idle\" >> /home/juan/site.pp")
    commands.getoutput("echo \"" + key[str(c_repositorio)]+"include repositorio\" >> /home/juan/site.pp")
    commands.getoutput("echo \"" + key[str(c_update)]+"include update\" >> /home/juan/site.pp")
    commands.getoutput("echo \"" + key[str(c_usuarios)]+"include usuarios\" >> /home/juan/site.pp")
    commands.getoutput("echo \"}\" >> /home/juan/site.pp")

    commands.getoutput("echo \"node /ubuntu*/{\" > /home/juan/site.pp")
    commands.getoutput("echo \"" + key[str(u_eclipse)]+"include eclipse\" >> /home/juan/site.pp")
    commands.getoutput("echo \"" + key[str(u_idle)]+"include idle\" >> /home/juan/site.pp")
    commands.getoutput("echo \"" + key[str(u_repositorio)]+"include repositorio\" >> /home/juan/site.pp")
    commands.getoutput("echo \"" + key[str(u_ubuntugui)]+"include ubuntugui\" >> /home/juan/site.pp")
    commands.getoutput("echo \"" + key[str(u_update)]+"include update\" >> /home/juan/site.pp")
    commands.getoutput("echo \"" + key[str(u_usuarios)]+"include usuarios\" >> /home/juan/site.pp")
    commands.getoutput("echo \"}\" >> /home/juan/site.pp")

    commands.getoutput("echo \"node /windows*/{\" >> /home/juan/site.pp")
    commands.getoutput("echo \"" + key[str(w_windowsus)]+"include windowsus\" >> /home/juan/site.pp")
    commands.getoutput("echo \"}\" >> /home/juan/site.pp")

    commands.getoutput("echo \"node /default*/{\" >> /home/juan/site.pp")
    commands.getoutput("echo \"}\" >> /home/juan/site.pp")

    return servicios()
    #return str(c_eclipse) + "-" + str(c_idle) + "-" + str(c_repositorio) + "-" + str(c_update) + "-" + str(c_usuarios)

#run(host='192.168.0.101', port=8080, debug=True)
run(host='localhost', port=8080, debug=True)
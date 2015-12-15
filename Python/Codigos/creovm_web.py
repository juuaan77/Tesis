__author__ = 'juan'

import os, time
from bottle import get, post, request, run # or route

@get('/') #Pagina principal, la cual pide los datos necesarios para crear la VM.
def creaVM():
    peticionhtml = open("/home/werner/demo/HTMLs/Peticion_parametros_CreacionVM.html","r", 0)
    #peticionhtml = open("/home/juan/Proyecto Integrador Desde Cero/Repositorio/Python/HTMLs/Peticion_parametros_CreacionVM.html","r", 0)
    return peticionhtml

@post('/') #toma los parametros ingresados e indica si se creo o no la VM con exito.
def do_creaVM():
    namevm = request.forms.get('namevm')
    ramvm = request.forms.get('ramvm')
    discovm = request.forms.get('discovm')
    MAC = request.forms.get('MAC')
    IPVM = request.forms.get('IPVM')
    IPCobbler = request.forms.get('IPCobbler')
    perfil = request.forms.get('perfil')
    hostname = request.forms.get('hostname')
    #Una vez obtenidos todos los paramentros desde la interfaz web, debo primero, crear el sistema.
    os.system("/home/werner/demo/bash/CreaSistema.sh " + IPCobbler + " " + namevm  + " " +  perfil  + " " +  hostname  + " " +  MAC  + " " + IPVM)
    #Le doy el tiempo necesario para que cree el sistema.
    time.sleep(3)
    os.system("/home/werner/demo/bash/CreacionVM.sh " + namevm + " " + ramvm  + " " + namevm  + " " + discovm + " " + MAC)
    return '''La maquina virtual se creo corectamente'''



run(host='localhost', port=8080, debug=True)
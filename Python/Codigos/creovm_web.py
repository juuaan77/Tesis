__author__ = 'juan'

import os
from bottle import get, post, request, run # or route

@get('/') #Pagina principal, la cual pide los datos necesarios para crear la VM.
def creaVM():
    peticionhtml = open("/home/juan/Proyecto Integrador Desde Cero/Repositorio/Python/HTMLs/Peticion_parametros_CreacionVM.html","r", 0)
    return peticionhtml

@post('/') #toma los parametros ingresados e indica si se creo o no la VM con exito.
def do_creaVM():
    namevm = request.forms.get('namevm')
    ramvm = request.forms.get('ramvm')
    discovm = request.forms.get('discovm')
    IPcobbler = request.forms.get('IPcobbler')
    IPcrear = request.forms.get('IPcrear')
    os.system("/home/juan/Proyecto\ Integrador\ Desde\ Cero/Repositorio/Codigos\ en\ bash/CreacionVM.sh " + namevm + " " + ramvm  + " " + namevm  + " " + discovm + " " + IPcobbler  + " " + IPcrear)
    os.system("echo $(whoami) > /home/juan/Escritorio/python")
    os.system("echo " + namevm + " >> /home/juan/Escritorio/python")
    os.system("echo " + ramvm + " >> /home/juan/Escritorio/python")
    os.system("echo " + discovm + " >> /home/juan/Escritorio/python")
    os.system("echo " + IPcrear + " >> /home/juan/Escritorio/python")
    os.system("echo " + IPcobbler + " >> /home/juan/Escritorio/python")

    return'''
        namevm, '--' ramvm, '--'discovm, '--'IPcobbler, '--',IPcrear
        '''


run(host='localhost', port=8080, debug=True)
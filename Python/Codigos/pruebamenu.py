__author__ = 'juan'

import os, time, commands,re
from bottle import get, post, request, run,route

@get('/') #Pagina principal, la cual pide los datos necesarios para crear la VM.
def creaVM():
    #peticionhtml = open("/home/werner/demo/HTMLs/Peticion_parametros_CreacionVM.html","r", 0)
    peticionhtml = open("/home/juan/Proyecto Integrador Desde Cero/Repositorio/Python/HTMLs/Pruebas de edicion.html","r", 0)
    return peticionhtml

@post('/') #toma los parametros ingresados e indica si se creo o no la VM con exito.
def do_creaVM():

    servicio = request.forms.get('servicio')
    seleccion ="Y el servicio es: " + str(servicio)

    return seleccion

run(host='localhost', port=8080, debug=True)
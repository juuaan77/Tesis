__author__ = 'juan'

import os, time, commands,re
from bottle import get, post, request, run,route

@get('/') #Pagina principal, la cual pide los datos necesarios para crear la VM.
def creaVM():
    #peticionhtml = open("/home/werner/demo/HTMLs/Peticion_parametros_CreacionVM.html","r", 0)
    peticionhtml = open("/home/juan/Proyecto Integrador Desde Cero/Repositorio/Python/HTMLs/Peticion_parametros_CreacionVM.html","r", 0)
    return peticionhtml
    #return '''fruta'''

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
    servicio = request.forms.get('servicio')
    #Una vez obtenidos todos los paramentros desde la interfaz web, debo primero, crear el sistema.
    #os.system("/home/werner/demo/bash/CreaSistema.sh " + IPCobbler + " " + namevm  + " " +  perfil  + " " +  hostname  + " " +  MAC  + " " + IPVM)
    os.system("/home/juan/Proyecto\ Integrador\ Desde\ Cero/Repositorio/Codigos\ en\ bash/CreaSistema.sh " + IPCobbler + " " + namevm  + " " +  perfil  + " " +  hostname  + " " +  MAC  + " " + IPVM)
    print "/home/juan/Proyecto Integrador Desde Cero/Repositorio/Codigos en bash/CreaSistema.sh " + IPCobbler + " " + namevm  + " " +  perfil  + " " +  hostname  + " " +  MAC  + " " + IPVM
    #Le doy el tiempo necesario para que cree el sistema.
    time.sleep(3)
    #os.system("/home/werner/demo/bash/CreacionVM.sh " + namevm + " " + ramvm  + " " + namevm  + " " + discovm + " " + MAC)
    os.system("/home/juan/Proyecto\ Integrador\ Desde\ Cero/Repositorio/Codigos\ en\ bash/CreacionVM.sh " + namevm + " " + ramvm  + " " + namevm  + " " + discovm + " " + MAC)
    print "/home/juan/Proyecto Integrador Desde Cero/Repositorio/Codigos en bash/CreacionVM.sh " + namevm + " " + ramvm  + " " + namevm  + " " + discovm + " " + MAC
    #time.sleep(3)
    #puppet = {}
    #puppet["web"] = "httpd"
    #puppet["dbs"] = "MySQL"
    #puppet["nfs"] = "NFS"
    #manifiesto = open("/home/juan/Escritorio/manifiesto","a", 0)
    #manifiesto.write( IPVM + "{\n"
    #              "       include " + puppet[servicio] + ";\n"
    #              "}\n");

    return estadoVM()

@get('/estadoVM')
def estadoVM():
    salida = commands.getstatusoutput("virsh list --all")
    salida = re.split("\n", salida[1])
    dominio=""
    for i in range(2,len(salida)-1,1):
        dominio=dominio + "<hr>" +salida[i]+ "<br>"
    return dominio# + ''' <hr> <form action="/" method="post">
    #<hr> <input value="Crear Virtual Machine" type="submit" /> <br>
    #</form>
   #<br>'''
#
#@post('/estadoVM')
#def do_estadoVM():
#    return '''<META HTTP-EQUIV="Refresh" CONTENT="0; URL=http://localhost:8080/creaVM">'''


run(host='0.0.0.0', port=8080, debug=True)

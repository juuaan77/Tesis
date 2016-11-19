#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'juan'

import commands,re,fnmatch


def estado():
    '''Obtiene el estado (encendido o apagado) de las VMs

        parametros: none.

        return: Lista Nombre_VM - estado'''

    salida = commands.getstatusoutput("virsh list --all")
    salida = re.split("\n", salida[1])
    dominio=""
    for i in range(1,len(salida)-1,1):
        dominio=dominio +salida[i]


    dominio = re.split(" ", dominio)

    salida = ""
    for i in range(1,len(dominio),1):
        if fnmatch.fnmatch(dominio[i], '*[a-z]*'):
            salida = salida + " " + dominio[i]

    dominio = re.split(" ", salida)
    dominio.pop(0)

    return dominio

#Genera dinamicamente el archivo HTML queindica el estado de las maquinas virtuales.
def genera_estado_html():

    dominio = estado()

    color = {'ejecutando': "21F911", 'apagado': "F91111"}
    accion = {'ejecutando': "Apagar", 'apagado': "Prender"}
    #print color["ejecutando"]

    html='''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN">
    <html>
        <head>
          <title>Estado de las maquinas virtuales</title>
          <META HTTP-EQUIV="refresh" CONTENT="60">
          <!-- Aca empieza la parte de css que va a formatear la pagina para que quede de la forma deseada -->
		<!-- Deberia ser una unica linea, que es la siguiente, pero con el bottle no anda y no se porque -->
		<!--<link rel="stylesheet" href="estilo1.css"> -->
		<style type="text/css">
			/*Esta seccion indica como debe ser el cuerpo de la pagina*/
			  body {
			    position:absolute;
				padding-left: 28em;/*debe ubicarse a la derecha, para dejar espacio a la izquierda para el menu*/
				padding-top: 15em
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
            <form action="/estados" method="post">
            <TABLE BORDERCOLOR="040404" BORDER="1" cellpadding="1" cellspacing="1">
            <TR>
                <TH>Nombre de la VM</TH>
                <TH>Estado</TH>
                <TH colspan="2">Accion</TH>
            </TR>'''

    for i in range(0,len(dominio)-1,2):
        html=html+'''<TR>
                    <TD>'''+dominio[i]+'''</TD>
                <TD BGCOLOR='''+color[dominio[i+1]]+'''> '''+dominio[i+1]+'''</TD>
                <TD><INPUT type="checkbox" name="Prender-'''+dominio[i]+'''">Encender<BR></TD>
				<TD><INPUT type="checkbox" name="Apagar-'''+dominio[i]+'''">Apagar<BR></TD>
            </TR>'''

    html = html +'''</TABLE>
    <TD><input value="Ejecutar acción" type="submit" /></TD>
    <ul class="navbar">
			<li><a href="virtual_machine">Crear máquinas virtuales optimizadas.</a>
			<li><a href="virtual_machine_parametrizada">Crear máquina virtual con parámetros.</a>
			<li><a href="servicios">Editar configuraciones de las máquinas virtuales.</a>
			<li><a href="politicas_maquinas">Editar política de una máquina virtual.</a>
		</ul>
        </body>
    </html>'''

    #print html

    return html

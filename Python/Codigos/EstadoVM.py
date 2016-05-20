__author__ = 'juan'

import commands,re,fnmatch

def estado():
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

    print dominio

    color = {'ejecutando': "21F911", 'apagado': "F91111"}

    print color["ejecutando"]

    html='''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN">
    <html>
        <head>
          <title>Estado de las maquinas virtuales</title>
        </head>

        <body>
            <TABLE BORDERCOLOR="040404" BORDER="1" cellpadding="1" cellspacing="1">
            <TR>
                <TH>Nombre de la VM</TH>
                <TH>Estado</TH>
            </TR>'''

    for i in range(0,len(dominio)-1,2):
        html=html+'''<TR>
                    <TD>'''+dominio[i]+'''</TD>
                <TD BGCOLOR='''+color[dominio[i+1]]+'''> '''+dominio[i+1]+'''</TD>
            </TR>'''

    html = html +'''</TABLE>
        </body>
    </html>'''

    print html

    return html
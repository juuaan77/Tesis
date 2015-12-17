__author__ = 'juan'

import commands,re
salida = commands.getstatusoutput("virsh list --all")
salida = re.split("\n", salida[1])
dominio=""
for i in range(1,len(salida)-1,1):
    dominio=dominio +salida[i]+ "\n"
print dominio
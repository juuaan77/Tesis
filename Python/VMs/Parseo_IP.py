import commands
import sys

#Obtengo la informacion del archivo dhcpd.leases, el caul contiene las direciones IP asociadas a las MAC
lista = commands.getoutput("cat /var/lib/dhcpd/dhcpd.leases")
mac = "52:54:00:fc:b9:54"
hostname = "Alumno1881"
parseado = lista.split("lease ")
i = 0
while i < int(len(parseado)):
    if mac in parseado[i] and hostname in parseado[i]:
        ip = parseado[i].split(" ")
        break
    else:
        ip = "naranja fanta"
    i = i+1


print ip[0]


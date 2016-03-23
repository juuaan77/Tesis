#Esta clase actualiza los paquetes una vez al mes.
class idle()
{
	if $osfamily == "Debian"
	{
		#Indico el paquete necesario a instalar.
		package { 'paquete_idle': #Este es el titulo del recurso, es el que aparecera en los LOGs
			ensure => installed, #aca le indico que quiero que el recurso este instalado
			name => "idle", #indico el nombre del paquete	
		}
	}
	elsif $osfamily == "RedHat"
	{
		#Indico el paquete necesario a instalar.
		package { 'paquete_python-tools': #Este es el titulo del recurso, es el que aparecera en los LOGs
			ensure => installed, #aca le indico que quiero que el recurso este instalado
			name => "python-tools", #indico el nombre del paquete	
		}
	}
}

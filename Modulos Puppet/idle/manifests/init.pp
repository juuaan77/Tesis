#Instala la IDE idle para python.
class idle()
{
	if $osfamily == "Debian"
	{
		#Obtengo los .deb para evitar usar internet.
		exec{'descarga_idle' :
                	command => "/usr/bin/curl ftp://192.168.122.1/proyectointegrador/Ubuntu14/idle.tar -o /var/cache/apt/archives/idle.tar", 
                	cwd => "/", #indico desde que directorio se ejecuta el comando.
                	unless => "/bin/ls /var/cache/apt/archives/idle.tar",#Ejecuta a menos que este comando sea exitoso.
        	}		

		#Desempaqueto los .deb
        	exec{'desempaqueta_idle' :
                	command => "/bin/tar -xvf /var/cache/apt/archives/idle.tar -C /var/cache/apt/archives/", 
                	cwd => "/", #indico desde que directorio se ejecuta el comando
                	require => Exec['descarga_idle'],#Requiere este recurso
                	unless => '/bin/grep "desempaqueta_idle]/returns) executed successfully" /var/log/syslog',
        	}


		#Indico el paquete necesario a instalar.
		package { 'paquete_idle': #Este es el titulo del recurso, es el que aparecera en los LOGs
			ensure => installed, #aca le indico que quiero que el recurso este instalado
			name => "idle", #indico el nombre del paquete
			require => Exec['desempaqueta_idle'],	
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

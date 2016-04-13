#Clase que instala la interfaz grafica gnome en ubuntu.
class ubuntugui{

	#Este IF es para evitar errores si se comete el error de colocar este manifiesto en una maquina no apta, por ej Centos.
	if $osfamily == "Debian"
	{
		#Obtengo los paquetes de gui, asi evito descargarlos
		exec{'descarga_gui' :
			command => "/usr/bin/curl ftp://192.168.122.1/proyectointegrador/Ubuntu14/ubuntu_gui.tar -o /var/cache/apt/archives/ubuntu_gui.tar", #Este es el comando que deseo que se ejecute
			cwd => "/", #indico desde que directorio se ejecuta el comando
			unless => "/bin/ls /var/cache/apt/archives/ubuntu_gui.tar",
		}

		#Descomprimo el paquete.
		exec{'desempaqueta_gui' :
			command => "/bin/tar -xvf /var/cache/apt/archives/ubuntu_gui.tar -C /var/cache/apt/archives/", #Este es el comando que deseo que se ejecute
			cwd => "/", #indico desde que directorio se ejecuta el comando
			require => Exec['descarga_gui'],#Requiere este recurso
			unless => '/bin/grep "desempaqueta_gui]/returns) executed successfully" /var/log/syslog',
		}
	
		#Estos paquetes son los necesarios para que funcione la GUI
		package { 'paquete_xinit': #Este es el titulo del recurso, es el que aparecera en los LOGs
			ensure => installed, #aca le indico que quiero que el recurso este instalado
			name => "xinit", #indico el nombre del paquete
			require => Exec['desempaqueta_gui'],#Requiere este recurso	
		}

		package { 'paquete_xorg': #Este es el titulo del recurso, es el que aparecera en los LOGs
			ensure => installed, #aca le indico que quiero que el recurso este instalado
			name => "xorg", #indico el nombre del paquete
			require => Exec['desempaqueta_gui'],#Requiere este recurso	
		}

		package { 'paquete_gnome-core': #Este es el titulo del recurso, es el que aparecera en los LOGs
			ensure => installed, #aca le indico que quiero que el recurso este instalado
			name => "gnome-core", #indico el nombre del paquete
			require => Exec['desempaqueta_gui'],#Requiere este recurso	
		}
	}
}

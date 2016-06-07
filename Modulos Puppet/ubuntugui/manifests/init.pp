#Clase que instala la interfaz grafica gnome en ubuntu.
class ubuntugui{

	#Este IF es para evitar errores si se comete el error de colocar este manifiesto en una maquina no apta, por ej Centos.
	if $osfamily == "Debian"
	{
		#Obtengo los paquetes de gui, asi evito descargarlos
		exec{'descarga_gui' :
			command => "/usr/bin/curl ftp://192.168.122.1/proyectointegrador/Ubuntu14/ubuntu_gui.tar.gz -o /var/cache/apt/archives/ubuntu_gui.tar.gz", #Este es el comando que deseo que se ejecute
			cwd => "/", #indico desde que directorio se ejecuta el comando
			unless => "/bin/ls /var/cache/apt/archives/ubuntu_gui.tar.gz",
		}

		#Descomprimo el paquete.
		exec{'desempaqueta_gui' :
			command => "/bin/tar -xzvf /var/cache/apt/archives/ubuntu_gui.tar.gz -C /var/cache/apt/archives/", #Este es el comando que deseo que se ejecute
			cwd => "/", #indico desde que directorio se ejecuta el comando
			require => Exec['descarga_gui'], #Requiere este recurso
			#unless => '/bin/grep "desempaqueta_gui]/returns) executed successfully" /var/log/syslog',
		}
		#Actualizo el gestor de descargas
		exec{'actualizo_gestor':
			command =>"/usr/bin/apt-get update -y",
			cwd => "/",
			unless => '/bin/grep "actualizo_gestor]/returns) executed successfully" /var/log/syslog',
		}
	
		#Estos paquetes son los necesarios para que funcione la GUI
		package { 'paquete_xinit': #Este es el titulo del recurso, es el que aparecera en los LOGs
			ensure => installed, #aca le indico que quiero que el recurso este instalado
			name => "xinit", #indico el nombre del paquete
			require =>[Exec['desempaqueta_gui'],Exec['actualizo_gestor']],#Requiere este recurso	
			install_options => ['--force-yes'],
		}

		package { 'paquete_xorg': #Este es el titulo del recurso, es el que aparecera en los LOGs
			ensure => installed, #aca le indico que quiero que el recurso este instalado
			name => "xorg", #indico el nombre del paquete
			require => [Exec['desempaqueta_gui'],Exec['actualizo_gestor']],#Requiere este recurso
			install_options => ['--force-yes'],	
		}

		package { 'paquete_gnome-core': #Este es el titulo del recurso, es el que aparecera en los LOGs
			ensure => installed, #aca le indico que quiero que el recurso este instalado
			name => "gnome-core", #indico el nombre del paquete
			require =>[Exec['desempaqueta_gui'],Exec['actualizo_gestor']],#Requiere este recurso
			install_options => ['--force-yes'],	
		}
	}
}

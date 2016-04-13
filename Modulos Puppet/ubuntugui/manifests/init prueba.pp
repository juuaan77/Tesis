class ubuntugui{
	
	#Debo tener los siguientes paquetes instalados
	package { 'paquete_apt_offline': #Este es el titulo del recurso, es el que aparecera en los LOGs
		ensure => installed, #aca le indico que quiero que el recurso este instalado
		name => "apt-offline", #indico el nombre del paquete	
	}

	#Obtengo los paquetes de gui
	exec{'descarga_gui' :
		command => "/usr/bin/curl ftp://192.168.122.1/gui/ubuntu_gui.zip -o /root/ubuntu_gui.zip", #Este es el comando que deseo que se ejecute
		cwd => "/", #indico desde que directorio se ejecuta el comando
		require => Package['paquete_apt_offline'],#Requiere este recurso
		unless => "/bin/ls /root/ubuntu_gui.zip",
	}

	exec{'desempaqueta_gui' :
		command => "/usr/bin/apt-offline install /root/ubuntu_gui.zip", #Este es el comando que deseo que se ejecute
		cwd => "/", #indico desde que directorio se ejecuta el comando
		require => Exec['descarga_gui'],#Requiere este recurso
		unless => '/bin/grep "desempaqueta_gui]/returns) executed successfully" /var/log/syslog',
	}

	package { 'paquete_xinit': #Este es el titulo del recurso, es el que aparecera en los LOGs
		ensure => installed, #aca le indico que quiero que el recurso este instalado
		name => "xinit", #indico el nombre del paquete
		require => Exec['desempaqueta_gui'],#Requiere este recurso	
	}

	package { 'paquete_x-window-system-core': #Este es el titulo del recurso, es el que aparecera en los LOGs
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

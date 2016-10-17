class httpd()
{

	#Aca indico que el paquete nfs debe estar instalado, como son dos, indico ambos paquetes.
	package { 'paquete_httpd': #Este es el titulo del recurso, es el que aparecera en los LOGs
		ensure => installed, #aca le indico que quiero que el recurso este instalado
		name => "httpd", #indico el nombre del paquete	
	}

	#Ejecuto el comandod de activacion del servicio
	exec{'activo_httpd' :
		command => "/sbin/chkconfig httpd on", #Este es el comando que deseo que se ejecute, en este caso, activa el servicio
		cwd => "/", #indico desde que directorio se ejecuta el comando
		require => Package['paquete_httpd'],#Antes de activar el servicio, los paquetes deben estar instalados.
	}


	#aca indico como quiero que sea el archivo /etc/exports
	file {'pagina_prueba':#Titulo del recurso
		ensure => file, #indico que sea un archivo
		owner => root, #indico el dueño del archivo
		mode => 0777, #indico los permisos de acceso al archivo.
		source => "/etc/puppet/modules/httpd/html/index.html",
		path => "/var/www/html/index.html", #indico la ubicacion del archivo
	}
	
	#aca defino el uno de los servicios
	service {'servicio_httpd':#Titulo del servicio
		ensure => running, #Indico que el servicio debe estar corriendo.
		name => "httpd",#Este es el nombre con que cetos reconoce al servicio.
		require => Exec['activo_httpd'],#Antes de activar el servicio, los paquetes deben estar instalados.
	}
}

#Clase que instalara el programa mysql y ademas, le seteara una contraseña de root pasada por parametro.
#En una prueba inicial, se utilizara una clave por defecto, la cual es qwerty,luego, se probara con clave por parametro.

class myqsl()
{

	#Aca indico los paquetes que se deben instalar.
	package { 'paquete_mysql': #Este es el titulo del recurso, es el que aparecera en los LOGs
		ensure => installed, #aca le indico que quiero que el recurso este instalado
		name => "mysql", #indico el nombre del paquete	
	}

	package { 'paquete_mysql-server': #Este es el titulo del recurso, es el que aparecera en los LOGs
		ensure => installed, #aca le indico que quiero que el recurso este instalado
		name => "mysql-community-server", #indico el nombre del paquete	
	}

	#Ejecuto el comandod de activacion del servicio
	exec{'activo_mysql' :
		command => "chkconfig mysqld on", #Este es el comando que deseo que se ejecute, en este caso, activa el servicio
		cwd => "/", #indico desde que directorio se ejecuta el comando
		require => Package['paquete_mysql-server'],#Antes de activar el servicio, los paquetes deben estar instalados.(el título)
		require => Package['paquete_mysql'],
	}
	
	#Inicio el serivicio
	service {'servicio_mysql':#Titulo del servicio
		ensure => running, #Indico que el servicio debe estar corriendo.
		name => "mysqld",#Este es el nombre con que cetos reconoce al servicio.
		require => Exec['activo_mysql'],Antes de iniciar el servicio debe estar activado
	}

	#Una vez instalado y activado el servicio, le setteo la clave de root.
	exec{'setteo_clave_root_mysql' :
		command => "mysqladmin -u root password 'qwerty'", #Este es el comando que deseo que se ejecute, en este caso, activa el servicio
		cwd => "/", #indico desde que directorio se ejecuta el comando
		require => Service['servicio_mysql'],#Antes de settear la clave root el servicio debe estar iniciado.
	}

	#Prueba para confirmar que funciono todo,creo una base de datos.
	exec{'creadb_mysql' :
		command => "mysqladmin -uroot -pqwerty create basededatospuppet", #Este es el comando que deseo que se ejecute, en este caso, activa el servicio
		cwd => "/", #indico desde que directorio se ejecuta el comando
		require => Exec['setteo_clave_root_mysql'],#Antes de intentar crear la base de datos, debo haber puesto una clave root.
	}
}

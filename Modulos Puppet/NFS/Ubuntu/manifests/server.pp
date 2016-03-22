class nfs::server()
{

	#Aca indico que el paquete nfs debe estar instalado, como son dos, indico ambos paquetes.
	package { 'paquete_nfs_utils': #Este es el titulo del recurso, es el que aparecera en los LOGs
		ensure => installed, #aca le indico que quiero que el recurso este instalado
		name => "nfs-utils", #indico el nombre del paquete	
	}

	#Ejecuto el comandod de activacion del servicio
	exec{'enable_servicio_rpcbind' :
		command => '/usr/bin/systemctl enable rpcbind', #Este es el comando que deseo que se ejecute, en este caso, activa el servicio
		cwd => "/", #indico desde que directorio se ejecuta el comando
		require => Package['paquete_nfs_utils'],#Antes de activar el servicio, los paquetes deben estar instalados.
	}

	#Ejecuto el comandod de activacion del servicio
	exec{'enable_servicio_nfs_server' :
		command => '/usr/bin/systemctl enable nfs-server', #Este es el comando que deseo que se ejecute, en este caso, activa el servicio
		cwd => "/", #indico desde que directorio se ejecuta el comando
		require => Package['paquete_nfs_utils'],#Antes de activar el servicio, los paquetes deben estar instalados.
	}

	#aca creo el directorio nfs que es el que compartire
	file {'directorioNFS':#Titulo del recurso
		ensure => directory, #indico que es un directorio
		owner => root, #indico el dueño del directorio
		mode => '0664', #indico los permisos de acceso al directorio.
		path => "/var/nfs/alumnos", #indico la ubicacion del directorio
	}

	#aca indico como quiero que sea el archivo /etc/exports
	file {'exportsNFS':#Titulo del recurso
		ensure => file, #indico que sea un archivo
		owner => root, #indico el dueño del archivo
		mode => '0644', #indico los permisos de acceso al archivo.
		path => "/etc/exports", #indico la ubicacion del archivo
		content => "/var/nfs/alumnos    192.168.122.0/24(rw,sync,no_root_squash,no_all_squash)",#indico el contenido del archivo.
	}
	
	#Ejecuto el comandod de activacion del servicio
	exec{'start_servicios_rpcbind' :
		command => '/usr/bin/systemctl start rpcbind', #Este es el comando que deseo que se ejecute, en este caso, activa el servicio
		cwd => "/", #indico desde que directorio se ejecuta el comando
		require => Package['paquete_nfs_utils'],#Antes de activar el servicio, los paquetes deben estar instalados.
	}

	#Ejecuto el comandod de activacion del servicio
	exec{'start_servicios_nfs_server' :
		command => '/usr/bin/systemctl start nfs-server', #Este es el comando que deseo que se ejecute, en este caso, activa el servicio
		cwd => "/", #indico desde que directorio se ejecuta el comando
		require => Package['paquete_nfs_utils'],#Antes de activar el servicio, los paquetes deben estar instalados.
	}

	#Ejecuto el comandod de activacion del servicio
	exec{'start_servicios_nfs_lock' :
		command => '/usr/bin/systemctl start nfs-lock', #Este es el comando que deseo que se ejecute, en este caso, activa el servicio
		cwd => "/", #indico desde que directorio se ejecuta el comando
		require => Package['paquete_nfs_utils'],#Antes de activar el servicio, los paquetes deben estar instalados.
	}

	#Ejecuto el comandod de activacion del servicio
	exec{'start_servicios_nfs_idmap' :
		command => '/usr/bin/systemctl start nfs-idmap', #Este es el comando que deseo que se ejecute, en este caso, activa el servicio
		cwd => "/", #indico desde que directorio se ejecuta el comando
		require => Package['paquete_nfs_utils'],#Antes de activar el servicio, los paquetes deben estar instalados.
	}

	#Ejecuto el comandod de activacion del servicio
	exec{'ejecuto_exportfs' :
		command => "/usr/sbin/exportfs -a", #Este es el comando que deseo que se ejecute, en este caso, activa el servicio
		cwd => "/usr/sbin/", #indico desde que directorio se ejecuta el comando
		require => Package['paquete_nfs_utils'],#Antes de activar el servicio, los paquetes deben estar instalados.
	}
}

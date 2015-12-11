class nfs::client::complete()
{
	#Aca indico que el paquete nfs debe estar instalado, como son dos, indico ambos paquetes.
	package { 'paquete_nfs_utils': #Este es el titulo del recurso, es el que aparecera en los LOGs
		ensure => installed, #aca le indico que quiero que el recurso este instalado
		name => "nfs-utils", #indico el nombre del paquete	
	}

	package { 'paquete_nfs_utils_lib': #Este es el titulo del recurso, es el que aparecera en los LOGs
		ensure => installed, #aca le indico que quiero que el recurso este instalado
		name => "nfs-utils-lib", #indico el nombre del paquete	
	}

	#aca creo el directorio nfs que es donde monatare el compartido.
	file {'directorioNFS':#Titulo del recurso
		ensure => directory, #indico que es un directorio
		owner => root, #indico el dueño del directorio
		mode => 0777, #indico los permisos de acceso al directorio.
		path => "/media/nfs", #indico la ubicacion del directorio
	}

	#Ejecuto el comandod de activacion del servicio
	exec{'ejecuto_exportfs' :
		command => "/bin/mount 192.168.1.105:/root/nfs /mnt/nfs/", #Este es el comando que deseo que se ejecute, monto la carpeta
		cwd => "/", #indico desde que directorio se ejecuta el comando
		require => Package['paquete_nfs_utils','paquete_nfs_utils_lib'],#Antes de activar el servicio, los paquetes deben estar instalados.
	}

}

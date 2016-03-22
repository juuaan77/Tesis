class nfs::client(
#Duenio del direcotrio donde se montara el sistema nfs
$duenio = "alumno",
#Ip donde busco el nfs
$nfs_ip = "192.168.122.1"
)
{
	#Aca indico que el paquete nfs debe estar instalado, como son dos, indico ambos paquetes.
	package { 'paquete_nfs_common': #Este es el titulo del recurso, es el que aparecera en los LOGs
		ensure => installed, #aca le indico que quiero que el recurso este instalado
		name => "nfs_common", #indico el nombre del paquete	
	}

	#aca creo el directorio donde montare el nfs
	file {'directorioNFS':#Titulo del recurso
		ensure => directory, #indico que es un directorio
		owner => $duenio, #indico el dueño del directorio
		mode => '0664', #indico los permisos de acceso al directorio.
		path => "/mnt/nfs", #indico la ubicacion del directorio
	}
		
	#Monto el direcotrio nfs
	exec{'monto_nfs' :
		command => "/bin/mount -t nfs ${nfs_ip}:/var/nfs/alumnos /mnt/nfs/",
		cwd => "/", #indico desde que directorio se ejecuta el comando
		#require => Package['paquete_nfs_utils'],#Antes de activar el servicio, los paquetes deben estar instalados.
		require => File['directorioNFS'],
	}
}

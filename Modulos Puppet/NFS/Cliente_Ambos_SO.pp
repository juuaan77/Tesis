class nfs::client(
#Duenio del direcotrio donde se montara el sistema nfs
$duenio = "alumno",
#Ip donde busco el nfs
$nfs_ip = "192.168.122.1"
)
{
	if ${osfamily} == "Debian"
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
	elsif ${osfamily} == "redhat"
	{
		#Aca indico que el paquete nfs debe estar instalado, como son dos, indico ambos paquetes.
		package { 'paquete_nfs_utils': #Este es el titulo del recurso, es el que aparecera en los LOGs
			ensure => installed, #aca le indico que quiero que el recurso este instalado
			name => "nfs-utils", #indico el nombre del paquete	
		}

		#aca creo el directorio donde montare el nfs
		file {'directorioNFS':#Titulo del recurso
			ensure => directory, #indico que es un directorio
			owner => $duenio, #indico el dueño del directorio
			mode => '0664', #indico los permisos de acceso al directorio.
			path => "/mnt/nfs", #indico la ubicacion del directorio
		}
	
		#Ejecuto el comandod de activacion del servicio
		exec{'enable_servicio_rpcbind' :
			command => '/usr/bin/systemctl enable rpcbind', #Este es el comando que deseo que se ejecute, en este caso, activa el servicio
			cwd => "/", #indico desde que directorio se ejecuta el comando
			require => Package['paquete_nfs_utils'],#Antes de activar el servicio, los paquetes deben estar instalados.
		}

		exec{'enable_servicio_nfs_server' :
			command => '/usr/bin/systemctl enable nfs-server', #Este es el comando que deseo que se ejecute, en este caso, activa el servicio
			cwd => "/", #indico desde que directorio se ejecuta el comando
			require => Package['paquete_nfs_utils'],#Antes de activar el servicio, los paquetes deben estar instalados.
		}

		#Inicio los servicios
		exec{'start_servicios_rpcbind' :
			command => '/usr/bin/systemctl start rpcbind', #Este es el comando que deseo que se ejecute, en este caso, activa el servicio
			cwd => "/", #indico desde que directorio se ejecuta el comando
			require => Package['paquete_nfs_utils'],#Antes de activar el servicio, los paquetes deben estar instalados.
		}

		exec{'start_servicios_nfs_server' :
			command => '/usr/bin/systemctl start nfs-server', #Este es el comando que deseo que se ejecute, en este caso, activa el servicio
			cwd => "/", #indico desde que directorio se ejecuta el comando
			require => Package['paquete_nfs_utils'],#Antes de activar el servicio, los paquetes deben estar instalados.
		}

		exec{'start_servicios_nfs_lock' :
			command => '/usr/bin/systemctl start nfs-lock', #Este es el comando que deseo que se ejecute, en este caso, activa el servicio
			cwd => "/", #indico desde que directorio se ejecuta el comando
			require => Package['paquete_nfs_utils'],#Antes de activar el servicio, los paquetes deben estar instalados.
		}

		exec{'start_servicios_nfs_idmap' :
			command => '/usr/bin/systemctl start nfs-idmap', #Este es el comando que deseo que se ejecute, en este caso, activa el servicio
			cwd => "/", #indico desde que directorio se ejecuta el comando
			require => Package['paquete_nfs_utils'],#Antes de activar el servicio, los paquetes deben estar instalados.
		}

	
		#Monto el direcotrio nfs
		exec{'monto_nfs' :
			command => "/usr/bin/mount -t nfs ${nfs_ip}:/var/nfs/alumnos /mnt/nfs/",
			cwd => "/", #indico desde que directorio se ejecuta el comando
			#require => Package['paquete_nfs_utils'],#Antes de activar el servicio, los paquetes deben estar instalados.
			require => File['directorioNFS'],
		}
	}
}

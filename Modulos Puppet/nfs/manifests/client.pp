#Instala y confugura un cliente nfs que toma 2 parametros
#dueio -> Es el duenio de la carpeta /mnt donde so montara el sistema nfs
#nfs_ip -> IP del servidor nfs al cual se conecta el cliente.
class nfs::client(
#Duenio del direcotrio donde se montara el sistema nfs
$duenio = "root",
#Ip donde busco el nfs
$nfs_ip = "192.168.122.1"
)
{
	if $osfamily == "Debian"
	{
		#Obtengo los .deb para evitar usar internet
		exec{'descarga_nfs' :
                	command => "/usr/bin/curl ftp://192.168.122.1/proyectointegrador/Ubuntu14/nfs.tar -o /var/cache/apt/archives/nfs.tar", #Este es el comando que deseo que se ejecute
                	cwd => "/", #indico desde que directorio se ejecuta el comando
                	unless => "/bin/ls /var/cache/apt/archives/nfs.tar",
	        }

		#Desempaqueto los .deb
        	exec{'desempaqueta_nfs' :
                	command => "/bin/tar -xvf /var/cache/apt/archives/nfs.tar -C /var/cache/apt/archives/", #Este es el comando que deseo que se ejecute
                	cwd => "/", #indico desde que directorio se ejecuta el comando
                	require => Exec['descarga_nfs'],#Requiere este recurso
                	unless => '/bin/grep "desempaqueta_nfs]/returns) executed successfully" /var/log/syslog',
        	}

		#Aca indico que el paquete nfs debe estar instalado.
		package { 'paquete_nfs_common': #Este es el titulo del recurso, es el que aparecera en los LOGs
			ensure => installed, #aca le indico que quiero que el recurso este instalado
			name => "nfs-common", #indico el nombre del paquete
			require => Exec['desempaqueta_nfs'],	
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
			require => File['directorioNFS'],
			unless => "/bin/ls /mnt/nfs/*",
		}
	}
	elsif $osfamily == "RedHat"
	{
		#Aca indico que el paquete nfs debe estar instalado.
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
			unless => '/bin/systemctl status puppet | /bin/grep "enable_servicio_rpcbind]/returns) executed successfully"',
		}

		exec{'enable_servicio_nfs_server' :
			command => '/usr/bin/systemctl enable nfs-server', #Este es el comando que deseo que se ejecute, en este caso, activa el servicio
			cwd => "/", #indico desde que directorio se ejecuta el comando
			require => Package['paquete_nfs_utils'],#Antes de activar el servicio, los paquetes deben estar instalados.
			unless => '/bin/systemctl status puppet | /bin/grep "enable_servicio_nfs_server]/returns) executed successfully"',
		}

		#Inicio los servicios
		exec{'start_servicios_rpcbind' :
			command => '/usr/bin/systemctl start rpcbind', #Este es el comando que deseo que se ejecute, en este caso, activa el servicio
			cwd => "/", #indico desde que directorio se ejecuta el comando
			require => Package['paquete_nfs_utils'],#Antes de activar el servicio, los paquetes deben estar instalados.
			unless => '/bin/systemctl status puppet | /bin/grep "start_servicios_rpcbind]/returns) executed successfully"',
		}

		exec{'start_servicios_nfs_server' :
			command => '/usr/bin/systemctl start nfs-server', #Este es el comando que deseo que se ejecute, en este caso, activa el servicio
			cwd => "/", #indico desde que directorio se ejecuta el comando
			require => Package['paquete_nfs_utils'],#Antes de activar el servicio, los paquetes deben estar instalados.
			unless => '/bin/systemctl status puppet | /bin/grep "start_servicios_nfs_utils]/returns) executed successfully"',
		}

		exec{'start_servicios_nfs_lock' :
			command => '/usr/bin/systemctl start nfs-lock', #Este es el comando que deseo que se ejecute, en este caso, activa el servicio
			cwd => "/", #indico desde que directorio se ejecuta el comando
			require => Package['paquete_nfs_utils'],#Antes de activar el servicio, los paquetes deben estar instalados.
			unless => '/bin/systemctl status puppet | /bin/grep "start_servicios_nfs_lock]/returns) executed successfully"',
		}

		exec{'start_servicios_nfs_idmap' :
			command => '/usr/bin/systemctl start nfs-idmap', #Este es el comando que deseo que se ejecute, en este caso, activa el servicio
			cwd => "/", #indico desde que directorio se ejecuta el comando
			require => Package['paquete_nfs_utils'],#Antes de activar el servicio, los paquetes deben estar instalados.
			unless => '/bin/systemctl status puppet | /bin/grep "start_servicios_nfs_idmap]/returns) executed successfully"',
		}

	
		#Monto el direcotrio nfs
		exec{'monto_nfs' :
			command => "/usr/bin/mount -t nfs ${nfs_ip}:/var/nfs/alumnos /mnt/nfs/",
			cwd => "/", #indico desde que directorio se ejecuta el comando
			#require => Package['paquete_nfs_utils'],#Antes de activar el servicio, los paquetes deben estar instalados.
			require => File['directorioNFS'],
			unless => "/bin/ls /mnt/nfs/*",
		}
	}
}

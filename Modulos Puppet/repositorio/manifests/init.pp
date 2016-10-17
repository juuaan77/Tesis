#Clase que instala y configura un repositorio hubicado en el servidor Cobbler
class repositorio()
{
	if $osfamily == "RedHat"
	{
		#aca indico como quiero que sea el archivo del repositorio
		file {'proyectointegrador_repo':#Titulo del recurso
			ensure => file, #indico que sea un archivo
			owner => root, #indico el dueño del archivo
			mode => '0644', #indico los permisos de acceso al archivo.
			source => "puppet:///modules/repositorio/proyectointegrador.repo",
			path => "/etc/yum.repos.d/proyectointegrador.repo", #indico la ubicacion del archivo
		}

		#Aca indico que el paquete debe estar instalado para poder incluir priridades en los repositorios, entregando la maxima al local.
		package { 'paquete_yum_priorities': #Este es el titulo del recurso, es el que aparecera en los LOGs
			ensure => installed, #aca le indico que quiero que el recurso este instalado
			name => "yum-priorities", #indico el nombre del paquete	
		}	

		#Aca indico que el paquete debe estar instalado para habilitar facilmente el repositorio
		package { 'paquete_yum_utils': #Este es el titulo del recurso, es el que aparecera en los LOGs
			ensure => installed, #aca le indico que quiero que el recurso este instalado
			name => "yum-utils", #indico el nombre del paquete	
		}	
	
		#Ejecuto el comandod que habilita el repositorio.
		exec{'enablerepo' :
			command => "/bin/yum-config-manager  --enable proyectointegrador", #Este es el comando que deseo que se ejecute, en este caso, activa el servicio
			cwd => "/", #indico desde que directorio se ejecuta el comando
			require => [File['proyectointegrador_repo'],Package['paquete_yum_utils']],#Antes de activar el repo, el archivo de configuracion de este debe encontrarse en el direcotiro adecuado
			unless => '/bin/systemctl status puppet | /bin/grep "enablerepo]/returns) executed successfully"',
		}
	}
}

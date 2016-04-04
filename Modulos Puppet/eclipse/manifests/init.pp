#Esta clase actualiza los paquetes una vez al mes.
class eclipse()
{
	if $osfamily == "Debian"
	{
		#Indico el paquete necesario a instalar.
		package { 'paquete_java_ubuntu': #Este es el titulo del recurso, es el que aparecera en los LOGs
			ensure => installed, #aca le indico que quiero que el recurso este instalado
			name => "openjdk-7-jdk", #indico el nombre del paquete	
		}

		#Obtengo el instalador de eclipse.
		exec{'descarga_eclipse_ubuntu' :
			command => "/usr/bin/curl ftp://192.168.122.1/ides/eclipse-cpp-mars-2-linux-gtk-x86_64.tar.gz -o /opt/eclipse-cpp-mars-2-linux-gtk-x86_64.tar.gz", #Este es el comando que deseo que se ejecute, descargo desde el servidor el instalador del pycharm.
			cwd => "/", #indico desde que directorio se ejecuta el comando
			require => Package['paquete_java_ubuntu'],#Requiere este recurso
			refreshonly => true,
		}
		
		#Descomprimo el instalador
		exec{'descomprimo_eclipse_ubuntu' :
			command => "/bin/tar -vzxf /opt/eclipse-cpp-mars-2-linux-gtk-x86_64.tar.gz -C /opt", 
			cwd => "/", #indico desde que directorio se ejecuta el comando
			require => Exec['descarga_eclipse_ubuntu'],#Requiere este recurso
			refreshonly => true,
		}

		#Descomprimo el instalador
		exec{'genero_enlace' :
			command => "/bin/ln -s /opt/eclipse/eclipse /usr/local/bin/eclipse",
			cwd => "/", #indico desde que directorio se ejecuta el comando
			require => Exec['descomprimo_eclipse_ubuntu'],#Requiere este recurso
			refreshonly => true,
		}

		#Creo el icono desktop
		file {'icono_desktop_eclipse_ubuntu':#Titulo del recurso
			ensure => file, #indico que sea un archivo
			owner => root, #indico el dueño del archivo
			mode => '0644', #indico los permisos de acceso al archivo.
			source => "puppet:///modules/eclipse/eclipse.desktop.ubuntu",
			path => "/usr/share/applications/eclipse.desktop", #indico la ubicacion del archivo
		}

		#Descomprimo el instalador
		exec{'intalo_desktop_ubuntu' :
			command => "/usr/bin/desktop-file-install /usr/share/applications/eclipse.desktop",
			cwd => "/", #indico desde que directorio se ejecuta el comando
			require => File['icono_desktop_eclipse_ubuntu'],#Requiere este recurso
			refreshonly => true,
		}
	}
	elsif $osfamily == "RedHat"
	{
		#Indico el paquete necesario a instalar.
		package { 'paquete_java': #Este es el titulo del recurso, es el que aparecera en los LOGs
			ensure => installed, #aca le indico que quiero que el recurso este instalado
			name => "java", #indico el nombre del paquete	
		}
		
		#Obtengo el instalador de eclipse.
		exec{'descarga_eclipse' :
			command => "/usr/bin/curl ftp://192.168.122.1/ides/eclipse-cpp-mars-2-linux-gtk-x86_64.tar.gz -o /opt/eclipse-cpp-mars-2-linux-gtk-x86_64.tar.gz", #Este es el comando que deseo que se ejecute, descargo desde el servidor el instalador del pycharm.
			cwd => "/", #indico desde que directorio se ejecuta el comando
			require => Package['paquete_java'],#Requiere este recurso
			refreshonly => true,
		}
		
		#Descomprimo el instalador
		exec{'descomprimo_eclipse' :
			command => "/usr/bin/tar -vzxf /opt/eclipse-cpp-mars-2-linux-gtk-x86_64.tar.gz -C /opt", 
			cwd => "/", #indico desde que directorio se ejecuta el comando
			require => Exec['descarga_eclipse'],#Requiere este recurso
		}

		#Descomprimo el instalador
		exec{'genero_enlace' :
			command => "/usr/bin/ln -s /opt/eclipse/eclipse /usr/bin/eclipse",
			cwd => "/", #indico desde que directorio se ejecuta el comando
			require => Exec['descomprimo_eclipse'],#Requiere este recurso
			refreshonly => true,
		}

		#Creo el icono desktop
		file {'icono_desktop_eclipse':#Titulo del recurso
			ensure => file, #indico que sea un archivo
			owner => root, #indico el dueño del archivo
			mode => '0644', #indico los permisos de acceso al archivo.
			source => "puppet:///modules/eclipse/eclipse.desktop.centos",
			path => "/usr/share/applications/eclipse.desktop", #indico la ubicacion del archivo
		}

	}
}

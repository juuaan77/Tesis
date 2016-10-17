#Esta clase instala la IDE eclipse para el lenguaje C
class eclipse()
{
	if $osfamily == "Debian"
	{
		#Requiere de que este instalada la interfaz grafica.
		include ubuntugui 
		
		#Obtengo los paquetes .deb esto es hecho para evitar descargar cosas de internet
		exec{'descargo_java':
			command => "/usr/bin/curl ftp://192.168.122.1/proyectointegrador/Ubuntu14/eclipse.tar -o /var/cache/apt/archives/eclipse.tar", #Este es el comando que deseo que se ejecute.
			cwd => "/", #indico desde que directorio se ejecuta el comando
                        unless => "/bin/ls /var/cache/apt/archives/eclipse.tar"

		}

		#Descomprimo el archivo con los .deb de java.
		exec{'descomprimo_java':
                        command => "/bin/tar -xvf /var/cache/apt/archives/eclipse.tar -C /var/cache/apt/archives/",
                        cwd => "/", #indico desde que directorio se ejecuta el comando
                        require => Exec['descargo_java'],#Requiere este recurso
			unless => '/bin/grep "descomprimo_java]/returns) executed successfully" /var/log/syslog',
		}

		#Indico el paquete necesario a instalar.
		package { 'paquete_java_ubuntu': #Este es el titulo del recurso, es el que aparecera en los LOGs
			ensure => installed, #aca le indico que quiero que el recurso este instalado
			name => "openjdk-7-jdk", #indico el nombre del paquete
			require => Exec['descomprimo_java'],#Requiere este recurso	
		}

		#Obtengo el instalador de eclipse.
		exec{'descarga_eclipse_ubuntu' :
			command => "/usr/bin/curl ftp://192.168.122.1/ides/eclipse-cpp-mars-2-linux-gtk-x86_64.tar.gz -o /opt/eclipse-cpp-mars-2-linux-gtk-x86_64.tar.gz", #Este es el comando que deseo que se ejecute, descargo desde el servidor el instalador del pycharm.
			cwd => "/", #indico desde que directorio se ejecuta el comando
			require => Package['paquete_java_ubuntu'],#Requiere este recurso
			unless => "/bin/ls /opt/eclipse-cpp-mars-2-linux-gtk-x86_64.tar.gz",
		}
		
		#Descomprimo el instalador
		exec{'descomprimo_eclipse_ubuntu' :
			command => "/bin/tar -vzxf /opt/eclipse-cpp-mars-2-linux-gtk-x86_64.tar.gz -C /opt", 
			cwd => "/", #indico desde que directorio se ejecuta el comando
			require => Exec['descarga_eclipse_ubuntu'],#Requiere este recurso
			unless => "/bin/ls /opt/eclipse",
		}

		#Genero un enlace simbolico que me permite ejecutar eclipse desde la terminal
		exec{'genero_enlace' :
			command => "/bin/ln -s /opt/eclipse/eclipse /usr/local/bin/eclipse",
			cwd => "/", #indico desde que directorio se ejecuta el comando
			require => Exec['descomprimo_eclipse_ubuntu'],#Requiere este recurso
			unless => "/bin/ls /usr/local/bin/eclipse",
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
			unless => "/bin/ls /usr/share/applications/eclipse.desktop",
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
			command => "/usr/bin/curl ftp://192.168.122.1/ides/eclipse-cpp-mars-2-linux-gtk-x86_64.tar.gz -o /opt/eclipse-cpp-mars-2-linux-gtk-x86_64.tar.gz", #Este es el comando que deseo que se ejecute.
			cwd => "/", #indico desde que directorio se ejecuta el comando
			require => Package['paquete_java'],#Requiere este recurso
			unless => "/bin/ls /opt/eclipse-cpp-mars-2-linux-gtk-x86_64.tar.gz",
		}
		
		#Descomprimo el instalador
		exec{'descomprimo_eclipse' :
			command => "/usr/bin/tar -vzxf /opt/eclipse-cpp-mars-2-linux-gtk-x86_64.tar.gz -C /opt", 
			cwd => "/", #indico desde que directorio se ejecuta el comando
			require => Exec['descarga_eclipse'],#Requiere este recurso
			unless => "/bin/ls /opt/eclipse",
		}

		#Genero un enlace simbolico que me permite ejecutar la app desde la consola
		exec{'genero_enlace' :
			command => "/usr/bin/ln -s /opt/eclipse/eclipse /usr/bin/eclipse",
			cwd => "/", #indico desde que directorio se ejecuta el comando
			require => Exec['descomprimo_eclipse'],#Requiere este recurso
			unless => "/bin/ls /usr/bin/eclipse",
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

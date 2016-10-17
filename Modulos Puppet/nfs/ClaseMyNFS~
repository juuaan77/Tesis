class mynfs()
{

#Package['MyNFS'] -> File['exportsNFS'] -> File['directorioNFS'] ~>
#Service['SerivcioNFS']

	#Aca indico que el paquete nfs debe estar instalado
	package { 'MyNFS': #Este es el titulo del recurso, es el que aparecera en los LOGs
		ensure => installed, #aca le indico que quiero que el recurso este instalado
		name => "nfs-utils" #indico el nombre del paquete	
	}

	#aca creo el directorio nfs que es el que compartire
	file {'directorioNFS':#Titulo del recurso
		ensure => directory, #indico que es un directorio
		owner => root, #indico el dueño del directorio
		mode => 0777, #indico los permisos de acceso al directorio.
		path => "/root/nfs", #indico la ubicacion del directorio
	}

	#aca indico como quiero que sea el archivo /etc/exports
	file {'exportsNFS':#Titulo del recurso
		ensure => file, #indico que sea un archivo
		owner => root, #indico el dueño del archivo
		mode => 0777, #indico los permisos de acceso al archivo.
		path => "/etc/exports", #indico la ubicacion del archivo
		content => "/root/nfs    192.168.122.1(rw,sync,no_root_squash,no_all_squash)",#indico el contenido del archivo.
	}

	#aca defino el servicio
	service{'SerivcioNFS':#Titulo del servicio
		ensure => running, #Indico que el servicio debe estar corriendo.
		name => "nfs-server",#Este es el nombre con que cetos reconoce al servicio.
		before => Package['MyNFS'],#Indico que antes de iniciar el servicio, debe asegurarse que este instalado.
		subscribe => File['exportsNFS'], #Indico que si el archivo exports cambia, se debe refrescar.
	}
}

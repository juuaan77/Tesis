#Clase que creara un usuario sin permisos.
#usuario -> nombre del usuario creado
class usuarios(
$usuario = "alumno"
)
{
	#Aca indico los datos del usuario a crear.
	user { 'creo_usuario': #Este es el titulo del recurso, es el que aparecera en los LOGs
		name => $usuario, #El usuario sera alumno.
		ensure => 'present', #Debe encontrase presente.
		password  => '$1$t059HC0X$N/J0Km9dJQEGmwSnjDrW0/', #para encriptar la clave deseada, se usa "openssl passwd -1", esta es "alumno"
		password_max_age => '99999', #numero de dias maximo que es valida la clave
  		password_min_age => '0', #numero de dias minimo que es valida la clave
		allowdupe => 'false', #No permito usuarios duplicados.
		expiry => 'absent', #El usuario no debe expirar.
		home => '/home/${usuario}' #El home del usuario
	}
	
	#Aca creo el grupo al que pertenecera el usuario.
	group { 'grupo_usuario': #Titulo del recurso, aparece en los LOGs
		name => $usuario, #nombre del grupo
		ensure => 'present', #Debe encontrase presente.
		allowdupe => 'false', #No permito grupos duplicados.
		members => $usuario, #mimbros del grupo 
		require => User['creo_usuario'],#Antes de crear el grupo del usuario, este debe existit
	}

	#Creo el directorio de usuario ALUMNO
	file { 'home_usuario': #Titulo del recurso, aparece en los LOGs
		path => '/home/${usuario}', #path del directorio.
		ensure => 'directory', #Indico que sea un directorio.
		mode => '0644', #Indico permisos del directorio
		owner => 'alumno', #dueño del directorio
		group => 'alumno', #grupo del directorio
		require => Group['grupo_usuario'],#Antes de crear el home del usuario, este debe existit
	}
}

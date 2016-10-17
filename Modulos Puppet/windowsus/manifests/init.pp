#Clase que creara un usuario sin permisos.
#usuario -> nombre del usuario creado
class windowsus(
$usuario = "alumno"
)
{
	#Aca indico los datos del usuario a crear.
	user { 'creo_usuario': #Este es el titulo del recurso, es el que aparecera en los LOGs
		name => 'alumno', #El usuario sera alumno.
		ensure => present, #Debe encontrase presente.
		groups    => ['Users'],
		managehome => true,
		password  => 'alumno', #En windows la clave debe estar en texto plano.
	}
}

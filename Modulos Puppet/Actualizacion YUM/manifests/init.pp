#Esta clase actualiza los paquetes una vez al mes.
class actualiza_repos()
{
	#A travez de un recurso CRON me aseguro que sea una vez al mes.
	cron { 'cron_repos':#Nombre del recurso
		name => 'cron_repos', #nombre simbolico del recurso.
		ensure => present, #El recurso debe estar presente.
		command => 'date >> /root/fecha', #Comando a ejecutar
		minute => '*/10', #que ejecute cada minuto 1 de cada hora.		
		#command => 'yum update -y',  #comando a ejecutar
		#monthday => '1', #Ejecuto el comando el primero de cada mes.
		user => 'root', #El dueño del cron
	}
}

#Esta clase actualiza los paquetes una vez al mes.
class update()
{
	if $osfamily == "Debian"
	{
		#A travez de un recurso CRON me aseguro que sea una vez al mes.
		cron { 'cron_repos':#Nombre del recurso
			name => 'cron_repos', #nombre simbolico del recurso.
			ensure => present, #El recurso debe estar presente.
			command => 'date >> /root/fecha', #Comando a ejecutar
			minute => '*/10', #que ejecute cada minuto 1 de cada hora.		
			#command => 'apt-get -y update && apt-get -y upgrade',  #comando a ejecutar
			#monthday => '1', #Ejecuto el comando el primero de cada mes.
			user => 'root', #El dueño del cron
		}
	}
	elsif $osfamily == "RedHat"
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
}

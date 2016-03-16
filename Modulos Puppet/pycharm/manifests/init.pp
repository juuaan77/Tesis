class repositorio()
{
	#Obtengo el instalador del pycharm.
	exec{'descarga_pycharm' :
		command => "curl ftp://192.168.122.1/ides/pycharm-community-5.0.4.tar.gz -o /var/lib/pycharm-community-5.0.4.tar.gz
", #Este es el comando que deseo que se ejecute, descargo desde el servidor el instalador del pycharm.
		cwd => "/", #indico desde que directorio se ejecuta el comando
	}

	#Descomprimo el instalador
	exec{'descarga_pycharm' :
		command => "tar -vzxf /var/lib/pycharm-community-5.0.4.tar.gz", 
		cwd => "/", #indico desde que directorio se ejecuta el comando
	}

	#Descomprimo el instalador
	exec{'descarga_pycharm' :
		command => "tar -vzxf /var/lib/pycharm-community-5.0.4.tar.gz", 
		cwd => "/", #indico desde que directorio se ejecuta el comando
	}

	#Instalo el pycharm
	exec{'descarga_pycharm' :
		command => "/var/lib/pycharm-community-5.0.4/bin/pycharm.sh", 
		cwd => "/", #indico desde que directorio se ejecuta el comando
	}
}

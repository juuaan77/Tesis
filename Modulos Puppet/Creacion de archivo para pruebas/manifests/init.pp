class modulo()
{
	#aca indico como quiero que sea el archivo /etc/exports
        file {'modulo':#Titulo del recurso
                ensure => 'file', #indico que sea un archivo
                owner => 'root', #indico el dueño del archivo
                mode => '0777', #indico los permisos de acceso al archivo.
                path => "/tmp/modulo", #indico la ubicacion del archivo
                content => $hostname,#indico el contenido del archivo.
        }

        exec{'exec_prueba':
                command =>'/bin/echo "date" >> /root/fecha', #Este es el comando que deseo que se ejecute
                cwd => "/", #indico desde que directorio se ejecuta el comando
                unless => "/bin/ls /root/stop"
        }

}

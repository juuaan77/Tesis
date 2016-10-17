#Instala la IDE idle para python.
class windows_eclipse()
{
	file {'Descarga_eclipse_windows':#Titulo del recurso
        	ensure => present, #indico que sea un archivo
        	mode => '0777', #indico los permisos de acceso al archivo.
        	path => "C:\Users\windows\puppet\eclipse-cpp-mars-2-win32-x86_64.zip", #indico la ubicacion del archivo
		source => 'puppet:///modules/windows_eclipse/eclipse-cpp-mars-2-win32-x86_64.zip/'
        }
	
	file {'Archivo_descomprimo_eclipse_windows':
		ensure => present,
		mode => '0777',
		path => "C:\Users\windows\puppet\descomprime_eclipse.bat",
		source => 'puppet:///modules/windows_eclipse/descomprime_eclipse.bat',
	}
	
	#Descomprimo el eclipse
	exec{'Descomprimo_eclipse_windows':
		command => 'C:\Users\windows\puppet\descomprime_eclipse.bat',
		require => File['Archivo_descomprimo_eclipse_windows','Descarga_eclipse_windows'],#Requiere este recurso
		logoutput => true,
	}
}

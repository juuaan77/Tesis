node /alumno*/ {
	
	#include modulo
	#include nfs::client
	#include nfs::server
	#include usuarios
	#include repositorio
	#include update	
}

node /ubuntu*/ {
	include modulo
	include usuarios
	include nfs::client
	include ubuntugui
	include idle
	#include update
	include eclipse
	#include nfs::server
}

node /gui*/ {
	#include usuarios
	#include nfs::client
	#include repositorio
	#include update
	#include idle
	#include eclipse
	#include modulo
}

node default{
	include modulo
}

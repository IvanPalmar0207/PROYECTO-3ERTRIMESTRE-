from tb_serviciosAdicionales import *

class mesero:
    
    def __init__(self,documento,nombre,email,direccion,telefono):
        self.documento = documento
        self.nombre = nombre
        self.email = email
        self.direccion = direccion
        self.telefono = telefono
        
    def consultar_servicios(self,conexion):
        print('CONSULTAR SERVICIOS')
        print()
        consultar=select_ServiciosAdicionales(conexion)
        for i in consultar:
            print(i)
        print()

    def agregar_servicios(self,conexion):
        print('AGREGAR SERVICIOS')
        print()
        TipoSer=input('¿Cual es el servicio que vas a agregar (mesero)?\n-')
        preSer=int(input('¿Cual es el precio del nuevo servicio agregado (mesero)?\n-'))
        agregar=Insert_tbServiciosAdicionales(conexion, TipoSer, preSer)
        consultar=select_ServiciosAdicionales(conexion)
        for i in consultar:
            print(i)
        print()
        
#Ejemplo   
#n1=mesero(1231231, 'Juan', 'Juan@gmail.com', 'A la izquierda', 3123213)
#n1.consultar_servicios(proyecto)
#n1.agregar_servicios(proyecto)        
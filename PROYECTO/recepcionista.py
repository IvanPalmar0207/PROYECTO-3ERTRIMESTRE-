from tb_facturacion import *
from tb_reserva import *

class recepcionista:
    def __init__(self,documento,nombre,email,telefono,direccion):
        self.documento = documento
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.direccion = direccion
    
    def consultar_reserva(self,conexion):
        print('CONSULTAR RESERVAS')
        d1=int(input('¿Cual es tu documento?\n-'))
        consulta=consultarReservaUsuario(conexion, d1)
        print('Tus reservas son:')
        for i in consulta:
            print(i)
        print()
    
    def crearReserva(self,conexion):
        print('CREAR RESERVA')
        print()
        print('Datos de la nueva reserva')
        d1=input('¿Cual es la fecha de llegada de la nueva reserva?\n-')
        d2=input('¿Cual es la fecha de salida de la nueva reserva?\n-')
        d3=int(input('¿Cual es el valor total de la nueva reserva?\n-'))
        d4=int(input('¿Cual es el documento del cliente de la nueva reserva?\n-'))
        crear=insertar_Reserva(conexion, d1, d2, d3, d4)
        print()
        consulta=consultarReservaUsuario(conexion, d4)
        for i in consulta:
            print(i)
        print()
        
    def actualizarReserva(self,conexion):
        print('ACTUALIZAR RESERVA')
        print()
        c1=int(input('¿Cual es el id de la reserva que deseas actualizar?\n-'))
        print('Los campos actualizables son: \nFechaLlegada_res \nFechaSalida_res \nId_usu\n')
        val2=input('¿Cual es el campo de la reserva que deseas actualizar?\n-')
        d1=input('¿Cual es el nuevo dato?\n-')
        actualizar=actualizarReserva(conexion, val2, d1, c1)
        consulta=consultarReservar(conexion, c1)
        for i in consulta:
            print(i)
        print()
        
    def eliminar_reserva(self,conexion):
        print('ELIMINAR RESERVA')
        d1=int(input('¿Cual es el id de la reserva que deseas eliminar?\n-'))
        eliminar=eliminarReserva(conexion, d1)
        print()
        consulta=consultarReservaUsuario(conexion, d1)
        for i in consulta:
            print(i)
        print()
        
    def consultarFactura(self,conexion):
        print('CONSULTAR FACTURA')
        print()
        d1=int(input('¿Cual es el id del usuario?\n-'))
        consulta=consultarReservaUsuario(conexion, d1)
        print('Sus facturas son:')
        for i in consulta:
            print(i)
        print()

#n1=recepcionista(213123123, 'Nombre', 'nombre@gmail,com', 31312312, 'Calle 4')
#n1.crearReserva(proyecto)
#n1.consultar_reserva(proyecto)
#n1.eliminar_reserva(proyecto)
#n1.consultaFactura(proyecto)
#n1.actualizarReserva(proyecto)
from tb_reserva import *
from random import *

class cliente:
    def __init__(self,documento,nombre,correo,telefono,direccion):
        self.__id=documento
        self.__nombre=nombre
        self.__correo=correo
        self.__telefono=telefono
        self.__direccion=direccion
    
    def registro_Reserva(self,conexion):
        print('REGISTRO DE RESERVAS')
        fechall=input('¿En que fecha llegaras al hotel?\n-')
        fechasal=input('¿En que fecha saldras del hotel?\n-')
        precio=randint(500000, 10000000)
        reservaResgistro=insertar_Reserva(conexion,fechall,fechasal,precio,self.__id)
    
    def consultar_Reservas(self,conexion):
        print('CONSULTAR RESERVAS')
        print('\nTus reservas son:')
        consultarReservas=consultarReservaUsuario(conexion,self.__id)
        for i in consultarReservas:
            print(i)
        
    def actualizar_Reserva(self,conexion):
        print('HAS DECIDIDO ACTUALIZAR UNA RESERVA\n')
        idres=input('¿Cual es el id de la reserva que deseas actualizar?\n-')
        print('\nCampos que pueden ser actualizados:\n-FechaLlegada_res, FechaSalida_res, Id_usu\n')
        campoact=input('¿Cual es el campo que deseas actualizar?\n-')
        if campoact=='ValorTotal_res':
            print('No se puede hacer la actualizacion de ese dato, ya que eres un cliente')
        else:
            valu1=input('\n¿Cual es el dato que deseas actualizar?\n-')
            actualizar__Reserva=actualizarReserva(conexion,campoact,valu1,idres)
    
    def cancelar_Reserva(self,conexion):
        print('ELIMINACION DE RESERVAS\n')
        print('Tus reservas son:')
        consultarReservas=consultarReservaUsuario(conexion,self.__id)
        for i in consultarReservas:
            print(i)
        eliminar=int(input('¿Cual es el id de la reserva deseas eliminar? (Si no tienes o no deseas cancelar reservas digita cero)\n-'))
        for h in consultarReservas:
            if eliminar in h:
                elimi1=eliminarReserva(conexion,eliminar)
                break
            else:
                print('No tienes la reserva que ibas a cancelar o no deseas cancelar reservas.')
                break

#Ejemplo   
#n1=cliente(595950, 'Goku', 'jdjajda@gmail.com', 23123123, 'Calle 1')
#n1.consultar_Reservas(proyecto)
#n1.cancelar_Reserva(proyecto)
#n1.actualizar_Reserva(proyecto)
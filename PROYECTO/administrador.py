from tb_habitacion import *
from tb_serviciosAdicionales import *
from tb_usuario import *

class administrador:
    
    def __init__(self,documento,nombre,email,telefono,direccion):
        self.__documento=documento
        self.__nombre=nombre
        self.__email=email
        self.__telefono=telefono
        self.__direccion=direccion
        
    def consulHabitacion(self,conexion):
        print('CONSULTA HABITACIONES\n')
        print('Las habitaciones disponibles son:\n')
        consulta=consultarTipoHabitacion(conexion)
        for i in consulta:
            print(i)
    
    def agregarHabitacion(self,conexion):
        print('AGREGAR HABITACIONES\n')
        tipo=input('¿Cual es el tipo de habitacion que deseas agregar?\n-')
        precio=input('¿Cual es el precio de la habitacion que deseas agregar?\n-')
        insertar=insertar_tipoHabitacion(conexion, tipo, precio)
        print('Las habitaciones ahora disponibles son: ')
        consulta=consultarTipoHabitacion(conexion)
        for i in consulta:
            print(i)
            
    def actualizarHabitacion(self,conexion):
        print('ACTUALIZAR HABITACION\n')
        consulta1=consultarTipoHabitacion(conexion)
        c1=int(input('¿Cual es el id de la habitacion por actualizar?\n-'))
        for j in consulta1:
            if c1 in j:
                print('Los campos actualizables son: IdTipoHabitacion_hab, Tipo_hab, PrecioHabitacion_hab')
                campo=input('¿Cual es el campo de la habitacion que deseas actualizar?\n-')
                d1=input('¿Cual es el nuevo dato?\n-')
                actualizar=actualizarTipoHabitacion(conexion, campo, d1, c1)
        consulta=consultarTipoHabitacion(conexion)
        for i in consulta:
            print(i)
                       
    def eliminarHabitacion(self,conexion):
        print('ELIMINAR HABITACION')
        id_hab=int(input('¿Cual es el id de la habitacion que deseas eliminar?\n-'))
        eliminar=eliminarTipoHabitacion(conexion, id_hab)
        consulta=consultarTipoHabitacion(conexion)
        for i in consulta:
            print(i)

    def consultarServicios(self,conexion):
        print('CONSULTAR SERVICIOS\n')
        print('Los servicios disponibles son:\n')
        consulta=select_ServiciosAdicionales(conexion)
        for i in consulta:
            print(i)
    
    def crear_ServiciosAdicionales(self,conexion):
        print('CREAR SERVICIOS')
        tipo=input('¿Cual es el nombre del nuevo servicio?\n-')
        precio=input('¿Cual es el precio del nuevo servicio?\n-')
        crear=Insert_tbServiciosAdicionales(conexion, tipo, precio)
        print()
        consulta=select_ServiciosAdicionales(conexion)
        for i in consulta:
            print(i)
        
    def actualizar_servicio(self,conexion):
        print('ACTUALIZAR SERVICIOS')
        print()
        consulta1=select_ServiciosAdicionales(conexion)
        id=int(input('¿Cual es el id del servicio por actualizar?\n-'))
        for j in consulta1:
            if id in j:
                print('Los campos actualizables son: id_serv, TipoServicio_serv, Precio_serv')
                campo=input('¿Cual es el nombre del campo a actualizar?\n-')
                dato=input('¿Cual es el nuevo dato?\n-')
                modificacion_tbServiciosAdicionales(conexion, campo, dato, id)
        print()
        consulta=select_ServiciosAdicionales(conexion)
        for i in consulta:
            print(i)
            
    def elimiar_servicios(self,conexion):
        print('ELIMINAR SERVICIOS')
        print()
        consulta=select_ServiciosAdicionales(conexion)
        for i in consulta:
            print(i)
        print()
        id=int(input('¿Cual es el id del servicio que deseas eliminar?\n-'))
        eliminar=eliminacion_tbServiciosAdicionales(conexion, id)
        print()
        consulta1=select_ServiciosAdicionales(conexion)
        for j in consulta1:
            print(j)
        print()
    
    def consultar_empleados(self,conexion):
        print('CONSULTAR EMPLEADOS')
        print()
        print('El personal del hotel, y los clientes son:\n')
        consulta=selectAll_tbUsuario(conexion)
        for i in consulta:
            print(i)
        
    def crear_usuarios(self,conexion):
        print('CREAR USUARIOS')
        print()
        print('DATOS NUEVO USUARIO')
        print()
        print('TIPO USUARIOS\n 1.Administrador \n 2.Clientes \n 3.Recepcionista \n 4.Mesero \n 5.RoomServive\n')
        id=int(input('¿Cual es el documento del nuevo usuario?\n-'))
        nombre=input('¿Cual es el nombre del nuevo usuario?\n-')
        apellido=input('¿Cual es el apellido del nuevo usuario?\n-')
        email=input('¿Cual es el email del nuevo usuario?\n-')
        telefono=input('¿Cual es el telefono del nuevo usuario?\n-')
        direccion=input('¿Cual es la direccion del nuevo usuario?\n-')
        contraseña=input('¿Cual es la contraseña del nuevo usuario?\n-')
        fechares=input('¿Cual es la fecha de restablecimiento de contraseña del nuevo usuario?\n-')
        fecharegis=input('¿Cual es la fecha de registro del nuevo usuario?\n-')
        id_tpu=int(input('¿Que tipo de usuario es el nuevo usuario?(id)\n-'))
        crear=insert_tbUsuario(conexion, id, nombre, apellido, email, telefono, direccion, contraseña, fechares, fecharegis, id_tpu)
        consulta=selectCondition_tbUsuario(conexion,id)
        for i in consulta:
            print(i)
        print()
               
    def actualizar_usuarios(self,conexion):
        print('ACTUALIZAR USUARIOS')
        consulta1=selectAll_tbUsuario(conexion)
        id=int(input('¿Cual es el id del usuario por actualizar?\n-'))
        for j in consulta1:
            if id in j:
                print('Los campos actualizables son: \nId_usu \nNombre_usu \nApellido_usu \nEmail_usu \nTelefono_usu \nDireccion_usu \nPassword_usu \nFechaRestablecimiento_usu \nFechaRegistro_usu \nId_TpU\n')
                campo=input('¿Cual es el nombre del campo a actualizar?\n-')
                dato=input('¿Cual es el nuevo dato?\n-')        
                actualizar=update_tbUsuario(conexion, campo,dato, id)
        print()    
        consulta=selectCondition_tbUsuario(conexion,id)
        for i in consulta:
            print(i)
        print()
    
    def eliminar_usuario(self,conexion):
        print('ELIMINAR USUARIOS')
        print()
        condition=int(input('¿Cual es el id o documento del usuario que deseas eliminar?\n-'))
        eliminar=delete_tbUsuario(conexion,condition)
        print()
#Ejemplo
#n1=administrador(21312312,'Messi', 'wdqdw@gmail.com', 3123213, 'calle2')
#n1.consulHabitacion(proyecto)
#n1.agregarHabitacion(proyecto)
#n1.eliminarHabitacion(proyecto)
#n1.consultarServicios(proyecto)
#n1.crear_ServiciosAdicionales(proyecto)
#n1.actualizar_servicio(proyecto)
#n1.elimiar_servicios(proyecto)
#n1.consultar_empleados(proyecto)
#n1.crear_usuarios(proyecto)
#n1.actualizar_usuarios(proyecto)
##n1.eliminar_usuario(proyecto)
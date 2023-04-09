from tb_servicios import *

class roomservice:
    def __init__(self,documento,nombre,email,telefono,direccion):
        self.documento = documento
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.direccion = direccion
    
    def consultaServicios(self,conexion):
        print('CONSULTAR SERVICIOS')
        print()
        id=int(input('¿Cual es el id de la factura a la cual desea ver los servicios cargados?\n-'))
        consulta=select_tb_servicios(conexion, id)
        print(f'Los servicios cargados a la factura con id {id} son:')
        for i in consulta:
            print(i)
        print()
        
    def agregarServicios(self,conexion):
        print('AGREGAR SERVICIOS')
        print()
        print('Datos de la factura y servicios')
        id_fac=int(input('¿Cual es el id de la factura a la cual desea agregar un nuevo servicio?\n-'))
        id_serv=int(input('¿Cual es el id del servicio a agregar?\n-'))
        consulta=select_tb_servicios(conexion, id_fac)
        for i in consulta:
            if id_serv<15:
                agregar=Insertacion_tb_servicios(conexion, id_fac, id_serv)
            else:
                print('El servicio no se encuentra disponible\n')
                break
        consulta=select_tb_servicios(conexion, id_fac)
        for i in consulta:
            print(i)    
        print()
        
#n1=roomservice(1321312, 'No hace nada', 'n@gmail.com', 3213123, 'calle5')
#n1.consultaServicios(proyecto)
#n1.agregarServicios(proyecto)
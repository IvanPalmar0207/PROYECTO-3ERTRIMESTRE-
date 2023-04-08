import sqlite3
with sqlite3.connect('CRUD/BD_PROYECTO.db') as proyecto:
    micursor=proyecto.cursor()
    
def insertar_Reserva(conexion,c1,c2,c3,c4,d1,d2,d3,d4):
    micursor=conexion.cursor()
    sentencia=f'INSERT INTO tb_reserva ({c1},{c2},{c3},{c4}) VALUES ("{d1}","{d2}","{d3}","{d4}")'
    micursor.execute(sentencia)
    conexion.commit()
    print('La insercion del dato fue creado')
#insertar_Reserva(proyecto,'FechaLlegada_res','FechaSalida_res','ValorTotal_res','Id_usu','2024-04-22','2024-04-26','1000000','595950')

def consultarReserva(conexion):
    micursor=conexion.cursor()
    sentencia=f'SELECT * FROM tb_reserva'
    print(micursor.execute(sentencia).fetchall())
#consultarReserva(proyecto)

def consultarReservaUsuario(conexion,d1):
    micursor=conexion.cursor()
    sentencia=f'SELECT * FROM tb_reserva WHERE Id_usu="{d1}"'
    print(micursor.execute(sentencia).fetchall())
#consultarReservaUsuario(proyecto,"7448484")

def actualizarReserva(conexion,d1,c1):
    micursor=conexion.cursor()
    sentencia=f'UPDATE tb_reserva SET ValorTotal_res="{d1}" WHERE Id_res="{c1}"'
    micursor.execute(sentencia)
    conexion.commit()
    print('El registro fue actualizado correctamente')
#actualizarReserva(proyecto,'1500000','11')

def eliminarReserva(conexion,d1):
    micursor=conexion.cursor()
    sentencia=f'DELETE FROM tb_reserva WHERE Id_res="{d1}"'
    micursor.execute(sentencia)
    conexion.commit()
    print('El registro ha sido eliminado corretamente')
eliminarReserva(proyecto,11)
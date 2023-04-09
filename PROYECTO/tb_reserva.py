import sqlite3
with sqlite3.connect('PROYECTO/BD_PROYECTO.db') as proyecto:
    micursor=proyecto.cursor()
    
def insertar_Reserva(conexion,d1,d2,d3,d4):
    micursor=conexion.cursor()
    sentencia=f'INSERT INTO tb_reserva (FechaLlegada_res,FechaSalida_res,ValorTotal_res,Id_usu) VALUES ("{d1}","{d2}","{d3}","{d4}")'
    micursor.execute(sentencia)
    conexion.commit()
    print('Se ha registrado la nueva reserva en la base de datos')
#insertar_Reserva(proyecto,'FechaLlegada_res','FechaSalida_res','ValorTotal_res','Id_usu','2024-04-22','2024-04-26','1000000','595950')

def consultarReserva(conexion):
    micursor=conexion.cursor()
    sentencia=f'SELECT * FROM tb_reserva'
    return (micursor.execute(sentencia).fetchall())
#consultarReserva(proyecto)

def consultarReservaUsuario(conexion,d1):
    micursor=conexion.cursor()
    sentencia=f'SELECT * FROM tb_reserva WHERE Id_usu="{d1}"'
    return (micursor.execute(sentencia).fetchall())
#consultarReservaUsuario(proyecto,"7448484")

def consultarReservar(conexion,d1):
    micursor=conexion.cursor()
    sentencia=f'SELECT * FROM tb_reserva WHERE Id_res="{d1}"'
    return (micursor.execute(sentencia).fetchall())

def actualizarReserva(conexion,val2,d1,c1):
    micursor=conexion.cursor()
    sentencia=f'UPDATE tb_reserva SET {val2}="{d1}" WHERE Id_res="{c1}"'
    micursor.execute(sentencia)
    proyecto.commit()
    print('La reserva ha sido eliminada correctamente')
#actualizarReserva(proyecto,'1500000','11')

def eliminarReserva(conexion,d1):
    micursor=conexion.cursor()
    sentencia=f'DELETE FROM tb_reserva WHERE Id_res="{d1}"'
    micursor.execute(sentencia)
    conexion.commit()
    print('La reserva ha sido eliminada correctamente')
#eliminarReserva(proyecto,11)
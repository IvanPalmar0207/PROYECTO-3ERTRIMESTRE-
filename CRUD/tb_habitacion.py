import sqlite3
with sqlite3.connect('CRUD/BD_PROYECTO.db') as proyecto:
    micursor=proyecto.cursor()
    
def insertar_tipoHabitacion(conexion,c1,c2,d1,d2):
    micursor=conexion.cursor()
    sentencia=f'INSERT INTO tb_habitacion ({c1},{c2}) VALUES ("{d1}","{d2}")'
    micursor.execute(sentencia)
    conexion.commit()
    print('La insercion del dato fue creado')
#insertar_tipoHabitacion(proyecto,'Tipo_hab','PrecioHabitacion_hab','Extra Grande','8000000')

def consultarTipoHabitacion(conexion):
    micursor=conexion.cursor()
    sentencia=f'SELECT * FROM tb_habitacion'
    print(micursor.execute(sentencia).fetchall())
#consultarTipoHabitacion(proyecto)

def consultarHabitacion(conexion,d1):
    micursor=conexion.cursor()
    sentencia=f'SELECT * FROM tb_habitacion WHERE IdTipoHabitacion_hab="{3}"'
    print(micursor.execute(sentencia).fetchall())
#consultarHabitacion(proyecto,"5")

def actualizarTipoHabitacion(conexion,d1,c1):
    micursor=conexion.cursor()
    sentencia=f'UPDATE tb_habitacion SET precioHabitacion_hab="{d1}" WHERE IdTipoHabitacion_hab="{c1}"'
    micursor.execute(sentencia)
    conexion.commit()
    print('El registro fue actualizado correctamente')
#actualizarTipoHabitacion(proyecto,'1500000','7')

def eliminarTipoHabitacion(conexion,d1):
    micursor=conexion.cursor()
    sentencia=f'DELETE FROM tb_habitacion WHERE IdTipoHabitacion_hab="{d1}"'
    micursor.execute(sentencia)
    conexion.commit()
    print('El registro ha sido eliminado corretamente')
eliminarTipoHabitacion(proyecto,7)
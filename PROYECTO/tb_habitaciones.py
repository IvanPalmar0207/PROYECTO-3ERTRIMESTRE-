import sqlite3
with sqlite3.connect('PROYECTO/BD_PROYECTO.db') as hab:
     micursor=hab.cursor()

def Insertacion_tb_habitaciones (conexion,tabla,id_res,idTipoHab,canHab,NumPersona):
    micursor=conexion.cursor()
    sentecia=f'INSERT INTO  {tabla} VALUES ("{id_res}","{idTipoHab}", "{canHab}", "{NumPersona}")'
    micursor.execute(sentecia)
    hab.commit()
    print('fue un exito')
#Insertacion_tb_habitaciones(hab,'tb_habitaciones',1,1,1,2)

def eliminacion_tb_habitaciones (conexion,tabla,id,dato):
    micursor=conexion.cursor()
    sentecia=f'DELETE FROM {tabla} WHERE {id}="{dato}"'
    micursor.excute(sentecia)
    hab.commit()
    print('Eliminación exitosa')
#eliminacion_tb_habitaciones(hab,'tb_habitaciones','Id_res',12)

def select_tb_habitaciones(conexion,tabla,campo,operador,dato):
    micursor=conexion.cursor()
    sentencia=f"SELECT * FROM {tabla} WHERE {campo}{operador}'{dato}'"
    return (micursor.execute(sentencia).fetchall())
#select_tb_habitaciones(hab,'tb_habitaciones','id''=',1)
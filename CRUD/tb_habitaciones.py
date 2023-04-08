import sqlite3
with sqlite3.connect('C:\\Users\\arnol\\Desktop\\PROYECTO-3ERTRIMESTRE-\\PROYECTO-3ERTRIMESTRE-\\CRUD\\BD_PROYECTO.db') as hab:
     micursor=hab.cursor()

def Insertacion_tb_habitaciones (conexion,tabla,id_res,idTipoHab,canHab,NumPersona):
    micursor=conexion.cursor()
    sentecia=f'INSERT INTO  {tabla} VALUES ("{id_res}","{idTipoHab}", "{canHab}", "{NumPersona}")'
    micursor.execute(sentecia)
    hab.commit()
    print('fue un exito')
Insertacion_tb_habitaciones(hab,'tb_habitaciones',1,1,1,2)

def insertacion_tb_habitaciones (conexion,tabla,id_res,idTipoHab,canHab,Numpersona):
    micursor=conexion.cursor()
    sentecia=f'INSERT INTO  {tabla} VALUES ("{id_res}","{idTipoHab}", "{canHab}", "{Numpersona}")'
    micursor.execute(sentecia)
    hab.commit()
    print('fue un exito')
Insertacion_tb_habitaciones (hab,'tb_habitaciones',8,2,5,1)

def insertacion_tb_habitaciones (conexion,tabla,id_res,idTipoHab,canHab,Numpersona):
    micursor=conexion.cursor()
    sentecia=f'INSERT INTO  {tabla} VALUES ("{id_res}","{idTipoHab}", "{canHab}", "{Numpersona}")'
    micursor.execute(sentecia)
    hab.commit()
    print('fue un exito')
Insertacion_tb_habitaciones (hab,'tb_habitaciones',10,6,4,7)

def insertacion_tb_habitaciones (conexion,tabla,id_res,idTipoHab,canHab,Numpersona):
    micursor=conexion.cursor()
    sentecia=f'INSERT INTO  {tabla} VALUES ("{id_res}","{idTipoHab}", "{canHab}", "{Numpersona}")'
    micursor.execute(sentecia)
    hab.commit()
    print('fue un exito')
Insertacion_tb_habitaciones (hab,'tb_habitaciones',11,4,2,3)

def insertacion_tb_habitaciones (conexion,tabla,id_res,idTipoHab,canHab,Numpersona):
    micursor=conexion.cursor()
    sentecia=f'INSERT INTO  {tabla} VALUES ("{id_res}","{idTipoHab}", "{canHab}", "{Numpersona}")'
    micursor.execute(sentecia)
    hab.commit()
    print('fue un exito')
Insertacion_tb_habitaciones (hab,'tb_habitaciones',6,2,5,4)

def eliminacion_tb_habitaciones (conexion,tabla,id,dato):
    micursor=conexion.cursor()
    sentecia=f'DELETE FROM {tabla} WHERE {id}="{dato}"'
    micursor.excute(sentecia)
    hab.commit()
    print('Eliminación exitosa')
eliminacion_tb_habitaciones(hab,'tb_habitaciones','Id_res',12)

def select_tb_habitaciones(conexion,tabla,campo,operador,dato):
    micursor=conexion.cursor()
    sentencia=f"SELECT * FROM {tabla} WHERE {campo}{operador}'{dato}'"
    print(sentencia)
    print(micursor.execute(sentencia).fetchall())
select_tb_habitaciones(hab,'tb_habitaciones','id''=',1)
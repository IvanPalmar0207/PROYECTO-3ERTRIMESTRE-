import sqlite3
with sqlite3.connect('C:\\Users\\arnol\\Desktop\\PROYECTO-3ERTRIMESTRE-\\PROYECTO-3ERTRIMESTRE-\\CRUD\\BD_PROYECTO.db') as ser:
     micursor=ser.cursor()

def Insertacion_tb_servicios (conexion,tabla,id_fac,id_serv):
    micursor=conexion.cursor()
    sentecia=f'INSERT INTO  {tabla} VALUES ("{id_fac}","{id_serv}")'
    micursor.execute(sentecia)
    ser.commit()
    print('fue un exito')
Insertacion_tb_servicios(ser,'tb_servicios',11,14)     

def Insertacion_tb_servicios (conexion,tabla,id_fac,id_serv):
    micursor=conexion.cursor()
    sentecia=f'INSERT INTO  {tabla} VALUES ("{id_fac}","{id_serv}")'
    micursor.execute(sentecia)
    ser.commit()
    print('fue un exito')
Insertacion_tb_servicios(ser,'tb_servicios',11,4)     

def modificacion_tb_servicios (conexion,tabla,campo,dato,id):
    micursor=conexion.cursor()
    sentencia=f"UPDATE {tabla} SET {campo}='{dato}' WHERE id='{id}'"
    micursor.excute(sentencia)
    ser.commit()
    print('Modificación con exito')
modificacion_tb_servicios(ser,'tb_servicios','id_fac',11,2)

def select_tb_servicios(conexion):
    micursor=conexion.cursor()
    sentencia=f"SELECT * FROM tb_servicios"

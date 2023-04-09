import sqlite3
with sqlite3.connect('PROYECTO/BD_PROYECTO.db') as proyecto:
    micursor=proyecto.cursor()

def Insertacion_tb_servicios (conexion,id_fac,id_serv):
    micursor=conexion.cursor()
    sentecia=f'INSERT INTO  tb_servicios VALUES ("{id_fac}","{id_serv}")'
    micursor.execute(sentecia)
    proyecto.commit()
    print('El nuevo servicio fue cargado correctamente')
#Insertacion_tb_servicios(ser,'tb_servicios',11,14)     

def modificacion_tb_servicios (conexion,tabla,campo,dato,id):
    micursor=conexion.cursor()
    sentencia=f"UPDATE tb_servicios SET {campo}='{dato}' WHERE id='{id}'"
    micursor.excute(sentencia)
    proyecto.commit()
    print('El servicio fue modificado correctamente')
#modificacion_tb_servicios(ser,'tb_servicios','id_fac',11,2)

def select_tb_servicios(conexion,id):
    micursor=conexion.cursor()
    sentencia=f"SELECT * FROM tb_servicios WHERE Id_fac='{id}'"
    return (micursor.execute(sentencia).fetchall())
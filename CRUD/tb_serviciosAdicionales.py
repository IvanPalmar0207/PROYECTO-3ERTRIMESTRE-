import sqlite3
with sqlite3.connect('C:\\Users\\arnol\\Desktop\\PROYECTO-3ERTRIMESTRE-\\PROYECTO-3ERTRIMESTRE-\\CRUD\\BD_PROYECTO.db') as sAdi:
     micursor=sAdi.cursor()


def Insertacion_tb_ServiciosAdicionales (conexion,tabla,id_res,TipoSer,preSer):
    micursor=conexion.cursor()
    sentecia=f'INSERT INTO  {tabla} VALUES ("{id_res}","{TipoSer}", "{preSer}")'
    micursor.execute(sentecia)
    sAdi.commit()
    print('fue un exito')
Insertacion_tb_ServiciosAdicionales(sAdi,'tb_serviciosAdicionales',)

def Insertacion_tb_ServiciosAdicionales (conexion,tabla,id_res,TipoSer,preSer):
    micursor=conexion.cursor()
    sentecia=f'INSERT INTO  {tabla} VALUES ("{id_res}","{TipoSer}", "{preSer}")'
    micursor.execute(sentecia)
    sAdi.commit()
    print('fue un exito')
Insertacion_tb_ServiciosAdicionales(sAdi,'tb_serviciosAdicionales',)

def modificacion_tb_servicios (conexion,tabla,campo,dato,id):
    micursor=conexion.cursor()
    sentencia=f"UPDATE {tabla} SET {campo}='{dato}' WHERE id='{id}'"
    micursor.excute(sentencia)
    sAdi.commit()
    print('Modificación con exito')
modificacion_tb_servicios(sAdi,'tb_serviosAdicionales',)

def eliminacion_tb_habitaciones (conexion,tabla,id_res,TipoSer):
    micursor=conexion.cursor()
    sentecia=f'DELETE FROM {tabla} WHERE {id_res}="{TipoSer}"'
    micursor.excute(sentecia)
    sAdi.commit()
    print('Eliminación exitosa')
eliminacion_tb_habitaciones(sAdi,'tb_habitaciones',)






def select_tb_servicios(conexion):
    micursor=conexion.cursor()
    sentencia=f"SELECT * FROM tb_servicios"
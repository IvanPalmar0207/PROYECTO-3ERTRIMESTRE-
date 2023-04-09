import sqlite3
with sqlite3.connect('PROYECTO/BD_PROYECTO.db') as proyecto:
     micursor=proyecto.cursor()

def Insert_tbServiciosAdicionales (conexion,TipoSer,preSer):
    micursor=conexion.cursor()
    sentecia=f'INSERT INTO tb_serviciosAdicionales (TipoServicio_serv,Precio_serv)  VALUES ("{TipoSer}", "{preSer}")'
    micursor.execute(sentecia)
    proyecto.commit()
    print('El registro se agrego con exito')
#Insertacion_tb_ServiciosAdicionales(sAdi,'tb_serviciosAdicionales',)

def select_ServiciosAdicionales (conexion):
    micursor=conexion.cursor()
    sentencia=f'SELECT * FROM tb_serviciosAdicionales'
    return (micursor.execute(sentencia).fetchall())
    
def select_ServiciosAdicionales_condicion(conexion,id):
    micursor=conexion.cursor()
    sentencia=f'SELECT * FROM tb_serviciosAdicionales WHERE id_serv="{id}"'
    return (micursor.execute(sentencia).fetchall())

def modificacion_tbServiciosAdicionales(conexion,campo,dato,id):
    micursor=conexion.cursor()
    sentencia=f"UPDATE tb_serviciosAdicionales SET {campo}='{dato}' WHERE id_serv='{id}'"
    micursor.execute(sentencia)
    proyecto.commit()
    print('Modificación con exito.')
#modificacion_tb_servicios(sAdi,'tb_serviosAdicionales',)

def eliminacion_tbServiciosAdicionales (conexion,id):
    micursor=conexion.cursor()
    sentecia=f'DELETE FROM tb_serviciosAdicionales WHERE id_serv="{id}"'
    micursor.execute(sentecia)
    proyecto.commit()
    print('Eliminación exitosa.')
#eliminacion_tb_habitaciones(sAdi,'tb_habitaciones',)
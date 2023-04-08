import sqlite3
with sqlite3.connect('CRUD/BD_PROYECTO.db') as proyecto:
    micursor=proyecto.cursor()
    
def insertar_factura(conexion,c1,c2,c3,d1,d2,d3):
    micursor=conexion.cursor()
    sentencia=f'INSERT INTO tb_facturacion ({c1},{c2},{c3}) VALUES ("{d1}","{d2}","{d3}")'
    micursor.execute(sentencia)
    conexion.commit()
    print('La insercion del dato fue creado')
#insertar_factura(proyecto,'Fecha_fac','Id_usu','ValorTotal_fac','2024-04-07','595950','2000000')

def consultarFacturas(conexion):
    micursor=conexion.cursor()
    sentencia=f'SELECT * FROM tb_facturacion'
    print(micursor.execute(sentencia).fetchall())
#consultarFacturas(proyecto)

def consultarUsuario(conexion,d1):
    micursor=conexion.cursor()
    sentencia=f'SELECT * FROM tb_facturacion WHERE Id_usu="{d1}"'
    print(micursor.execute(sentencia).fetchall())
#consultarUsuario(proyecto,"595950")

def actualizarFactura(conexion,d1,c1):
    micursor=conexion.cursor()
    sentencia=f'UPDATE tb_facturacion SET ValorTotal_fac="{d1}" WHERE id_fac="{c1}"'
    micursor.execute(sentencia)
    conexion.commit()
    print('El registro fue actualizado correctamente')
#actualizarFactura(proyecto,'1500000','11')

def eliminarFactura(conexion,d1):
    micursor=conexion.cursor()
    sentencia=f'DELETE FROM tb_facturacion WHERE id_fac="{d1}"'
    micursor.execute(sentencia)
    conexion.commit()
    print('El registro ha sido eliminado corretamente')
#eliminarFactura(proyecto,11)
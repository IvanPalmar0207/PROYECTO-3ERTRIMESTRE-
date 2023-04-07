import sqlite3
with sqlite3.connect('CRUD/BD_PROYECTO.db') as database:
    micursor=database.cursor()
    sentencia=''
def insertar_TpUsuario(conexion,c1,dato1):
    micursor=conexion.cursor()
    sentenciainsert=f'INSERT INTO tb_tipoUsuario ({c1}) VALUES ("{dato1}")'
    micursor.execute(sentenciainsert)
    database.commit()
    print('La insercion del dato fue creado')
#Ejemplo
#insertar_TpUsuario(database,'Tipo_TpU','Prueba-ADSO')

def selectALL_tpUsuario(conexion):
    micursor=conexion.cursor()
    sentenciaselectall=f'SELECT * FROM tb_tipoUsuario'
    print(micursor.execute(sentenciaselectall).fetchall())
#Ejemplo
#selectALL_tpUsuario(database)

def selectId_tpUsuario(conexion,condicionid):
    micursor=conexion.cursor()
    sentencia=f'SELECT * FROM tb_tipoUsuario WHERE Id_TpU="{condicionid}"'
    print(micursor.execute(sentencia).fetchall())
#Ejemplo
#selectId_tpUsuario(goku,7)

def updateId_tpUsuario(conexion,nombre,id):
    micursor=conexion.cursor()
    sentencia=f'UPDATE tb_tipoUsuario SET Tipo_TpU="{nombre}" WHERE Id_TpU="{id}"'
    micursor.execute(sentencia)
    database.commit()
    print('El registro fue actualizado correctamente')
#Ejemplo
#updateId_tpUsuario(database,'Saiyajin',2)

def delete_tpUsuario(conexion,id):
    micursor=conexion.cursor()
    sentencia=f'DELETE FROM tb_tipoUsuario WHERE Id_TpU="{id}"'
    micursor.execute(sentencia)
    database.commit()
    print('El registro ha sido eliminado corretamente')
#Ejemplo
#delete_tpUsuario(database,2)
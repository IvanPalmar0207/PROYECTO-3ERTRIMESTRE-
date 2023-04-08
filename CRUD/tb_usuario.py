import sqlite3
with sqlite3.connect('CRUD/BD_PROYECTO.db') as database:
    micursor=database.cursor()

def insert_tbUsuario(conexion,id,nombre,apellido,email,telefono,direccion,contraseña,fechares,fecharegis,id_tpu):
    micursor=conexion.cursor()
    sentencia=f'INSERT INTO tb_usuario (Id_usu,Nombre_usu,Apellido_usu,Email_usu,Telefono_usu,Direccion_usu,Password_usu,FechaRestablecimiento_usu,FechaRegistro_usu,Id_TpU) VALUES ("{id}","{nombre}","{apellido}","{email}","{telefono}","{direccion}","{contraseña}","{fechares}","{fecharegis}","{id_tpu}")'
    micursor.execute(sentencia)
    database.commit()
    print('El registro ha sido agregado a la base de datos')
#Ejemplo
#insert_tbUsuario(database, 13, 'Ivan', 'Palmar', 'palmar.ivan0205@gmail.com', 12312423, 'calle 34No 14-00 este','hjda', '', '4/07/2023', 3)

def selectAll_tbUsuario(conexion):
    micursor=conexion.cursor()
    select=f'SELECT * FROM tb_usuario'
    print('El resultado es: \n')
    print(micursor.execute(select).fetchall())
#Ejemplo
#selectAll_tbUsuario(database)

def selectCondition_tbUsuario(conexion,campo,operator,condition):
    micursor=conexion.cursor()
    sentencia=f'SELECT * FROM tb_usuario WHERE {campo}{operator}{condition}'
    print('El resultado es: \n')
    print(micursor.execute(sentencia).fetchall())
#Ejemplo
#selectCondition_tbUsuario(database,'Id_TpU','>',2)

def update_tbUsuario(conexion,campo1,condition1,campo2,condition2):
    micursor=conexion.cursor()
    sentencia=f'UPDATE tb_usuario SET {campo1}="{condition1}" WHERE {campo2}="{condition2}"'
    micursor.execute(sentencia)
    database.commit()
    print('La actualizacion fue completamente realizada')
#Ejemplo
#update_tbUsuario(database, 'Nombre_usu', 'Alien Isolation', 'Id_usu', 1444441441)
    
def delete_tbUsuario(conexion,campo,operator,condition):
    micursor=conexion.cursor()
    sentencia=f'DELETE FROM tb_usuario WHERE {campo}{operator}="{condition}"'
    micursor.execute(sentencia)
    database.commit()
    print('La eliminacion fue completamente realizada')
#Ejemplo
#delete_tbUsuario(database,'Id_usu', '=', 1444441441)
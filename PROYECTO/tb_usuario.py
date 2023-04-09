import sqlite3
with sqlite3.connect('PROYECTO/BD_PROYECTO.db') as proyecto:
    micursor=proyecto.cursor()

def insert_tbUsuario(conexion,id,nombre,apellido,email,telefono,direccion,contraseña,fechares,fecharegis,id_tpu):
    micursor=conexion.cursor()
    sentencia=f'INSERT INTO tb_usuario (Id_usu,Nombre_usu,Apellido_usu,Email_usu,Telefono_usu,Direccion_usu,Password_usu,FechaRestablecimiento_usu,FechaRegistro_usu,Id_TpU) VALUES ("{id}","{nombre}","{apellido}","{email}","{telefono}","{direccion}","{contraseña}","{fechares}","{fecharegis}","{id_tpu}")'
    micursor.execute(sentencia)
    proyecto.commit()
    print('El registro ha sido agregado a la base de datos.')
#Ejemplo
#insert_tbUsuario(database, 13, 'Ivan', 'Palmar', 'palmar.ivan0205@gmail.com', 12312423, 'calle 34No 14-00 este','hjda', '', '4/07/2023', 3)

def selectAll_tbUsuario(conexion):
    micursor=conexion.cursor()
    select=f'SELECT * FROM tb_usuario'
    print('El resultado es: \n')
    return (micursor.execute(select).fetchall())
#Ejemplo
#selectAll_tbUsuario(database)

def selectCondition_tbUsuario(conexion,condition):
    micursor=conexion.cursor()
    sentencia=f'SELECT * FROM tb_usuario WHERE Id_usu="{condition}"'
    print('El resultado es: \n')
    return (micursor.execute(sentencia).fetchall())
#Ejemplo
#selectCondition_tbUsuario(database,'Id_TpU','>',2)

def update_tbUsuario(conexion,campo1,condition1,condition2):
    micursor=conexion.cursor()
    sentencia=f'UPDATE tb_usuario SET {campo1}="{condition1}" WHERE Id_usu="{condition2}"'
    micursor.execute(sentencia)
    proyecto.commit()
    print('La actualizacion fue completamente realizada')
#Ejemplo
#update_tbUsuario(database, 'Nombre_usu', 'Alien Isolation', 'Id_usu', 1444441441)
    
def delete_tbUsuario(conexion,condition):
    micursor=conexion.cursor()
    sentencia=f'DELETE FROM tb_usuario WHERE Id_usu="{condition}"'
    micursor.execute(sentencia)
    proyecto.commit()
    print('La eliminacion fue completamente realizada')
#Ejemplo
#delete_tbUsuario(database,'Id_usu', '=', 1444441441)
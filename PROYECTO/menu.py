from administrador import * 
from cliente import *
from mesero import *
from recepcionista import *
from roomservice import *
import os
import time
    
def menuAdministrador():
    print("-"*50)
    print ("           BIENVENIDO ADMINISTRADOR    ")
    print("-"*50), time.sleep(0.7)
    print('\n      REGISTRO ADMINISTRADOR      \n'),time.sleep(0.30)
    documento=int(input('Cual es tu documento?\n-'))
    nombre=input('¿Cual es tu nombre?\n-')
    email=input('¿Cual es tu email?\n-')
    telefono=int(input('¿Cual es tu telefono?\n-'))
    direccion=input('¿Cual es tu direccion?\n-')
    registro=administrador(documento, nombre, email, telefono, direccion)
    while True:
        os.system("cls")
        print()
        print('-'*50)
        print('             OPCIONES ADMINISTRADOR    ')
        print("-"*50), time.sleep(0.7)
        print('\n1.Consultar habitacion'),time.sleep(0.35)
        print('2.Agregar Habitacion'),time.sleep(0.35)
        print('3.Actualizar Habitacion'),time.sleep(0.35)
        print('4.Eliminar Habitacion'),time.sleep(0.35)
        print('5.Consultar servicios'),time.sleep(0.35)
        print('6.Crear servicios'),time.sleep(0.35)
        print('7.Actualizar servicios'),time.sleep(0.35)
        print('8.Eliminar servicios'),time.sleep(0.35)
        print('9.Consultar usuarios'),time.sleep(0.35)
        print('10.Crear usuarios'),time.sleep(0.35)
        print('11.Actualizar usuarios'),time.sleep(0.35)
        print('12.Eliminar usuarios'),time.sleep(0.35)
        print('0.Salir del menu del administrador\n'),time.sleep(0.35)
        menu=int(input('¿Cual opcion elegiras?\n-'))
        match menu:
            case 1:
                registro.consulHabitacion(proyecto)
                print()
                print('-'*35),time.sleep(10)
            case 2:
                registro.agregarHabitacion(proyecto)
                print()
                print('-'*35),time.sleep(40)
            case 3:
                registro.actualizarHabitacion(proyecto)
                print()
                print('-'*35),time.sleep(40)
            case 4: 
                registro.eliminarHabitacion(proyecto)
                print()
                print('-'*35),time.sleep(40)
            case 5:
                registro.consultarServicios(proyecto)
                print()
                print('-'*35),time.sleep(10)
            case 6:
                registro.crear_ServiciosAdicionales(proyecto)
                print()
                print('-'*35),time.sleep(40)
            case 7:
                registro.actualizar_servicio(proyecto)
                print()
                print('-'*35),time.sleep(40)
            case 8:
                registro.elimiar_servicios(proyecto)
                print()
                print('-'*35),time.sleep(40)
            case 9:
                registro.consultar_empleados(proyecto)
                print()
                print('-'*35),time.sleep(10)
            case 10:
                registro.crear_usuarios(proyecto)
                print()
                print('-'*35),time.sleep(40)
            case 11:
                registro.actualizar_servicio(proyecto)
                print()
                print('-'*35),time.sleep(40)
            case 12:
                registro.eliminar_usuario(proyecto)
                print()
                print('-'*35),time.sleep(40)
            case 0:
                print('Gracias por ser un gran administrador')
                break
            case _:
                print('Ingresaste un numero erroneo')
                break
#Ejemplo
#menuAdministrador()

def menuCliente():
    print("-"*30)
    print ("    BIENVENIDO CLIENTE    ")
    print("-"*30), time.sleep(0.7)
    print('\n    REGISTRO CLIENTE      \n'),time.sleep(0.30)
    documento=int(input('Cual es tu documento?\n-'))
    nombre=input('¿Cual es tu nombre?\n-')
    correo=input('¿Cual es tu email?\n-')
    telefono=int(input('¿Cual es tu telefono?\n-'))
    direccion=input('¿Cual es tu direccion?\n-')
    registro=cliente(documento, nombre, correo, telefono, direccion)
    while True:
        os.system("cls")
        print()
        print('-'*30)
        print('    OPCIONES CLIENTE    \n')
        print("-"*30), time.sleep(0.7)
        print('\n1.Registrar una reserva'),time.sleep(0.35)
        print('2.Consultar reservas'),time.sleep(0.35)
        print('3.Actualizar Reserva'),time.sleep(0.35)
        print('4.Cancelar Reserva'),time.sleep(0.35)
        print('0.Salir del menu del administrador\n'),time.sleep(0.35)
        menu=int(input('¿Que opcion elegiras?\n-'))
        match menu:
            case 1:
                registro.registro_Reserva(proyecto)
                print()
                print('-'*35),time.sleep(40)
            case 2:
                registro.consultar_Reservas(proyecto)
                print()
                print('-'*35),time.sleep(30)
            case 3:
                registro.actualizar_Reserva(proyecto)
                print()
                print('-'*35),time.sleep(40)
            case 4:
                registro.cancelar_Reserva(proyecto)
                print()
                print('-'*35),time.sleep(40)
            case 0:
                print('Gracias por ser un fiel cliente.')
                break
            case _:
                print('Ingresaste un numero herroneo.')
                break
#Ejemplo
#menuCliente()
def menuRecepcionista():
    print("-"*30)
    print ("    BIENVENIDO RECEPCIONISTA    ")
    print("-"*30), time.sleep(0.7)
    print('\n    REGISTRO RECEPCIONISTA      \n'),time.sleep(0.30)
    documento=int(input('Cual es tu documento?\n-'))
    nombre=input('¿Cual es tu nombre?\n-')
    email=input('¿Cual es tu email?\n-')
    telefono=int(input('¿Cual es tu telefono?\n-'))
    direccion=input('¿Cual es tu direccion?\n-')
    registro=recepcionista(documento, nombre, email, telefono, direccion)
    while True:
        os.system("cls")
        print()
        print('-'*30)
        print('    OPCIONES RECEPCIONISTA    ')
        print("-"*30), time.sleep(0.7)
        print('\n1.Consultar Reservas'),time.sleep(0.35)
        print('2.Crear Reservas'),time.sleep(0.35)
        print('3.Actualizar Reservas'),time.sleep(0.35)
        print('4.Eliminar Reserva'),time.sleep(0.35)
        print('5.Consultar Factura'),time.sleep(0.35)
        print('0.Salir del menu del administrador\n'),time.sleep(0.35)
        menu=int(input('¿Que opcion elegiras?\n-'))
        match menu:
            case 1:
                registro.consultar_reserva(proyecto)
                print()
                print('-'*35),time.sleep(40)
            case 2:
                registro.crearReserva(proyecto)
                print()
                print('-'*35),time.sleep(40)
            case 3:
                registro.actualizarReserva(proyecto)
                print()
                print('-'*35),time.sleep(40)
            case 4:
                registro.eliminar_reserva(proyecto)
                print()
                print('-'*35),time.sleep(40)
            case 5:
                registro.consultarFactura(proyecto)
                print()
                print('-'*35),time.sleep(40)
            case 0:
                print('Gracias por ser un buen recepcionista')
                break
            case _:
                print('Ingresaste un numero incorrecto')
                break
#ejemplo
#menuRecepcionista()            
    
def menuMesero():
    print("-"*30)
    print ("      BIENVENIDO MESERO    ")
    print("-"*30), time.sleep(0.7)
    print('\n       REGISTRO MESERO     \n'),time.sleep(0.30)
    documento=int(input('Cual es tu documento?\n-'))
    nombre=input('¿Cual es tu nombre?\n-')
    email=input('¿Cual es tu email?\n-')
    telefono=int(input('¿Cual es tu telefono?\n-'))
    direccion=input('¿Cual es tu direccion?\n-')
    registro=mesero(documento, nombre, email, direccion, telefono)
    while True:
        os.system("cls")
        print()
        print('-'*30)
        print('      OPCIONES MESERO    ')
        print("-"*30), time.sleep(0.7)
        print('\n1.Consultar Servicios'),time.sleep(0.35)
        print('2.Agregar Servicios'),time.sleep(0.35)
        print('0.Salir del menu del administrador\n'),time.sleep(0.35)
        menu=int(input('¿Que opcion elegiras?\n-'))
        match menu:
            case 1:
                registro.consultar_servicios(proyecto)
                print()
                print('-'*35),time.sleep(40)
            case 2:
                registro.agregar_servicios(proyecto)
                print()
                print('-'*35),time.sleep(40)
            case 0:
                print('Gracias por ser un buen Mesero')
                break
            case _:
                print('Digitaste un numero erroeneo')
                break
#Ejemplo
#menuMesero()                

def menuRoomservice():
    print("-"*30)
    print ("      BIENVENIDO ROOMSERVICE    ")
    print("-"*30), time.sleep(0.7)
    print('\n       REGISTRO ROOM SERVICE     \n'),time.sleep(0.30)
    documento=int(input('Cual es tu documento?\n-'))
    nombre=input('¿Cual es tu nombre?\n-')
    email=input('¿Cual es tu email?\n-')
    telefono=int(input('¿Cual es tu telefono?\n-'))
    direccion=input('¿Cual es tu direccion?\n-')
    registro=roomservice(documento, nombre, email, telefono, direccion)
    while True:
        os.system("cls")
        print()
        print('-'*30)
        print('      OPCIONES ROOM SERVICE    ')
        print("-"*30), time.sleep(0.7)
        print('\n1.Consultar Servicios'),time.sleep(0.35)
        print('2.Agregar Servicios'),time.sleep(0.35)
        print('0.Salir del menu del administrador\n'),time.sleep(0.35)
        menu=int(input('¿Que opcion elegiras?\n-'))
        match menu:
            case 1:
                registro.consultaServicios(proyecto)
                print()
                print('-'*35),time.sleep(40)
            case 2:
                registro.agregarServicios(proyecto)
                print()
                print('-'*35),time.sleep(40)
            case 0:
                print('Gracias por ser un gran RoomService')
                break
            case _:
                print('Ingresaste un numero incorrecto')
                break
            
def menuProyecto():
    while True:
        os.system("cls")
        print("-"*40)
        print ("       BIENVENIDO AL HOTEL PEGASUS    ")
        print("-"*40),time.sleep(0.7)
        print ("1","Administrador", sep=" -> "),time.sleep(0.35)
        print ("2","Cliente", sep=" -> "),time.sleep(0.35)
        print ("3","Recepcionista", sep=" -> "),time.sleep(0.35)
        print ("4","Mesero", sep=" -> "),time.sleep(0.35)
        print ("5","Room Service", sep=" -> "),time.sleep(0.35)
        print ("0","Salir", sep=" -> "),time.sleep(0.35)
        menu=int(input('¿Cual es tu rol (Digita un numero)?\n-'))
        match menu:
            case 1:
                menuAdministrador()
            case 2:
                menuCliente()
            case 3:
                menuRecepcionista()
            case 4:
                menuMesero()
            case 5:
                menuRoomservice()
            case 0:
                print('Gracias por usar nuestro menu Hotelero.')
                break
            case _:
                print("digitastes un número incorrecto, pero gracias por usar el menu de el Hotel Pegasus.")
                break
menuProyecto()
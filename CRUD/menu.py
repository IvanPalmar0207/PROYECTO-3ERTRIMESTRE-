import os
import time
def menu ():
    while True:
        os.system("cls")
        print("-"*50)
        print ("       BIENVENIDO AL HOTEL PEGASUS    ")
        print("-"*50),time.sleep(0.7)
        print ("1","Administrador", sep=" -> "),time.sleep(0.35)
        print ("2","Cliente", sep=" -> "),time.sleep(0.35)
        print ("3","Recepcionista", sep=" -> "),time.sleep(0.35)
        print ("4","Mesero", sep=" -> "),time.sleep(0.35)
        print ("5","Room Service", sep=" -> "),time.sleep(0.35)
        print ("6","Salir", sep=" -> "),time.sleep(0.35)
        seleccion=input("Escoja la opción, según su rol:  ")
        match seleccion:
            case "1":
                pass
            case "2":
                pass
            case "3":
                pass
            case "4":
                os.system("cls")
                print("-"*50)
                print ("       4 -> Eliminar Cantante: ")
                print("-"*50),time.sleep(1)
                nombre=input("Ingrese el nombre del cantante a eliminar:  ") 
            case "5":
                pass
            case "6":
                os.system("cls")
                print("-"*50)
                print("Hasta pronto, ¡¡FIN!!")
                print("-"*50),time.sleep(3)
                break
            case _:
                print("digitastes un número incorrecto")

menu()
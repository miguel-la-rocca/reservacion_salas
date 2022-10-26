# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 21:55:48 2022

@author: gaita_c0xadhf
"""

from datetime import datetime
import time


today = datetime.today()





class Salas:
    
    

    def __init__(self ,nombre ,  cant_pers,  tamano, usos , fechas_ocupadas = "01-01-1900" ):
        self.nombre=nombre
       
        self.fechas_ocupadas=datetime.strptime(fechas_ocupadas, '%d-%m-%Y')
        
        self.fechas_ocupadas=datetime.strptime(fechas_ocupadas, '%d-%m-%Y')
        
        self.cant_pers=cant_pers
        self.tamano=tamano
        self.usos=usos
        self.caracteristicas={"Cantidad de personas":cant_pers, "Tamaño": tamano, " usos": usos}    
        self.lista_fechas_ocupadas=[]
        self.lista_fechas_ocupadas.append(self.fechas_ocupadas)
        
        
        #lista_salas.append(self)         
     
                
            
    def __str__ (self):
        
       
            return (f"\nNombre: {self.nombre} \n  \nCaracteristicas: {self.caracteristicas}  \n\n")
        
   
    def __setitem__(self, fecha_agre):  #agregar fecha de reserva
        convert_fecha=datetime.strptime(fecha_agre , '%d-%m-%Y')
        self.lista_fechas_ocupadas.append(convert_fecha)
        
    
        
    def mostrar_reservas(self):  #mostrar reservas
        print("Fechas ocupadas:\n ")
        for fechas in self.lista_fechas_ocupadas:
            print(f"--- {fechas.strftime('%d-%m-%Y')} ---")


def buscar_sala(lista_salas):
    print("Buscando Sala...\n")
    time.sleep(0.5)
    nombre = str(input("Nombre a buscar: "))
    for objSalas in lista_salas:
        if nombre == objSalas.nombre:
            print("SALA ENCONTRADA!")
            print(objSalas)
            return objSalas
        else : print("No se encontro la sala buscado")      

def creas_sala(lista_salas):
    print(" Ingrese los datos para crear una nueva sala \n\n ")
    nombre=input("\nIngrese el nombre de la sala \n")
    fechas_ocupadas=input("Ingrese la fecha que desea reservar con el formato [dd-mm-yyyy]\n")
    cant_pers=int(input("Ingrese la capacidad de personas \n"))
    tamano=int(input("Ingrese el tamaño de la sala en m2 \n"))
    usos=input("Ingrese los usos disponibles separados por una coma \n")
    
    objSalas = Salas(nombre,  cant_pers, tamano, usos, fechas_ocupadas)
    lista_salas.append(objSalas)      
      
def listar_salas(lista_salas):    #Mostrar salas
    print("Listado de Salones\n")
    for objSalas in lista_salas:
        print(objSalas)
        objSalas.mostrar_reservas()
    
        
def listarfechasocupSalas(lista_salas):
  print("Listar fechas ocupadas de la sala")
  objSalas = buscar_sala(lista_salas)
  objSalas.mostrar_reservas()
  
def reservar(lista_salas):
    print("Agregar reserva\n")
    objSalas = buscar_sala(lista_salas)
    if objSalas == None:
      return
    else:
        time.sleep(0.5)
        fecha_agre = input("Fecha a agregar [dd-mm-yyyy]: ")
        convert_fecha_agre=datetime.strptime(fecha_agre, '%d-%m-%Y')
       
        print(objSalas.fechas_ocupadas)
        if not convert_fecha_agre in objSalas.lista_fechas_ocupadas:
            objSalas.lista_fechas_ocupadas.append(convert_fecha_agre)
            input("...FECHA AGREGADA... \nPresione enter para continuar")
      
        
        else :
            print("Esa fecha esta reservada, por favor elija otra")
            return

def salir():
    print("Salida inminente...!")
    
     
def main(lista_salas):
    while True:
        print("\n")
        print("|****************************|")
        print("|**|      Bienvenidos     |**|")
        print("|**|         Menu         |**|")
        print("|****************************|")
        print("")
        print("Seleccione una de las siguientes opciones:");
        print("1.- Reservar sala")
        print("2.- Informacion de los salones")
        print("3.- Mostrar_reservas")
        print("4.- Crear sala")
        print("9.- Salir\n")
        time.sleep(0.5)
        opcion = int(input("Opcion: "))
        

        if  opcion == 1:
            reservar(lista_salas)
        elif opcion == 2:
            listar_salas(lista_salas)
        elif opcion == 3:
            listarfechasocupSalas(lista_salas)
        elif opcion == 4:
            creas_sala(lista_salas)
        elif opcion == 9:
            
            salir()
            break

            
lista_salas=[]
main(lista_salas)
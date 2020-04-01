# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
lista_anim=[]
lista_tipo=[]
lista_mkgasto=[]
class animal: 
    def init(self, nombre, tipo):
        self.nombre = nombre
        self.tipo   = tipo
       
    def set_nombre(self,nombre): 
        self.nombre = nombre
          
    def get_nombre(self):
        print(self.nombre)
        self.get_miprueba()

def Menu():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Que opcion deseas?....: "))
            correcto=True
        except ValueError:
            print('Esa no es una opcion, intenta de nuevo')
     
    return num
 
salir = False
opcion = 0
 
while not salir:
 
    print ("\n \n1. Añadir un animal a la lista")
    print ("2. Ver la lista")
    print ("3. Salir") 
    print ("Elige una opcion")
 
    opcion = Menu()
 
    if opcion == 1:
     a=int (input ("Cuantos animales quieres añadir? \n"))
     for x in range (a):
            nombreanim=input("Dame el nombre del animal \n")
            lista_anim.append(nombreanim)
            tipoanimal=input("Que tipo de animal es?\n")
            lista_tipo.append(tipoanimal)
    elif opcion == 2:
        lista_mkgasto = lista_anim+lista_tipo
        for element in lista_mkgasto:
         print (element)
    elif opcion == 3:
        salir = True
    else:
        print ("Esa no es una opcion, intenta de nuevo")
 
print ("Fin")
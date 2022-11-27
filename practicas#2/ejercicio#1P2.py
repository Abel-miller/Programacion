#Escribir un programa que pregunte el nombre del usuario en la consola 
#y un número entero e imprima por pantalla en líneas distintas el nombre 
#del usuario tantas veces como el número introducido.

name=input("Ingresar un nombre:")
number=int(input("Ingresar un numero:"))

while number  > 0:
    print (name)
    number=number-1 
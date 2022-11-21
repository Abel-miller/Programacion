#Ejercicio 1: Multiplicar 2 números sin usar el símbolo de la multiplicación.
#a = int(input("Ingresar el primer numero: \n"))
#b = int(input("Ingrese el segundo numero: \n"))

def multiplicar(a,b):
 sum=0
 cont=0

 while(cont<b):
    sum=sum+a
    cont+=1

 return(sum)
print(multiplicar(5,5))

#Ejercicio 2 : ingresar el nombre y apellido e imprimirlo al revés.

def invertir_cadena(cadena):
 inversa =""
 for x in cadena: 
   inversa = x + inversa 
 return (inversa) 
print(invertir_cadena("Daddy Acacho"))


#Ejercicio 3: Crear un cript que encuentre el elemento menor de una lista.

def elemento_menor(lista):
    menor=lista[0]
    for x in range(1,len(lista)):
        if (lista[x]<menor):
            menor=lista[x]
    return(menor)
lista=[5,6,12,32,0,2,-5,42,3]
print(elemento_menor(lista))


#Ejercicio 4: Crear un script que imprima el volumen de una esfera por su radio 4/3* pi* r**3.

def volumen_esfera(radio):
    return (4/3*3.14*pow(radio,3))
print (volumen_esfera(4))    


#Ejercicio 5: Crear una script que indique si el usuario es mayor de edad.

def mayor_edad(edad):
    if(edad>=18):
        imp="Mayor de edad"
    else:
        imp="Menor de edad"
    return imp
print(mayor_edad(18))


#Ejercicio 6: Crear un Script que permita calcular si un número es par o impar.

def par_impar(num):
    if(num%2==0):
        imp="Número par"
    else:
        imp="Número impar"
    return imp
print(par_impar(24))


#Ejercicio 7: Crear un script que indique cuantas vocales tiene una palabra.

def contar_vocales(palabras):
    cont = 0
    for letra in palabras:
        if letra.lower() in "aeiou":
         cont += 1
    return cont
print(contar_vocales("Edificios"))

#Ejercicio 8: Crear un script que reciba una cantidad infinita de números hasta decir basta, luego que imprima la suma de los números ingresados.

def inf_parar(sum):
    num = input("Ingrese stop para parar, sino ingrese un numero \n")
    if(num == "stop"):
        return int(sum)
    else:
        return inf_parar(int(sum)+int(num))
print(inf_parar(0))

#Ejercicio 9:  crear un sistema de calificaciones
def calificacion(nota):
    if(nota==10 or nota>=9):
        valor="A"
    elif(nota<9 and nota>=8):
        valor="B"
    elif(nota<8 and nota>=7):
        valor="C"
    elif(nota<7 and nota>=6):
        valor="D"
    elif(nota<6 and nota>=0):
        valor="F"
    else:
        valor="Valor desconocido"

    return valor

print(calificacion(8.5))

# Ejercicio 10: Imprimir números de 5 a 1 de manera descendente

def num_des(num,cadena):
    if(num==0):
        return cadena
    else:
        return num_des(num-1,cadena+str(num)+"\n")
print(num_des(5,""))

# Ejercicio 11:Imprimir los números naturales del 0 al 10 utilizando un ciclo while

def num_while(num):
    cont=0
    while(cont<=num):
        print(cont)
        cont+=1

num_while(10)

#Ejercicio 12: Calcular el área y el perímetro de un Rectángulo

def area_perimetro(alto,ancho):
    return "Area = ",(int(alto)*int(ancho)),"Perimetro = ",(int(alto)+int(ancho))
print(area_perimetro(12,45))

#Ejercicio 13: terar un rango de 0 a 10 e imprimir sólo los números divisibles entre 3

def num_div_tres(rango):
    for x in range(1,rango):
        if(x%3==0):
            print(x)  

num_div_tres(11)

#Ejercicio 14:Presentar un string con el titulo y el autor de un libro

def presentar(titulo,autor):
    return "Titulo: "+titulo+" Autor: "+autor
print(presentar("Aprende Python en un Fin de Semana"," Alfredo Moreno Muñoz y Sheila Córcoles Córcoles")) 


#Ejercicio 15: Se debe imprimir el mayor de los dos números
def mayor():
    num1 = int(input("Proporciona el numero 1 \n"))
    num2 = int(input("Proporciona el numero 2 \n"))
    if(num1>num2):
        return "El numero mayor es ",num1
    else:
        return "El numero mayor es ",num2
print(mayor())
#Ejercicio 16: Dada la siguiente tupla, crear una lista que sólo incluya los números menor que 5 utilizando un ciclo for
def menor_cinco(tupla):
    listatupla=[]
    for x in tupla:
        if(x<5):
            listatupla.append(x)
    return listatupla

def recorrer(lista):
    for x in lista:
        print(x)
tupla = (13, 1, 8, 3, 2, 5, 8)
#recorrer(menor_cinco(tupla))

#Ejercicio 17: Crear un script que encuentre la potencia de un número ingresado por el teclado
def potencia():
    num1 = int(input("Proporciona un numero \n"))
    num2 = int(input("Proporciona la potencia \n"))
    return pow(num1,num2)
#print(potencia()) 

#Ejercicio 18: Dado dos números enteros, encontrar la suma

def suma(a,b):
    return a+b
print(suma(4,9))


#Ejercicio 19: Dado un número de 5 dígitos, devolver el número en orden inverso.
def invertir_numero(num):
    return str(num)[::-1]
print(invertir_numero(123456789))


#Ejercicio 20: Crear un script para saludar desde Python
def saludar():
    return "hola mundo"
print(saludar())
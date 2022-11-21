# 1: Define una función llamada menorque() que nos devuelva en pantalla el número
#menor entre dos enteros. Define una salida de texto en caso de que.

def menorque(a,b):
    if(a<b):
        mostrar=a, 'Es menor '
    else:
        mostrar=b, 'Es menor '
    return mostrar
#print(menorque(10,20)) 

# 2: Define una función llamada num_max() que nos devuelva en pantalla el número
#mayor entre 4 diferentes enteros. No definas ningún valor a imprimir en caso
#de que ambos números sean iguales.


def num_max(lista):
    mayor=lista[0]
    for x in range(1,len(lista)):
     if (lista[x]>mayor):
      mayor=lista[x]
    return(mayor)
lista=[5,-5,101,50]
print(num_max(lista))

# 3: Define una función llamada num_max_min() que nos devuelva en pantalla el
#número mayor y menor entre 3 diferentes enteros. En caso de que todos sean
#iguales imprime en pantalla un mensaje indicándolo.

def num_max_min(lista):
    empezar= lista[0]
    mayor = empezar
    menor = empezar
    for x in range(1,len(lista)):
        if(lista[x]>empezar):
            mayor=lista[x]
        else:
            menor=lista[x]
    return ("El mayor es",mayor,"y el Menor es",menor)

print(num_max_min([-5,10,25]))
    

#Ejercisio 4 Define una función llamada num_min() que nos devuelva en pantalla el número
#menor entre 3 diferentes enteros. En caso de que todos sean iguales imprime en
#pantalla un mensaje indicándolo.

num1=int(input("ingrese un numero"))
num2=int(input("ingrese un numero"))
num3=int(input("ingrese un numero"))
if num1 < num2 and num2 > num3 and num3 > num1:
    print(f"numero menor {numero1}")
else:
    print(f"numero menor {numero2}")
    
if num1 == num2 or num2 == num3:
    print("son numeros iguales")
else:
    print("no son numeros iguales")



#ejercisio 5 Define una función que nos devuelva True si al darle una vocal mayúscula nos
#devuelva False, mientras que si es minúscula sea True.

print("dime una vocal")
vocal=input()
if vocal == 'a' or vocal == 'e' or vocal == 'i' or vocal =='o' or vocal == 'u' :
    print("TRUE") 
elif vocal == 'A' or vocal == 'E' or vocal == 'I' or vocal =='O' or vocal == 'U':
    print("False")


#ejercisio 6 Define una función simple que no tenga parámetros y sólo imprima en pantalla
#un mensaje.


nombre = input("ingrese su nombre")
apellido = input("por favor ingrese su edad")
print("que tengas un excelente dia " (nombre+apellido));



#ejercisio 7 Define una función que permita imprimir un mensaje en base a los valores
#tomados de una lista para comprobar si todos los de la lista son mayores o
#menores de edad.

lista=[9,1,2,3,4,8,6,7]

def mayor (lista):
    min = lista[0]
    for x in lista:
        if x > min:
            min = x
            return min

def main(lista):
    print ("La lista es ", lista)    
    print ("El número mayor es: ", min(lista))
 
main(lista)


#ejercisio 8 Define una función que permita multiplicar los números de una lista y sumar
#sus resultados.

def multiplicar_lista(numeros):
    producto =1
    for numero in numeros:
        producto*= numero
    return producto
numeros=[1,2,3,4,5]
print(multiplicar_lista(numeros))





















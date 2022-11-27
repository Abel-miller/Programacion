#Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por 
#pantalla la frase invertida.

def invertir_cadena(cadena):
 inversa =''
 for x in cadena: 
  inversa = x + inversa 
 return (inversa) 
print("El unico modo de hacer un gran trabajo es amar lo que haces")
print(invertir_cadena("El unico modo de hacer un gran trabajo es amar lo que haces"))


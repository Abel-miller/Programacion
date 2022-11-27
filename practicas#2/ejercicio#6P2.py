#Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal
#y después muestre por pantalla la misma frase, pero con la vocal introducida en mayúscula.

def cambiar_vocales(frases,vocal):
    cadena=""
    for letra in frases:
      if letra.lower() in vocal:
        letra=letra.upper()
      cadena=cadena+letra
    return cadena
        
    
print(cambiar_vocales("El unico modo de hacer un gran trabajo es amar lo que haces","o"))
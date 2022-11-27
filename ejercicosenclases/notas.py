#Pedir una nota al usuario
#Si la nota es menor a 10 y mayor o igual o 9, imprimir Excelente.
#Si la nota es menor a 9 y mayor o igual 8, imprimir Muy bueno
def calificacion(nota):
    if(nota==10 and nota>=9):
        valor="Excelente"
    elif(nota<9 and nota>=8):
        valor="Muy bueno"
    elif(nota<8 and nota>=7):
        valor="Bueno"
    elif(nota<7 and nota>=0):
        valor="Reprobado"
    else:
        valor="Valor desconocido"
    return valor

print(calificacion(float(input("Ingrese la Nota: \n"))))
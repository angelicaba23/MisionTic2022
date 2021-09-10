"""
------------MinTic-----------------
-------------UPB-------------------
-------Angélica Barranco-----------
"""
#Calificacion de acuerdo a "El sistema de evaluación de una universidad"
#Entradas
nombre = input("Ingrese su nombre ")
ID = input("Ingrese el numero de identificacion ")
calificacion = float(input("Ingrese la calificacion "))
#Procesos
if(calificacion >= 4.5 and calificacion <=5.0):
 	Resultado = "A"
elif(calificacion >= 4.0 and calificacion <=4.4):
 	Resultado = "B"
elif(calificacion >= 3.5 and calificacion <=3.9):
 	Resultado = "C"
elif(calificacion >= 3.0 and calificacion <=3.4):
 	Resultado = "D"
elif(calificacion >= 2.5 and calificacion <=2.9):
 	Resultado = "E1"
elif(calificacion >= 2.0 and calificacion <=2.4):
 	Resultado = "E2"
elif(calificacion >= 1.5 and calificacion <=1.9):
 	Resultado = "E3"
elif(calificacion >= 1.0 and calificacion <=1.4):
 	Resultado = "E4"
#Salidas
print("El estudiante" , nombre, "identificado con el numer", ID, "tiene una calificacion de", calificacion, ". Su codificadion es", Resultado)
"""
------------MinTic-----------------
-------------UPB-------------------
-------Angélica Barranco-----------
"""

#Elaborar un algoritmo que solicite el número de respuestas correctas, incorrectas y en blanco, correspondientes a postulantes, y muestre su puntaje final considerando, que por cada respuesta correcta tendrá 4 puntos, respuestas incorrectas tendrá -1 y respuestas en blanco tendrá 0.
#entradas
correctas = int(input("Ingrase el número de respuestas correctas "))
incorrectas = int(input("Ingrase el número de respuestas incorrectas "))
blanco = int(input("Ingrase el número de respuestas en blanco "))
#proceso
resultado = 4*correctas + -1*incorrectas + 0*blanco
#salida
print("El puntaje es = ", resultado)

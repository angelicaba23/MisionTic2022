"""
------------MinTic-----------------
-------------UPB-------------------
-------Angélica Barranco-----------
"""

#Elabore un algoritmo que lea los 3 lados de un triángulo cualquiera y calcule su área, considerar: Si A, B y C son los lados, y S el semiperímetro.
import numpy as np
#Entradas
a = float(input("Digite el valor de a "))
b = float(input("Digite el valor de b "))
c = float(input("Digite el valor de c "))

# Procesos
s = (a +b + c) / 2
arg = s*(s-a)*(s-b)*(s-c)
area = np.sqrt(arg)

#Salida
print("El triangulo de lados a = ", a, ", b = ", b, " c = ", c, " tiene un semiperímetro = ", s, "y area = ", area)

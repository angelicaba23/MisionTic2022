"""
------------MinTic-----------------
-------------UPB-------------------
-------Angélica Barranco-----------
"""

#Calcular y visualizar la longitud de la circunferencia y el área de un círculo de radio dado

import numpy as np
r = float(input("Digite el valor de r "))

#Procesos
l = 2*np.pi*r
a = np.pi*r**2

#Salidas
print("La longitud de la circunferencia es = 2*pi*" , r," = ", l)
print("El area del circulo es = pi*" , r,"**2 = ", a)


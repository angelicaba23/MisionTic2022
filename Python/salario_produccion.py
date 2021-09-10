"""
------------MinTic-----------------
-------------UPB-------------------
-------Angélica Barranco-----------
"""
#Salario por produccion

nombre = input("Ingrese el nombre: ")
cantidad = int(input("Ingrese la producción (unidades) lograda a lo largo de la semana (lunes a sábado): "))

if cantidad >= 0 and cantidad <= 99:
    salario = cantidad * 2
    incentivo = 0
elif cantidad >= 100 and cantidad <= 299:
    salario = cantidad * 2
    incentivo = 0.10
elif cantidad >= 200 and cantidad <= 299:
    salario = cantidad * 2.5
    incentivo = 0.12
elif cantidad >= 300 and cantidad <= 399:
    salario = cantidad * 3
    incentivo = 0.14
elif cantidad >= 400:
    salario = cantidad * 3.5
    incentivo = 0.16

total = salario + salario*incentivo

print("El trabajador", nombre, "registro", cantidad, "de productos vendidos.")
print("Su salario es de", salario,"pesos, tiene un incentivo de",salario*incentivo,"pesos, y el pago total es de", total, "pesos.")
"""
------------MinTic-----------------
-------------UPB-------------------
-------Angélica Barranco-----------
"""

#Escribir un algoritmo que encuentre el salario semanal de un trabajador, dada la tarifa horaria y el número de horas trabajadas diariamente
#Entradas

valor_hora = int(input("Ingrese el valor hora del trabajador "))
horas_lunes = int(input("Ingrese horas laboradas el lunes "))
horas_martes = int(input("Ingrese horas laboradas el martes "))
horas_miercoles = int(input("Ingrese horas laboradas el miercoles "))
horas_jueves = int(input("Ingrese horas laboradas el jueves "))
horas_viernes = int(input("Ingrese horas laboradas el viernes "))
horas_sabado = int(input("Ingrese horas laboradas el sabado "))
#Procesos
horas_totales= horas_lunes + horas_martes + horas_miercoles + horas_jueves + horas_viernes + horas_sabado 
salario_semanal = horas_totales * valor_hora
#Salidas
print("El valor de la Hora es de ", valor_hora, "pesos")
print("El trabajador laboro", horas_totales, "horas en la semana")
print("Entonces, el salario semanal es de", salario_semanal, "pesos")

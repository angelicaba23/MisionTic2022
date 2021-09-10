"""
------------MinTic-----------------
-------------UPB-------------------
-------Angélica Barranco-----------
"""
#NOmina

#Entradas
nombre = input("Ingrese el nombre: ") 
id = input("Ingrese el numero de identificacion: ") 
salario = float(input("Ingrese el salario: "))
prestamo = int(input("Ingrese el valor del prestamo: "))
horario = input(("El trabajador tiene recargo nocturno si / no: "))
dias = int(input("Ingrese los el numero de dias trabajados: "))

extras = input("Tiene horas extras? si / no: ")
if extras == "si":
    hed = int(input("Ingrese el numero de horas extras diurnas: "))
    hen = int(input("Ingrese el numero de horas extras nocturnas: "))
    hefd = int(input("Ingrese el numero de horas extras festivas diurnas: "))
    hefn = int(input("Ingrese el numero de horas extras festivas nocturnas: "))
else:
    hed = 0
    hen = 0
    hef = 0
    hefd = 0
    hefn = 0

#Procesos
smlv = 908526
transporte = 10*smlv/100
if (salario <= 2*smlv):
	subsidio = 106454 / 30 * dias
else: 		
	subsidio = 0 
sueldo = salario / 30 * dias

vhed = salario / 240 * hed * 1.25
vhen = salario / 240 * hen * 1.35
vhefd = salario / 240 * hefd * 1.75
vhefn = salario / 240 * hefn * 2.1

if horario == "si":
    recargo_nocturno = salario * 0.35
else:
    recargo_nocturno = 0 
total_devengado =  sueldo + subsidio + vhed + vhen + vhefd + vhefn + recargo_nocturno 
salud = (total_devengado - subsidio) * 4 / 100
pension = (total_devengado - subsidio) * 4 / 100
#Fondo de Solidaridad 1% del salario, se le descuenta a los que ganen más de 4 mínimos: 3634104
if (salario >= 3634104):
	fondo = salario * 0.01
else: 		
	fondo = 0 
total_deducido = salud + pension + prestamo + fondo
neto_pagado = total_devengado - total_deducido

print("El trabajdor", nombre, "identificado con el numero", id, "trabajo", dias, "dias." )
print("El total deducido es = ", total_deducido )
print("El pago neto es = ", neto_pagado)
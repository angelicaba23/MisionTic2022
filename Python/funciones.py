

"""
------------MinTic-----------------
-------------UPB-------------------
-------Angélica Barranco-----------
"""

#Funciones

import math
start = "si"
while start == "si":
    print('Bienvenido. Este programa te permite ejecutar varias funciones: \n1. Valor absoluto. \n2. Función exponencial. \n3. Potencial.\n4. Raíz cuadrada. \n5. Coseno. \n6. Seno. \n7. Tangente.\n8. Arcoseno.\n9. Arcseno. \n10. Valor de pi.\n11. Valor de e.')
    op = int(input("Seleccione la función (Digite un numero del 1 al 11): "))
    if op == 3:
        b = float(input("Digite el valor del argumento (base) "))
        e = float(input("Digite el valor del argumento (exponente) "))
    elif op == 10 or op == 11:
        print("")
    else:
        arg = float(input("Digite el valor del argumento "))

#Procesos
    if op == 1:
        #Valor absoluto
        resultado = math.fabs(arg)
        texto = 'El valor absoluto de ' , arg ,' es ' , resultado
    elif op == 2:
        #Función exponencial
        resultado = math.exp(arg)
        texto = "La función exponencial de " , arg ," es " , resultado
    elif op == 3:
        #Potencial
        #math.pow(base,exponente)
        resultado = math.pow(b,e)
        texto = "El potencial de base " , b , " y exponente ", e ," es " , resultado
    elif op == 4:
        #raíz cuadrada
        resultado = math.sqrt(arg)
        texto = "La raíz cuadrada de ", arg ," es " , resultado
    elif op == 5:
        #Coseno de un ángulo medido en radianes
        resultado0 = math.cos(arg)
        #Conversión de radianes a grados
        resultado = math.degree(arg)
        texto = "El coseno de " , arg, " medido en radianes es " , resultado0 ," y en grados es " , resultado
    elif op == 6:
        #Seno de un ángulo medido en radianes
        resultado0 = math.sin(arg)
        #Conversión de radianes a grados
        resultado = math.degree(arg)
        texto = "El seno de " , arg, " medido en radianes es " , resultado0 ," y en grados es " ,resultado
    elif op == 7:
        #Tangente de un ángulo medido en radianes
        resultado0 = math.tan(arg)
        #Conversión de radianes a grados
        resultado = math.degree(arg)
        texto = "El Coseno de " , arg," medido en radianes es " , resultado0 ," y en grados es " , resultado
    elif op == 8:
        #Arcoseno de un valor (ángulo)
        resultado0 = math.acos(arg)
        #Conversión de radianes a grados
        resultado = math.degree(arg)
        texto = "El Coseno de " , arg, " medido en radianes es " , resultado0 ," y en grados es " , resultado
    elif op == 9:
        #Arcseno de un valor (ángulo)
        resultado0 = math.asin(arg)
        #Conversión de radianes a grados
        resultado = math.degree(arg)
        texto = "El Coseno de ", arg," medido en radianes es " , resultado0 ," y en grados es " , resultado
    elif op == 10:
        #Obtención de valor de pi
        resultado = math.pi
        texto = "El valor de pi es  " , resultado
    elif op == 11:
        #obtención de valor de e
        resultado = math.e
        texto = "El valor de e es " , resultado
    else:
        print("No ha seleccionado una función")
    #Salidas
    print(texto)
    start = input("Desea ir al menu? si / no ")

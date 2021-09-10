"""
------------MinTic-----------------
-------------UPB-------------------
-------Angélica Barranco-----------
"""
#Este Programa realiza las operaciones Matematicas
print ("Bienvenid@ a la Sesion de Operaciones Matematicas")
#Entradas
numero1 = int(input("Digite el primer numero"))
numero2 = int(input("Digite el segundo numero"))
numero3 = 10
#Procesos
suma = numero1 + numero2 + numero3
resta = numero1 - numero2 - numero3
producto = numero1 * numero2 * numero3
division = numero1 / numero2 / numero3
division_entera =  numero1 // numero2 // numero3
potencia = numero1 ** numero2 
residuo = numero1 % numero2 % numero3
negacion = -numero1 + -numero2 - -numero3
#Salidas
print ("Señor Usuario, Resultados de las Operaciones Matematicas")
print("El resultado de la suma es = ",numero1," + ",numero2, " + ",numero3, "=", suma)
print("El resultado de la resta es = ",numero1 ,"-", numero2 ,"-", numero3, "=", resta)
print("El resultado del producto es = ",numero1 ,"*", numero2 ,"*", numero3, "=", producto)
print("El resultado de la división decimal = ",numero1 ,"/", numero2 ,"/", numero3, "=", division)
print("El resultado de la división entera = ", numero1 ,"//", numero2 ,"//", numero3, "=", division_entera)
print("El resultado de la potencia es = ", numero1 ,"**", numero2 ,"=",potencia)
print("El resultado del residuo es = ", numero1 ,"%", numero2 ,"%", numero3, "=", residuo)
print("El resultado de la negación es = -", numero1 ,"+  -", numero2 ,"- -", numero3, "=", negacion)
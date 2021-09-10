# Compara tres (3) numeros y dice cual es central

# Entradas
num1 = int(input("Ingrese el valor del primer numero "))
num2 = int(input("Ingrese el valor del segundo numero "))
num3 = int(input("Ingrese el valor del tercer numero "))

# Proceso
#Num 1 central

if num1 > num2 and num1 < num3:
    central = num1
    mayor = num3
    menor = num2
    b = "Hemos encontrado un numero central"

elif num1 > num3 and num1 < num2:
    central = num1
    mayor = num2
    menor = num3
    b = "Hemos encontrado un numero central"

#Num 2 central
elif num2 > num1 and num2 < num3:
    central = num2
    mayor = num3
    menor = num1
    b = "Hemos encontrado un numero central"
elif num2 > num3 and num2 < num1:
    central = num2
    mayor = num1
    menor = num3
    b = "Hemos encontrado un numero central"

#Num 3 central
elif num3 > num1 and num3 < num2:
    central = num3
    mayor = num2
    menor = num1
    b = "Hemos encontrado un numero central"

elif num3 > num2 and num3 < num1:
    central = num3
    mayor = num1
    menor = num2
    b = "Hemos encontrado un numero central"

elif num1 == num2 == num3:
    print("Los tres números son iguales")
    central = "Nan"
    mayor = "Nan"
    menor = "Nan"
elif num1 == num2:
    print("Hay dos numeros iguales")
    central = "Nan"
    mayor = "Nan"
    menor = "Nan"
elif num3 == num2:
    print("Hay dos numeros iguales")
    central = "Nan"
    mayor = "Nan"
    menor = "Nan"
elif num1 == num3:
    print("Hay dos numeros iguales")
    central = "Nan"
    mayor = "Nan"
    menor = "Nan"

   
print ("El numero mayor es ", mayor)
print ("El numero central es ", central)
print ("El numero menor es ", menor)

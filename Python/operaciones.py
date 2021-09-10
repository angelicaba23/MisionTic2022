"""
------------MinTic-----------------
-------------UPB-------------------
-------Angélica Barranco-----------
"""
#Realiza op matematicas
import numpy as np
start = "si"
while start == "si":
    op = int(input("Seleccione la operación (Digite un numero del 1 al 5):  "))
    if op == 1:
        M = int(input("Digite el valor de M "))
        N = int(input("Digite el valor de N "))
        P = int(input("Digite el valor de P "))
        if N == 0:
            N = int(input("Digite un valor de N diferente de O "))
    elif op ==2:
        M = int(input("Digite el valor de M "))
        N = int(input("Digite el valor de N "))
        P = int(input("Digite el valor de P "))
        Q = int(input("Digite el valor de Q "))

    elif op ==3:
        m = int(input("Digite el valor de m "))
        n = int(input("Digite el valor de n "))
        p = int(input("Digite el valor de p "))
        q = int(input("Digite el valor de q "))
        r = int(input("Digite el valor de r "))
        if p == 0:
            p = int(input("Digite un valor de p diferente de O"))
        if q-r/5 == 0:
            p = int(input("Digite un valor de p diferente de O"))
    elif op == 4:
        m = int(input("Digite el valor de m "))
        n = int(input("Digite el valor de n "))
        p = int(input("Digite el valor de p "))
        q = int(input("Digite el valor de q "))
        
    elif op == 5: 
        a = int(input("Digite el valor de a "))
        b = int(input("Digite el valor de b "))
        c = int(input("Digite el valor de c "))
    else:
        print("")
        #start = input("Desea ir al menu?? si / no : ")

#Procesos
    if op == 1:
        op1 = M / N + P
    elif op == 2:
        op2 = M + N / (P + Q) 
    elif op == 3:
        op3 = (m + n / p) / (q - r / 5)
    elif op == 4:
        if p == q:
            print("")
        else:
            op4 = (m + n) / (p - q)
    elif op == 5:
        op5 = (-b + np.sqrt(b**2 - (4 * a * c))) / 2 * a
    else:
        print("")
    #Salidas
    if op == 1:
        print("El resultado de M / N + P = " , M, "/", N ,"+", P, " = ", op1)
    elif op == 2:
        print("El resultado de M / N + P = " , M ,"+", N,"/","(",P ,"+", Q,")", " = ", op2)
    elif op == 3:
        print("El resultado de M / N + P = " , "(", m , "+", n ,"/", p ,")", "/ (", q, "-", r ,"/", 5, ") = ", op3)
    elif op == 4:
        if p == q:
            print("Operacion no valida con los datos ingresados")
        else:
            print("El resultado de M / N + P =  (" , m ,"+", n, ") / ( ", p ,"-", q, ") = ", op4)
    elif op == 5:
        print("El resultado de M / N + P = ( -" , b ,"+", np.sqrt(b**2 - (4 * a * c)) ,") /", 2 ,"*", a, " = ", op5)
    else:
        print("")
    start = input("Desea ir al menu? si / no ")
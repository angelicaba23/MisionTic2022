"""
------------MinTic-----------------
-------------UPB-------------------
-------Angélica Barranco-----------
"""

print(" \t Bienvenido al menu de programas desarrollado con Python")
op0 = "Todas las operaciones matematicas"
op1 = "Area del triangulo"
op2 = "Superficie del triangulo"
op3 = "Circunferencia (area y longitud)"
op4 = "Funciones"
op5 = "Operadores de asignacion"
op6 = "Operaciones"
op7 = "Salario Semanal"
op8 = "Salario por producción"
op9 = "Codificación segun el puntaje"
op10 = "Calificación segun preguntas"
op11 = "Numero central"
op12 = "Nomina"
menu = True
while menu  == True:
    menu = False
    print("\n\t------ menú de opciones ------ \n\t1. {} \n\t2. {} \n\t3. {} \n\t4. {} \n\t5. {} \n\t6. {} \n\t7. {} \n\t8. {} \n\t9. {} \n\t10. {} \n\t11. {} \n\t12. {} \n\t13. {}".format(op0,op1,op2,op3,op4,op5,op6,op7,op8,op9,op10,op11,op12))
    op = int(input("\n\t Elija una opción "))
    if op == 1:
        print("Usted ha elegido la opción 1. " + op0)
        import operaciones_mathe
    elif op == 2:
        print("Usted ha elegido la opción 2. " + op1)
        import area_triangulo
    elif op == 3:
        print("Usted ha elegido la opción 3. " + op2)
        import superficie_triángulo
    elif op == 4:
        print("Usted ha elegido la opción 4. " + op3)
        import circunferencia
    elif op == 5:
        print("Usted ha elegido la opción 5. " + op4)
        import funciones
    elif op == 6:
        print("Usted ha elegido la opción 6. " + op5)
        import operadores_asignacion
    elif op == 7:
        print("Usted ha elegido la opción 7. " + op6)
        import operaciones
    elif op == 8:
        print("Usted ha elegido la opción 8. " + op7)
        import salario_semanal
    elif op == 9:
        print("Usted ha elegido la opción 9. " + op8)
        import salario_produccion
    elif op == 10:
        print("Usted ha elegido la opción 10. " + op9)
        import calificacion
    elif op == 11:
        print("Usted ha elegido la opción 11. " + op10)
        import puntaje
    elif op == 12:
        print("Usted ha elegido la opción 12. " + op11)
        import num_central
    elif op == 13:
        print("Usted ha elegido la opción 13. " + op12)
        import nomina
    else:
        print("Error")
        menu = True
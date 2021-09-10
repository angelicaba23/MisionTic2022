"""
------------MinTic-----------------
-------------UPB-------------------
-------Angélica Barranco-----------
"""
#factura

num_factura = 0

menu = "si"
while menu == "si":
    print("\nBienvenido al sistema de calificacion")
    nota_a = 0
    nota_b = 0
    nota_c = 0
    nota_d = 0
    nota_f = 0
    c_f = 0
    c_d = 0
    c_c = 0
    c_b = 0
    c_a = 0
    menu2= "si"
    curso = input("\nIngrese el curso: ")
    estudiante = int(input("\nIngrese el numero de estudiantes: "))
    
    for i in range(estudiante):
        grado  = 200
        while grado not in range(101):
            grado = int(input(f"\nIngrese la calificacion en grado numerico [0-100] del estudiante {i+1}: "))
        else:
            pass
        if grado < 60:
            letra = "F"
            nota_f = nota_f + grado 
            c_f = c_f+ 1
        elif  60 <= grado < 70:
            letra = "D"
            nota_d+= grado 
            c_d += 1
        elif  70 <= grado < 80:
            letra = "C"
            nota_c += grado 
            c_c += 1
        elif  80 <= grado < 90:
            letra = "B"
            nota_b += grado 
            c_b += 1
        elif grado >= 90:
            letra = "A"
            nota_a += grado 
            c_a += 1
        else:
            letra=""
        print(f"\n\tEstudiante {i+1} : {letra}")
    if c_f != 0:
        promedio_f = nota_f / c_f
    else:
        promedio_f = 0
    if c_d != 0:
        promedio_d = nota_d / c_d
    else:
        promedio_d = 0
    if c_c != 0:
        promedio_c = nota_c / c_c
    else:
        promedio_c = 0
    if c_b != 0:
        promedio_b = nota_b / c_b
    else:
        promedio_b = 0
    if c_a != 0:
        promedio_a = nota_a / c_a
    else:
        promedio_a = 0

    promedio = (nota_f+nota_a+nota_b+nota_c+nota_d)/estudiante
    print(f"\n\t--------- CURSO {curso} ----------")
    print(f"\n\t\t\t\t PROMEDIO")
    print(f"\n\t A \t\t\t {promedio_a}")
    print(f"\n\t B \t\t\t {promedio_b}")
    print(f"\n\t C \t\t\t {promedio_c}")
    print(f"\n\t D \t\t\t {promedio_d}")
    print(f"\n\t F \t\t\t {promedio_f}")
    print(f"\n\t CURSO \t\t\t {promedio}")

    menu = input("\n Desea agregar notas de un nuevo curso? si/no: ")
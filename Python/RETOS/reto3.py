"""
------------MinTic-----------------
-------------UPB-------------------
-------Angélica Barranco-----------
------------RETO 3-----------------
"""
#import numpy as np

#Funciones--------------------------

def verf(arg1,arg2):
    if arg1 in arg2:
        return
    else:
        print("\nError coordenada")
        exit()
        

        
    """
    Sup = 2.766
    Inf = 2.548
    Or = -76.493 
    Occ = -76.879
    step =0.001
    if arg1 in np.arange(Inf, Sup+step,step ):
        pass
        if arg2 in np.arange(Occ,Or+step,step):
            return
        else:print("\nError coordenada")
        exit()
    else:print("\nError coordenada")
    exit()
    """
    

def sur_ori(arg):
    c1 = arg[0]
    c2 = arg[1]
    c3 = arg[2]
    sur = 0
    if c1[0]<c2[0] and c1[0]<c3[0]:
        sur = 1
    elif c2[0]<c1[0] and c2[0]<c3[0]:
        sur = 2
    elif c3[0]<c1[0] and c3[0]<c2[0]:
        sur = 3
    else:
        print("Hay dos coordenadas 'más' al sur")
        if c3[0]==c1[0] or c3[0]==c2[0]:
            sur = 3
        else:
            sur = 1
        
    ori = 0
    if c1[1]>c2[1] and c1[1]>c3[1]:
        ori = 1
    elif c2[1]>c1[1] and c2[1]>c3[1]:
        ori = 2
    elif c3[1]>c1[1] and c3[1]>c2[1]:
        ori = 3
    else:
        print("Hay dos coordenadas 'más' al oriente")
        if c3[1]==c1[1] or c3[1]==c2[1]:
            ori = 3
        else:
            ori = 1
        
    return sur, ori

    



#------------------------------------
# Requisitos funcionales:
#RF01
print("\nBienvenido al sistema de ubicación para zonas públicas WIFI")
#RF02
correct_user = 51745
correct_password = 54715
user = int(input("\nIngrese el nombre de usuario: "))
if user == correct_user:
    password = int(input("Ingrese la contraseña: "))
    if password == correct_password:
        #RF03
        num1 = 745
        num2 = int((7*5) % (5/1) + 4)
        correct_captcha = num1 + num2
        captcha = int(input(f"Verificacion del captcha: {num1} + {num2} = "))
        if captcha == correct_captcha:
            print("\nSesión iniciada")
            menu =  True
            coordenadas_ok = False
            while menu == True:
                op1 = "Cambiar contraseña"
                op2 = "Ingresar coordenadas actuales"
                op3 = "Ubicar zona wifi más cercana"
                op4 = "Guardar archivo con ubicación cercana"
                op5 = "Actualizar registros de zonas wifi desde archivo"
                op6 = "Elegir opción de menú favorita"
                op7 = "Cerrar sesión"
                options = [op1, op2, op3, op4, op5, op6,op7]
                menu_op = "\n\t------ menú de opciones ------ \n\t1. {0[0]} \n\t2. {0[1]} \n\t3. {0[2]} \n\t4. {0[3]} \n\t5. {0[4]} \n\t6. {0[5]} \n\t7. {0[6]}".format(options)
                print (menu_op)
                menu2 =  True
                while menu2 == True:
                    #menu2 = False
                    counter = 0
                    while counter < 3:
                        op = int(input("\n\t Elija una opción "))
                        if op in range(1,8):
                            print(f"\nUsted ha elegido la opción {op}")
                            op -= 1
                            if options[op] == "Cambiar contraseña":
                                passw = int(input("\n\t Ingrese la contraseña actual:"))
                                if passw == correct_password:
                                    passw = False
                                    while passw == False:
                                        correct_passwordn = int(input("\n\t Ingrese la contraseña nueva:"))
                                        if correct_password == correct_passwordn:
                                            print("Las contraseña nueva no puede ser igual a la antigua")
                                            passw = False
                                        else:
                                            correct_password = correct_passwordn
                                            print (menu_op)
                                            passw = True
                                else: 
                                    print("Error")
                                    exit() 
                            elif options[op] == "Ingresar coordenadas actuales":
                                if coordenadas_ok:
                                    filas = 1
                                    print(f"\ncoordenada 1 (latitud, longitud) : {coordenadas[0]}")
                                    print(f"coordenada 2 (latitud, longitud) : {coordenadas[1]}")
                                    print(f"coordenada 3 (latitud, longitud) : {coordenadas[2]}")
                                    #defcoor()
                                    ori = "2"
                                    s_o = sur_ori(coordenadas)
                                    #print(s_o ,s_o[1],s_o[0])
                                    print(f"\nLa coordenada {s_o[0]} ubicada más al sur")
                                    print(f"La coordenada {s_o[1]} ubicada más al oriente")
                                    print(f"\nPresione 1 , 2 ó 3 para actualizar la respectiva coordenada.\nPresione 0 para regresar al menú")
                                    ops = input()
                                    if ops == "0":
                                        print (menu_op)
                                        menu2 =  False
                                    elif ops == "1":
                                        c = 0
                                        menu2 =  True
                                    elif ops == "2":
                                        c = 1
                                        menu2 =  True
                                    elif ops == "3":
                                        c = 2
                                        menu2 =  True
                                    else:
                                        print("Error actualización")
                                        exit()
                                else:
                                    filas = 3
                                    c = 0
                                    coordenadas = [(),(),()]
                                if menu2:
                                    Sup = 2.766
                                    Inf = 2.548
                                    Or = -76.493 
                                    Occ = -76.879
                                    lats = []
                                    longs = []
                                    #print(Sup-Inf)
                                    #print(Or-Occ)
                                    x = 0
                                    for i in range(219):
                                        lats.append(round(Inf+x,3))
                                        #longs.append(round(Occ+c,3))
                                        x +=0.001
                                    x = 0
                                    for i in range(387):
                                        #lats.append(round(Inf+c,3))
                                        longs.append(round(Occ+x,3))
                                        x +=0.001
                                    #print(lats)
                                    #print(longs)
                                    #c = 0
                                    for i in range(filas):
                                        try:
                                            latitud = float(input(f"\n\tIngrese la latitud {c+1}: "))
                                            verf(latitud,lats)
                                            longitud = float(input(f"\n\tIngrese la longitud {c+1}: "))
                                            verf(longitud,longs)
                                        except:
                                            #print("Error")
                                            exit()
                                        coordenadas[c] = (latitud, longitud)
                                        c += 1
                                    coordenadas_ok = True
                                    #print (coordenadas)
                                    print (menu_op)
                                else: pass
                            elif options[op] == "Ubicar zona wifi más cercana":
                                pass
                                print (menu_op)
                            elif options[op] == "Guardar archivo con ubicación cercana":
                                pass
                                print (menu_op)
                            elif options[op] == "Actualizar registros de zonas wifi desde archivo":
                                pass
                                print (menu_op)
                            elif options[op] == "Elegir opción de menú favorita":
                                opfav = int(input("Seleccione opción favorita "))
                                opfavs = range(1,6)
                                if opfav in opfavs:
                                    adivinanza1 = int(input("Para confirmar por favor responda: Soy un número, y no miento, que tengo forma de asiento: "))
                                    if adivinanza1 == int(str(correct_user)[3]):
                                        adivinanza2 = int(input("Para confirmar por favor responda: Cuéntame las manos o cuéntame los pies y en seguida labrás que número es: "))
                                        if adivinanza2 == int(str(correct_user)[4]):
                                            menu = False
                                            if opfav == 1:
                                                options = [options[0], options[1],options[2], options[3], options[4], op6,op7]
                                                menu_op = "\n\t------ menú de opciones ------ \n\t1. {0[0]} \n\t2. {0[1]} \n\t3. {0[2]} \n\t4. {0[3]} \n\t5. {0[4]} \n\t6. {0[5]} \n\t7. {0[6]}".format(options)
                                                print (menu_op)
                                                menu2 = True
                                            elif opfav == 2:
                                                options = [options[1], options[0],options[2], options[3], options[4], op6,op7]
                                                menu_op = "\n\t------ menú de opciones ------ \n\t1. {0[0]} \n\t2. {0[1]} \n\t3. {0[2]} \n\t4. {0[3]} \n\t5. {0[4]} \n\t6. {0[5]} \n\t7. {0[6]}".format(options)
                                                print (menu_op)
                                                menu2 = True                                    
                                            elif opfav == 3:
                                                options = [options[2], options[1],options[0], options[3], options[4], op6,op7]
                                                menu_op = "\n\t------ menú de opciones ------ \n\t1. {0[0]} \n\t2. {0[1]} \n\t3. {0[2]} \n\t4. {0[3]} \n\t5. {0[4]} \n\t6. {0[5]} \n\t7. {0[6]}".format(options)
                                                print (menu_op)
                                                menu2 = True  
                                            elif opfav == 4:
                                                options = [options[3], options[1],options[2], options[0], options[4], op6,op7]
                                                menu_op = "\n\t------ menú de opciones ------ \n\t1. {0[0]} \n\t2. {0[1]} \n\t3. {0[2]} \n\t4. {0[3]} \n\t5. {0[4]} \n\t6. {0[5]} \n\t7. {0[6]}".format(options)
                                                print (menu_op)
                                                menu2 = True  
                                            elif opfav == 5:
                                                options = [options[4], options[1],options[2], options[3], options[0], op6,op7]
                                                menu_op = "\n\t------ menú de opciones ------ \n\t1. {0[0]} \n\t2. {0[1]} \n\t3. {0[2]} \n\t4. {0[3]} \n\t5. {0[4]} \n\t6. {0[5]} \n\t7. {0[6]}".format(options)
                                                print (menu_op)
                                                menu2 = True  
                                            else:
                                                pass
                                        else:
                                            print("Error")
                                            menu = True
                                    else:
                                        print("Error")
                                        menu = True
                                else:
                                    print("Error")
                            elif options[op] == "Cerrar sesión":
                                print("\n\tHasta pronto")
                                exit() 
                            else:
                                pass
                        else:
                            print("Error")
                            counter += 1    
                    else:
                        exit() 
                else:
                    pass
            else:
                pass
        else:
            print("Error")
    else:
        print("Error")   
else:
    print("Error")

#funciones


    

    
    
 
 

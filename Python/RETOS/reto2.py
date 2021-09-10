"""
------------MinTic-----------------
-------------UPB-------------------
-------Angélica Barranco-----------
------------RETO 2-----------------
"""

# Requisitos funcionales:
#RF01
print("\nBienvenido al sistema de ubicación para zonas públicas WIFI")
#RF02
corect_user = 51745
corect_password = 54715
user = int(input("\nIngrese el nombre de usuario: "))
if user == corect_user:
    password = int(input("Ingrese la contraseña: "))
    if password == corect_password:
        #RF03
        num1 = 745
        num2 = int((7*5) % (5/1) + 4)
        corect_captcha = num1 + num2
        captcha = int(input(f"Verificacion del captcha: {num1} + {num2} = "))
        if captcha == corect_captcha:
            print("\nSesión iniciada")
            menu =  True
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
                    menu2 = False
                    counter = 0
                    while counter < 3:
                        op = int(input("\n\t Elija una opción "))
                        if op in range(1,8):
                            print(f"\nUsted ha elegido la opción {op}")
                            op -= 1
                            if options[op] == "Cambiar contraseña":
                                exit()
                            elif options[op] == "Ingresar coordenadas actuales":
                                exit()
                            elif options[op] == "Ubicar zona wifi más cercana":
                                exit()
                            elif options[op] == "Guardar archivo con ubicación cercana":
                                exit()
                            elif options[op] == "Actualizar registros de zonas wifi desde archivo":
                                exit()
                            elif options[op] == "Elegir opción de menú favorita":
                                opfav = int(input("Seleccione opción favorita "))
                                opfavs = range(1,6)
                                if opfav in opfavs:
                                    adivinanza1 = int(input("Para confirmar por favor responda: Soy un número, y no miento, que tengo forma de asiento: "))
                                    if adivinanza1 == int(str(corect_user)[3]):
                                        adivinanza2 = int(input("Para confirmar por favor responda: Cuéntame las manos o cuéntame los pies y en seguida labrás que número es: "))
                                        if adivinanza2 == int(str(corect_user)[4]):
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
                                    exit()
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


    

    
    
 
 

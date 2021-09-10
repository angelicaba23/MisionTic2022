"""
------------MinTic-----------------
-------------UPB-------------------
-------Angélica Barranco-----------
------------RETO 4-----------------
"""
import numpy as np

#Funciones--------------------------
def verf(arg1,arg2):
    if arg1 in arg2:
        return
    else:
        print("\nError coordenada")
        exit()

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


def distancia(arg):
  zona = [[2.698,-76.680,63],[2.,-76.494,20],[2606.549,-76.742,680],[2.698,-76.690,15]]
  zona_wifi = zona
  lat = arg[0]
  lon = arg[1]
  R = 6372.795477588 
  dis = []
  for zona_wifi in zona_wifi:
      lat2 = zona_wifi[0]
      lon2 = zona_wifi[1]
      x = ((np.sin((lat2-lat)/2))**2)+np.cos(lat)*np.cos(lat2)*((np.sin((lon2-lon)/2))**2)
      d = 2*R*np.arcsin(np.sqrt(x))
      d = abs(d)
      dis.append(d)
  dis_o =sorted(dis)
  menor = dis.index(dis_o[0])
  medio = dis.index(dis_o[1])
  zmenor = zona[menor]
  zmedio =zona[medio]
  r = [(dis[menor],zmenor[:2],zmenor[2]),(dis[medio], zmedio[:2], zmedio[2])]
  return r

def findHemisferio():
    global hemisferio
    if lati < 0:
        hemisferio = "sur"
    else:
        hemisferio = "norte"
    return

def promedioLatis():
    global prom
    suma = sum(latis)
    prom = suma/numLatis
    return

def findHuso():
    global huso
    if longi < 81.296 and longi > -67.401:
        huso = -5
    elif longi < 67.402 and longi > -54.316:
        huso = -4
    elif longi < 54.316 and longi > -35.833:
        huso = -3
    else: pass
    return
#------------------------------------
# Requisitos funcionales:
#RF01
print("\nBienvenido al sistema de ubicación para zonas públicas WIFI")
#RF02
coordenadas = [(),(),()]
ubicacion = 0
correct_user = 51745
correct_password = 54715
user = input("\nIngrese el nombre de usuario: ")
if user == "Tripulante2022":
    print("\nEste fue mi primer programa y vamos por más")
    exit()
elif int(user) == correct_user:
    password = input("Ingrese la contraseña: ")
    if password == "m1s10nt1c":
        numLatis = int(input("Cunatas latitudes desea ingresar: "))
        latis = []
        for i in range(numLatis):
            l = int(input(f"Ingrese la latitud {i+1}: "))
            latis.append(l)
        promedioLatis()
        print(prom)
    elif int(password) == correct_password:
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
                        if op == 2021:
                            lati = int(input("Ingrese la latitud"))
                            findHemisferio()
                            print(f"Usted está en hemisferio {hemisferio}")
                            exit()
                        else: pass
                        if op == 2022:
                            longi = int(input("Escribe una la coordenada de una longitud en Sudamérica y te diré su huso horario: "))
                            findHuso()
                            print(f"El huso horario es {huso}")
                            exit()
                        else: pass
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
                                #zona_wifi = [(2.548,-76.492,10),(2.549,-76.493,20),(2.55,-76.494,30)]
                                if coordenadas == [(),(),()]:
                                    print("\nError sin registro de coordenadas")
                                    exit()
                                else:
                                    print(f"\ncoordenada 1 (latitud, longitud) : {coordenadas[0]}")
                                    print(f"coordenada 2 (latitud, longitud) : {coordenadas[1]}")
                                    print(f"coordenada 3 (latitud, longitud) : {coordenadas[2]}")
                                    ubicacion  = input(f"\nPor favor elija su ubicación actual (1, 2 ó 3) para calcular la distancia a los puntos de conexión: ")
                                    if ubicacion == "1" or ubicacion == "2" or ubicacion == "3":
                                        ubicacion = int(ubicacion)
                                        ubicacion-=1
                                        coordenada_actual = coordenadas[ubicacion]
                                        r = distancia(coordenada_actual)
                                        r0 = r[0]
                                        r1 = r[1]
                                        #print(r0)
                                        print("\n - - - - - - - - - - - - Zonas wifi con menos usuarios - - - - - - - - - - -")
                                        print(f"Zona wifi 1: ubicada en {r0[1]} a {round(r0[0],4)} metros, tiene en promedio {r0[2]} usuarios")
                                        print(f"Zona wifi 2: ubicada en {r1[1]} a {round(r1[0],4)} metros, tiene en promedio {r1[2]} usuarios")
                                        opp  = input(f"\nPor favor elija 1 o 2 para recibir indicaciones de llegada: ")
                                        if opp == "1" or opp == "2":
                                            if opp == "1":
                                                print(f"\nPara llegar a la zona wifi dirigirse primero al norte y luego hacia el oriente.")
                                                d = round(r0[0],4)
                                                v = 19.44
                                                t = round(d/v,4)
                                                print(f"\n -Tiempo en moto: {t} segundos")
                                                v = 0.483
                                                t = round(d/v,4)
                                                print(f" -Tiempo a pie: {t} segundos")
                                            else:
                                                print(f"\nPara llegar a la zona wifi dirigirse primero al oriente y luego hacia el norte.")
                                                d = round(r1[0],4)
                                                v = 19.44
                                                t = round(d/v,4)
                                                print(f"\n -Tiempo en moto: {t} segundos")
                                                v = 0.483
                                                t = round(d/v,4)
                                                print(f" -Tiempo a pie: {t} segundos")
                                            ops  = input(f"\nPresione 0 para salir: ")
                                            if ops == "0":
                                                print(menu_op)

                                        else:
                                            print("\nError zona wifi")
                                            exit()
                                    else:
                                        print("\nError ubicación")
                                        exit()
                            elif options[op] == "Guardar archivo con ubicación cercana":
                                if coordenadas == [(),(),()] or ubicacion == 0:
                                    print("\nError de alistamiento")
                                    exit()
                                else :
                                    #informacion={"actual": [latitud’, ‘longitud’],"zonawifi1":[‘latitud’,‘longitud’, usuarios], "recorrido:"[‘distancia’, ‘mediotransporte’, ‘tiempopromedio’]}
                                    informacion={"actual": [coordenadas[ubicacion]],"zonawifi1":[r0[1], r0[2]],"recorrido":[round(r0[0],4), "moto", t]}
                                    print(informacion)
                                    ex = input(print("\nEstá de acuerdo con la información a exportar? \nPresione 1 para confirmar. \nPresione 0 para regresar al menú principal  "))
                                    #ex = input()
                                    if ex  == "0":
                                        print(menu_op)
                                    elif ex == "1":
                                        print("\nExportando archivo")
                                        exit()
                                    else: 
                                        print (menu_op)
                            elif options[op] == "Actualizar registros de zonas wifi desde archivo":
                                #documento = input("Ingresar ubicacion de archivo")
                                #documento = np.loadtxt(documento)
                                doc = input(f"\nDatos de coordenadas para zonas wifi actualizados, \npresione 0 para regresar al menú principal")
                                if doc == "0":
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


    

    
    
 
 

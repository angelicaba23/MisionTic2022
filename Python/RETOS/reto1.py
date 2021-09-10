"""
------------MinTic-----------------
-------------UPB-------------------
-------Angélica Barranco-----------
------------RETO 1-----------------
"""
# Requisitos funcionales:
#RF01
print("Bienvenido al sistema de ubicación para zonas públicas WIFI")
#RF02
corect_user = 51745
corect_password = 45715
user = int(input("\nIngrese el nombre de usuario: "))
if user == corect_user:
    password = int(input("Ingrese la contraseña: "))
    if password == corect_password:
        #RF03
        num1 = 745
        num2 = int((7*5) % (5/1) + 5)
        corect_captcha = num1 + num2
        captcha = int(input(f"Verificacion del captcha: {num1} + {num2} = "))
        if captcha == corect_captcha:
            print("\nSesión iniciada")
        else:
            print("Error")
    else:
        print("Error")   
else:
    print("Error")
    

    
    
 
 

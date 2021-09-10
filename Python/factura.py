"""
------------MinTic-----------------
-------------UPB-------------------
-------Angélica Barranco-----------
"""
#factura

num_factura = 0

menu = "si"
while menu == "si":
    print("\n\tBienvenido a la tienda PY")
    num_factura += 1
    l = 0
    codigo_a = []
    producto_a=[]
    precio_a =[]
    cantidad_a = []
    subtotal_a = []
    total = 0
    subtotal = 0
    nombre = input("\n\tIngrese el nombre: ") 
    id = input("\n\tIngrese el numero de identificacion: ")

    menu2 = "si"
    while menu2 == "si":
        codigo  = 11
        while codigo not in range(11):
            codigo = int(input("\n\tIngrese el codigo del producto: "))
        else:
            pass
        lista = ["iPhone 8","iPhone XR","iPhone X", "iPhone 11", "iPhone 12", "iPad Pro", "iPad Air", "iMac", "Macbook Pro", "Airpods"]
        precio = [100, 200, 300, 400,500, 600, 700, 800,900,200]
        producto = lista[codigo-1]
        print(f"\n\tCuantos {producto} desea comprar?: ")
        cantidad = int(input("\n\t"))
        subtotal += cantidad*precio[codigo-1]
        subtotal_p = cantidad*precio[codigo-1]
        total += subtotal*1.19
        print(f"\n\t----------------- FACTURA # {num_factura} ------------------")
        print(f"\tCliente:\t\t\t\t{nombre}")
        print(f"\tID: \t\t\t\t\t{id}")
        print(f"\n\tCODIGO \t\tPRODUCTO \t\tPRECIO")
        codigo_a.append(codigo)
        producto_a.append(producto)
        cantidad_a.append(cantidad)
        precio_a.append(precio[codigo-1])
        subtotal_a.append(subtotal_p)
        for i in range(l+1):
            print(f"\t{codigo_a[i]} \t\t({cantidad_a[i]}){producto_a[i]} \t\t{precio_a[i]} - {subtotal_a[i]}")
        print(f"\n\tSubotal: \t\t\t\t{subtotal}")
        print(f"\n\tTotal: \t\t\t\t\t{total}")
        l += 1
        menu2  = input("\nDesea comprar otro producto? si /no: ")
    menu = input("\n Nuevo cliente? si/no: ")
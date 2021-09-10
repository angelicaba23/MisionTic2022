pregunta = "y"
i = 1
lista = []

while pregunta == "y":
    pregunta = input("Desea ingresar un nuevo numero? (y/n): ")
    numero = float(input(f"Ingrese el numero {i}: "))
    i +=1
    lista.append(numero)

lista_pos = []
lista_neg = []
lista_par = []
lista_impar = []

#------------------------------------------------------------------------------------------------
print(f"\nLista completa = ")
if lista != None:
    arg = lista
    print(f"\n\t{arg}")
    print(f"\n\tTamaño = {len(arg)}")
    print(f"\n\tSuma = {sum(arg)}")
    print(f"\n\tMaximo = {max(arg)}")
    print(f"\n\tMinimo = {min(arg)}")
    print(f"\n\tPromedio = {sum(arg)/len(arg)}")
    l = 1
    for arg in arg:
        l = l *arg
    print(f"\n\tProducto = {l}")
else: print("Error")

#--------------------------------------------------------------------------------------------------

for lista in lista:
    if lista%2 ==0:
        lista_par.append(lista)
    else:
        lista_impar.append(lista)
    if lista < 0:
        lista_neg.append(lista)
    else:
        lista_pos.append(lista)

#------------------------------------------------------------------------------------------------
todas_listas = [lista_par,lista_impar,lista_neg,lista_pos]
nombre_listas = ["Pares","Impares","Negativos","Positivos"]
i=0
for todas_listas in todas_listas:
    arg = todas_listas
    print(f"\nLista de {nombre_listas[i]}")
    i +=1
    if len(arg) != 0:    
        print(f"\n\t{arg}")
        print(f"\n\tTamaño = {len(arg)}")
        print(f"\n\tSuma = {sum(arg)}")
        print(f"\n\tMaximo = {max(arg)}")
        print(f"\n\tMinimo = {min(arg)}")
        print(f"\n\tPromedio = {sum(arg)/len(arg)}")
        l = 1
        for arg in arg:
            l = l *arg
        print(f"\n\tProducto = {l}")
    else: print("Lista vacia")

#------------------------------------------------------------------------------------------------



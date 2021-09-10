
def f(arg):
    if len(arg) == 0:
        print("Error")
    else:
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

    return

lista = [1,2,3,4,5,8,9]
lista_pos = []
lista_neg = []
lista_par = []
lista_impar = []
print(f"\nLista completa = ")
f(lista)

for lista in lista:
    if lista%2 ==0:
        lista_par.append(lista)
    else:
        lista_impar.append(lista)
    if lista < 0:
        lista_neg.append(lista)
    else:
        lista_pos.append(lista)

print(f"\nLista Par")
f(lista_par)

print(f"\nLista Impar")
f(lista_impar)

print(f"\nLista Positivo")
f(lista_pos)

print(f"\nLista Negativo")
f(lista_neg)

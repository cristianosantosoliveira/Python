print('Entre com um numero:')
lista = int(input())

lista = []

for x in range(3):
    lista.append(2 * x)

lista = [2 * x for x in range(3) ] 
pow3  = lista

print(lista, pow3)





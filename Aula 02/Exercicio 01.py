##Remove os itens repetidos da lista

def remover(lista):
    L = []
    for n in lista:
        if n not in L:
            L.append(n)
    return L

lista = [1, 1, 1, 1,3, 5, 6, 7] 

lista = remover(lista)
print (lista)





##Listas 

##Listas Sao Mutaveis 

numeros = [1, 4, 9, 16, 25]
##print(numeros)
numero_maior_1 = numeros
##print(numero_maior_1)
numero_maior_1.append(42) ##Pego a Lista  e Insiro um numero nela
##print(numero_maior_1)
numero_maior_2 = numeros+[42]
##print(numeros)
##print(numero_maior_2)

numero_menor_1 = numeros[2:]
##print(numero_menor_1)
numero_menor_2 = numeros
##print(numeros)
del numero_menor_2[:2]

print(numero_menor_2)
print(numeros)




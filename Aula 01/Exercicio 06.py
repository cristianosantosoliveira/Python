letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

letras[2:5] = ['c', 'd', 'e']
print(letras)

letras[2:5] = []
print(letras)

letras[2:2] = [1,2]
print(letras)

letras[:] = []
print(letras)
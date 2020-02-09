numeros = [1, 4, 9, 16, 25]

numero_maior_0 = numeros 
numero_maior_0.append([9,36,98])
print (numero_maior_0, 'Usando Append') 

numero_maior_1 = numeros
numero_maior_1.extend([987,654,321])
print (numero_maior_1, 'Usando Extend') 

numero_maior_2 = numeros
numero_maior_2.insert(3, 1593572580)
print (numero_maior_2, 'Usando Insert')
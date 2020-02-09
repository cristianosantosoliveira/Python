###Exercico com dicionario e listas

estado = dict()
brasil = list()

for c in range(0, 3):
    estado['uf'] = str(input('Informe o Nome Estado: '))
    estado['estado'] = str(input('Informe a Sigla: '))
    brasil.append(estado.copy())  ##Copy é usado para gravar os itens do range da lista

for e  in brasil:  ##Lendo a lista
    for v in e.values():   ##For ta lendo o dicionário
        print(v, end = ' ')
    print()

 
###Exercico com dicionario

from datetime import datetime

dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Digite o ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = str(input('Informe sua carteira de trabalho (0 não tem ): '))

if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Ano de Contratação: '))
    dados['salario'] = float(input('Salario R$: '))
    dados['aponsentadoria'] = dados['idade']  + ((dados['contratacao']) + 35 - datetime.now().year)
print('='*30)
for dicionario, entradas in dados.items():
    print(f' ** {dicionario} tem valor de {entradas}')


 
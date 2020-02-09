"""
Variaveis
"""

nome = 'Cristiano Oliveira'
idade = 30
altura = 1.80
e_maior = 18
peso = 80
imc = peso/altura **2

print(nome, 'tem', idade, 'anos de idade e seu IMC é ', imc)
print(f'{nome} tem {idade} anos de idade e seu IMC é {imc:.2f}')
print('{im} {n} tem {i} anos e seu IMC é '.format(n=nome, i=idade, im=imc))

frase = str(input('Entre com uma frase: ')).strip().upper() ##strip seria jogar a string para lista
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('O inverso  de {} é {}'.format(junto, inverso))

if inverso == junto:
    print('Temos um palindromo!')
else:
    print('A frase digitada não é um palíndromo! ')
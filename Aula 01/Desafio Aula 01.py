print("Altura do triangulo (numero impar):", end = ' ')
altura = int(input())

fator = (altura - 1) //2
for i in range(altura):
    espacos = abs(i - fator)
    chars = 2*abs(espacos - fator) + 1
    print((' ' * espacos) [:espacos], end = '')
    print('*' * chars)

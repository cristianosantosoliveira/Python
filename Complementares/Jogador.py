time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou?: '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'  Quantos gols na partida {c+1}: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy()) #joga o dicionario para dentro de uma lista
    while True:
        resp = str(input('Deseja continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('Erro! Respoonda apenas S ou N.')
    if resp == 'N':
        break
print('-' * 60)
print('cod ', end='')
#cabeçalho acessa o dicionario e exibe keys(): do dict
for i in jogador.keys():
    print(f'{i:<18}', end='')
print()
print('-' * 60) 

#Imprime os jogadores ordenando pela lista
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<18} ', end='')
    print()  ##Pula linha
print('-=' * 30)

while True:
    busca = int(input('Mostrar dados de qual jogador?: (digite 999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro! Não existe jogador com código {busca}! ')
    else:
        print(f' -- Levantamento do Jogador {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca]['gols']): #esta fazendo um enumerate dentro da lista, mais lendo o dicionario
            print(f'   No jogo {i+1} fez {g} gols')
    print('-' * 60)
print('<<<<< Volte Sempre! >>>>>')


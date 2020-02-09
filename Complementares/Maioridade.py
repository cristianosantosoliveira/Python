from datetime import date
total_maior = 0
total_menor = 0

atual = date.today().year
for pess in range(1,8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(pess)))
    idade = atual - nasc
    if idade >= 18:
        total_maior += 1
    else:
       total_menor += 1 

print('Tivemos tantas pessoas maiores de idade {} '.format(total_maior))
print('Em também tivemos tantas pessoas menor de idade {} '.format(total_menor))
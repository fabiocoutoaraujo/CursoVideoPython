primeiroTermo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiroTermo
cont = 0
total = 0
maisTermos = 10
while maisTermos != 0:
    total += maisTermos
    while cont < total:
        print(f'{termo} -> ', end='')
        termo += razao
        cont += 1
    print('PAUSA')
    maisTermos = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados.')
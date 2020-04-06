primeiroTermo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiroTermo
cont = 0
while cont < 10:
    print(f'{termo} -> ', end='')
    termo += razao
    cont += 1
print('FIM')

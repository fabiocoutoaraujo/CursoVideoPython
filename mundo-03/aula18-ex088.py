from random import randint
from time import sleep
print('-' * 40)
print(' ' * 10, 'JOGA NA MEGA-SENA', ' ' * 10)
print('-' * 40)
numeroJogos = int(input('Quantos jogos você quer que eu sorteie? '))
numeroRandomico = 0
lista = list()
print('-' * 9, f'SORTEANDO {numeroJogos} JOGO(S)', '-' * 9)
for jogo in range(0, numeroJogos):
    for dezena in range(0, 6):        
        while True:
            numeroRandomico = randint(1, 60)
            if numeroRandomico not in lista:
                lista.append(numeroRandomico)
                break
    lista.sort()
    print(f'Jogo {jogo+1}: {lista}')
    lista.clear()
    sleep(1)
print('-' * 12, '< BOA SORTE! >', '-' * 12)

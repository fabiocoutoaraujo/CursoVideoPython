from random import randint
from time import sleep
def sorteia(lista):    
    for i in range(0, 5):
        lista.append(randint(1, 100))
    print(f'Sorteando 5 valores da lista: {lista} PRONTO!')

def somaPar(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    print(f'A soma dos 5 números pares sorteados {lista} é {soma}.')

números = []
print('-' * 70)
sorteia(números)
somaPar(números)
print('-' * 70)

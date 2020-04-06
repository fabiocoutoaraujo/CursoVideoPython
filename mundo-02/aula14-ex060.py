"""
from math import factorial
numero = int(input('Digite um número para calcular o fatorial: '))
fatorial = factorial(numero)
print('O fatorial de {} é {}!'.format(numero, fatorial))
"""

n = int(input('Digite um número para calcular o fatorial: '))
f = 1
if n < 0:
    print('Não é possível calcular o fatorial de um número negativo!')
else:
    if n < 1:
        print('Calculando 0! = 1')
    else:
        if n < 2:
            print('Calculando 1! = 1 x 1 = 1')
        else:
            print('Calculando {}! = '.format(n), end='')
            while n > 0:
                f *= n
                print(f'{n}', end='')
                print(' x ' if n > 1 else ' = ', end='')
                n -= 1
            print(f)

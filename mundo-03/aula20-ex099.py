from random import randint
from time import sleep
def maior(*numeros):
    print('-=' * 23)
    print('Analisando os valores passados...')
    maior = 0
    for c in numeros:
        if c > maior:
            maior = c
        print(c, end=' ', flush=True)
        sleep(0.4)
    print(f'Foram informados {len(numeros)} valores ao todo.', end='')
    print()
    print(f'O maior valor informado foi {maior}.')


# Programa Principal
maior(randint(1, 10), randint(1, 10), randint(
    1, 10), randint(1, 10), randint(1, 10))
maior(randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
maior(randint(1, 10), randint(1, 10), randint(1, 10))
maior(randint(1, 10), randint(1, 10))
maior(randint(1, 10))
print()

from random import randint
valores = (randint(0, 20),
           randint(0, 20),
           randint(0, 20),
           randint(0, 20),
           randint(0, 20))
print(f'Os valores sorteados foram: {valores}')
print(f'O MAIOR valor sorteado foi {max(valores)}')
print(f'O menor valor sorteado foi {min(valores)}')

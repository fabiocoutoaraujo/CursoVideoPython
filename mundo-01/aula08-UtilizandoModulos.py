from math import factorial, sqrt, floor

import random
print('A raíz quadrada de 20 é {}'.format(sqrt(20)))
print('A raíz quadrada de 20 formatada é {:.2f}'.format(floor(sqrt(20))))
print('O fatorial de 5 é {}'.format(factorial(5)))

print('Número randômico {}'.format(random.random()))
print('Número randômico inteiro {}'.format(random.randint(1, 10)))

import emoji
print(emoji.emojize('Olá, mundo!!! :earth_americas:', use_aliases=True))



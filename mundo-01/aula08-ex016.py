from math import trunc
from math import floor

n = float(input('Digite um número qualquer :'))
print('v0 | O valor digitado foi {} e a parte inteira é {}'.format(n, floor(n)))
print('v1 | O valor digitado foi {} e a parte inteira é {}'.format(n, trunc(n)))
print('v2 | O valor digitado foi {} e a parte inteira é {}'.format(n, int(n)))


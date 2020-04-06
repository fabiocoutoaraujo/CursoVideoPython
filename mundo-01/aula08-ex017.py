# Teorema de Pitágoras
# O teorema de Pitágoras relaciona as medidas dos catetos de um trinângulo retângulo à
# medida de sua hipotenusa.
# a² + b² = c², onde a = cateto oposto, b = cateto adjacente e c = hipotenusa

from math import sqrt, pow, hypot

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

hi = sqrt(pow(co, 2) + pow(ca, 2))

print('v0 | A hipotenusa vai medir {:.2f}'.format(hi))
print('v1 | A hipotenusa vai medir {:.2f}'.format(hypot(co, ca)))

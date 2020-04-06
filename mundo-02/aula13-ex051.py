# Progressão aritimética (PA) é toda sequência númerica em que cada um de seus termos,
# a partir do segundo, é igual ao anterior somado a uma CONSTANTE r, denominada razão da
# progressão aritimética. Para descobrimos qual é a razão de uma PA, basta subtrairmos um
# termo qualquer do seu antecessor.
print('='*25)
print('10 TERMOS DE UMA PA')
print('='*25)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
"""
pa = primeiro
print(f'{pa}', end=' -> ')
for c in range(1, 10):
    pa += razao
    print(f'{pa}', end=' -> ')
print('ACABOU')
"""
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print('{} '.format(c), end='-> ')
print('ACABOU')

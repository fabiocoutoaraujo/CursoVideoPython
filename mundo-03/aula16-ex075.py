valores = (int(input('Digite um número: ')),
           int(input('Digite outro número: ')),
           int(input('Digite mais um número: ')),
           int(input('Digite o último número: ')))
print(f'Você digitou os valores {valores}')
print(f'O valor 9 apareceu {valores.count(9)} vezes.')
if 3 in valores:
    print(f'O valor 3 foi digitado na {valores.index(3)+1}ª posição.')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
pares = ''
print('Os valores pares digitados foram ', end='')
for c in valores:
    if c % 2 == 0:
        print('{}'.format(c), end=' ')

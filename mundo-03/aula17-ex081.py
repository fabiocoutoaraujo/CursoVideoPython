lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Você digitou {len(lista)} elementos.')
print(f'Os elementos em ordem decrescente são: {sorted(lista, reverse=True)}')
if 5 in lista:
    print(f'O número 5 faz parte da lista na posição {lista.index(5, 0) + 1}')
else:
    print('O número 5 não foi digitado!')

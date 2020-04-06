lista = pares = impares = []
while True:
    lista.append(int(input('Digite um número: ')))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
for c, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print(f'A lista completa é {lista}.')
print(f'A lista de pares é: {pares}.')
print(f'A lista de ímpares é: {impares}.')

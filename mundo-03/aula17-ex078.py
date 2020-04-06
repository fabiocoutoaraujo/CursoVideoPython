valores = []
maior = menor = 0
posMaiores = posMenores = ''
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a Posição {c}: ')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]
print('=-'*30)
print(f'Você digitou os valores {valores}')
for c, v in enumerate(valores):
    if v == maior:
        posMaiores += str(c) + '...'
    elif v == menor:
        posMenores += str(c) + '...'
print(f'O maior valor digitado foi {maior} nas posições {posMaiores}')
print(f'O menor valor digitado foi {menor} nas posições {posMenores}')

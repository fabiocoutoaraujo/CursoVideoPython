for c in range(1, 6):
    peso = float(input(f'Peso da {c}ª pessoa: '))
    if c == 1:
        menor = maior = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O MAIOR peso lido foi de {:.2f}Kg'.format(maior))
print('O MENOR peso lido foi de {:.2f}Kg'.format(menor))

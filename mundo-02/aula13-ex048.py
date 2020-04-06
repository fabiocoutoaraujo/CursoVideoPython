total = 0
for impar in range(1, 501, 2):
    if impar % 3 == 0:
        total += impar
print('A soma de todos os números ímpares, múltiplo de 3, entre 1 e 501 é {}'.format(total))

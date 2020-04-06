total = 0
for c in range(1, 7):
    numero = int(input('Digite o {}º valor: '.format(c)))
    if numero % 2 == 0:
        total += numero
print(f'A soma dos números pares digitados é {total}')

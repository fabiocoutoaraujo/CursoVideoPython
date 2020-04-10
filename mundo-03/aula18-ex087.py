matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPares = somaTerceiraColuna = maiorValorSegundaColuna = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        valor = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
        matriz[linha][coluna] = valor
        if (valor % 2 == 0):
            somaPares += valor
print('-=' * 30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[ {matriz[linha][coluna]:^5} ]', end='')
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {somaPares}')
for linha in range(0, 3):
    somaTerceiraColuna += matriz[linha][2]
print(f'A soma dos valores da terceira coluna é {somaTerceiraColuna}')
for coluna in range(0, 3):
    if matriz[1][coluna] > maiorValorSegundaColuna:
        maiorValorSegundaColuna = matriz[1][coluna]
print(f'O maior valor da segunda linha é {maiorValorSegundaColuna}')

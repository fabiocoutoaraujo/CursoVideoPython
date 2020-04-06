d = int(input('Qual a distância da sua viagem? Km '))

if d > 200:
    print('v0 | A sua viagem custará R${:.2f}'.format(d * 0.45))
else:
    print('v0 | A sua viagem custará R${:.2f}'.format(d * 0.5))

preco = d * 0.45 if d > 200 else d * 0.5
print('v1 | O preço de sua passagem será de R${:.2f}'.format(preco))

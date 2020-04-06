preço = float(input('Qual o preço do produto? R$ '))
novo = preço - (preço * 5 / 100)
msg = 'O produto que custava R$ {:.2f}, na promoção com desconto de 5% vai custar R$ {:.2f}.'
print(msg .format(preço, novo))

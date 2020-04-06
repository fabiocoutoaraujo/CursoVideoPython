print('-'*40)
print('{:-^40}'.format(' LOJA SUPER BARATÃO '))
print('-'*40)
totalCompra = superior1000 = precoMaisBarato = 0
produtoMaisBarato = ''
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$ '))
    if preco > 1000:
        superior1000 += 1
    if totalCompra == 0 or preco < precoMaisBarato:
        precoMaisBarato = preco
        produtoMaisBarato = produto
    totalCompra += preco
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar in ('Nn'):
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print('O total da compra foi R$ {:.2f}'.format(totalCompra))
print('Temos {} produtos custando mais de R$ 1.000,00'.format(superior1000))
print('O produto mais barato foi {} que custa R$ {:.2f}'.format(produtoMaisBarato, precoMaisBarato))

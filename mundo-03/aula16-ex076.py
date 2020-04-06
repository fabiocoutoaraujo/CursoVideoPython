listagem = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90,
            'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99,
            'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90, 'Notebook', 3499.99)
print('-'*40)
print('{:^40}'.format('LISTAGEM DE PREÇOS'))
print('-'*40)
for pos in range(0, len(listagem), 2):
    print(f'{listagem[pos]:.<30}R$ {listagem[pos+1]:>7.2f}')
print('-'*40)

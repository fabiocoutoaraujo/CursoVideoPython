def escreva(texto):
    caracteres = len(texto) + 4
    print('-' * caracteres)
    print(f'{texto:^{caracteres}}')
    print('-' * caracteres)


# Programa Principal
escreva('Olá, Mundo!')
escreva('Curso de Python no YouTube!')

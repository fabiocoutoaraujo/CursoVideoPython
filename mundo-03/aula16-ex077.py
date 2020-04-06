palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar',
            'mercado', 'programador', 'futuro')
for palavra in palavras:
    print(f'\nNa palavra {palavra.title()} temos as vogais: ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(F'\033[31m{letra.lower()}\033[m', end=' ')

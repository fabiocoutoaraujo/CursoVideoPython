 # docstrings
def contador(i, f, p):
    """
        -> Faz uma contagem e mostra na tela.
        :param i: inicio da contagem
        :param f: fim da contagem
        :param p: passo da contagem
        :return: sem retorno
    """
    c = i
    while i <= f:
        print(f'{c}', end='..')
        c+=p
    print('FIM!')

# parâmetros Opcionais
def somar(a = 0, b = 0, c = 0):
    s = a + b + c
    print(f'A soma vale {s}')

# escopos
def teste(b):
    global a # não crie uma variável A, use o A GLOBAL
    a = 8 # cria uma variável LOCAL A, não sendo mais o A GLOBAL
    b += 4
    c = 2
    print(f'A, local vale {a}')
    print(f'B, local vale {b}')
    print(f'C, local vale {c}')

# retorno de valores
def somar2(a=0, b=0, c=0):
    s = a + b + c
    return s

# Programa Principal
help(contador)
somar(a=3, c=2)

a = 5
teste(a)
print(f'A, global vale {a}')

resp = somar2(1, 2, 3)
print(f'O valor da função somar2 (utilizando return) é: {resp}')
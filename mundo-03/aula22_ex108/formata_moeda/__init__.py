from aula22_ex107 import moeda

def formata(p):
    return 'R$ {:>.2f}'.format(p).replace('.', ',')


def metade(p):
    return formata(moeda.metade(p))
    

def dobro(p):
    return formata(moeda.dobro(p))


def aumentar(v, p):
    return formata(moeda.aumentar(v, p))


def diminuir(v, p):
    return formata(moeda.diminuir(v, p))

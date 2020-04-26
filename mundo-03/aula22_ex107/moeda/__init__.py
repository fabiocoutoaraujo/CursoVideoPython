def metade(preco):
    res = preco / 2
    return res


def dobro(preco):
    res = preco * 2
    return res


def aumentar(preco, taxa):
    res = preco * (1 + taxa / 100)
    return res


def diminuir(preco, taxa):
    res = preco * (1 - taxa / 100)
    return res

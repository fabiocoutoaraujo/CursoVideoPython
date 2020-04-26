from aula22_ex107 import moeda
from aula22_ex108 import formata_moeda

def metade(preco, formatar=False):
    return formata_moeda.metade(preco) if formatar else moeda.metade(preco)


def dobro(preco, formatar=False):
    return formata_moeda.dobro(preco) if formatar else moeda.dobro(preco)


def aumentar(preco, taxa, formatar=False):
    return formata_moeda.aumentar(preco, taxa) if formatar else moeda.aumentar(preco, taxa)


def diminuir(preco, taxa, formatar=False):
    return formata_moeda.diminuir(preco, taxa) if formatar else moeda.diminuir(preco, taxa)

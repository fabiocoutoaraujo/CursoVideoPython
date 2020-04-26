from aula22_ex108 import formata_moeda

def cabecalho(texto, tam):
    print('-' * tam)
    print(f'{texto.upper():^{tam}}')
    print('-' * tam)


def resumo(preco, taxaA, taxaR):
    '''
    -> Calcula o aumento e a redução de um determinado preço,
    bem como, o dobro e a metade deste preço. Ao final, escreve
    os valores do console.
    :param preco: o preço que se quer reajustar
    :param taxaA: a percentagem do aumento
    :param taxaR: a percentagem da redução 
    '''
    tam = 40
    cabecalho('resumo do preço', tam)
    print(f'Preço analisado: \t{formata_moeda.formata(preco)}')
    print(f'Dobro do preço: \t{formata_moeda.dobro(preco)}')
    print(f'Metade do preço: \t{formata_moeda.metade(preco)}')
    print(f'{taxaA}% de aumento: \t{formata_moeda.aumentar(preco, taxaA)}')
    print(f'{taxaR}% de redução: \t{formata_moeda.diminuir(preco, taxaR)}')
    print('-' * tam)

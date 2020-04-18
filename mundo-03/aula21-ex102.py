def fatorial(numero=1, show=False):
    """
        -> Calcula o Fatorial de um número.
        :param numero: O número a ser calculado.
        :param show: (opcional) Mostrar ou não a conta.
        :return: O valor do Fatorial de um número n.
    """
    fat = 1
    ext = ''
    for i in range(numero, 0, -1):
        fat *= i
        ext += str(i) + ' x '
    return ext[:-2] + '= ' + str(fat) if show else str(fat)


# Programa Principal
num = int(input('Digite um número: '))
retorno = fatorial(numero=num, show=False)
print('-'*30)
print(retorno)
help(fatorial)
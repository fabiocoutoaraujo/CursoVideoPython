# Quando um número é divisivel por outro, isto é, a divisão por eles possui resto igual a
# zero, dizemos que os números são múltiplos.

# Os anos bissetos são múltiplos de 4, não múltiplos de 100 e múltiplos de 400.

from datetime import date

ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSESTO!'.format(ano))
else:
    print('O ano {} NÃO É BISSESTO!'.format(ano))

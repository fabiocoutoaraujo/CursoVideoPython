cas = float(input('Valor da casa: R$ '))
sal = float(input('Salário do comprador: R$ '))
ano = int(input('Quantos anos de financiamento? '))

pre = cas / ano / 12
par = sal * 0.3

print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'
      .format(cas, ano, pre))

if pre > par:
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo pode ser CONCEDIDO!')

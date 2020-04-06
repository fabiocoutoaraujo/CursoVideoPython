sal = float(input('Qual é o salário do funcionário? R$ '))

if sal > 1250:
    input('Seu novo salário é de R$ {:.2f}'.format(sal + (sal * 10 / 100)))
else:
    input('Seu novo salário é de R$ {:.2f}'.format(sal + (sal * 15 / 100)))


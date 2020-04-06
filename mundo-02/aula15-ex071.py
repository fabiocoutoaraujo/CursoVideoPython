print('='*30)
print('{:^30}'.format('BANCO'))
print('='*30)
valor = int(input('Que valor você quer sacar? R$ '))
resto = valor
while resto != 0:
    if resto // 50 > 0:
        print(f'Emitindo {valor // 50} cédulas de R$ 50')
        resto %= 50
    if resto // 20 > 0:
        print(f'Emitindo {resto // 20} cédulas de R$ 20')
        resto %= 20
    if resto // 10 > 0:
        print(f'Emitindo {resto // 10} cédulas de R$ 10')
        resto %= 10
    if resto // 1 > 0:
        print(f'Emitindo {resto // 1} cédulas de R$ 01')
        resto %= 1

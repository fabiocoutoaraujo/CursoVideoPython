n1 = float(input('Digite sua nota 01: '))
n2 = float(input('Digite sua nota 02: '))

media = (n1 + n2) / 2

if media < 7:
    print('Sua média {:.1f} foi ruim! ESTUDE MAIS!!!'.format(media))
else:
    print('Sua média {:.1f} foi boa! PARABÊNS!!!'.format(media))

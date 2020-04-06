n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

media = (n1+n2)/2

print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(n1, n2, media))

if media < 5:
    print('A sua média final foi {} e você foi REPROVADO!'.format(media))
elif media < 7:
    print('A sua média final foi {} e você está de RECUPERAÇÃO!'.format(media))
else:
    print('A sua média final foi {} e você foi APROVADO!')

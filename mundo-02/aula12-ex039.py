from datetime import date
corrente = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = corrente - nascimento

print('Quem nasceu em {} tem {} anos em {}.'.format(nascimento, idade, corrente))

if idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos, pois seu alistamento foi em {}.'
          .format(saldo, corrente - saldo))
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento, que será em {}.'
          .format(saldo, corrente + saldo))
else:
    print('Você deve se alistar IMEDIATAMENTE.')

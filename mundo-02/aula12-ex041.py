from datetime import date
corrente = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = corrente - nascimento
print('O atleta tem {} anos e sua '.format(idade), end='')
if idade < 10:
    print('classificação é MIRIM')
elif idade < 15:
    print('classificação é INFANTIL')
elif idade < 20:
    print('classificação é JUNIOR')
elif idade < 26:
    print('classificação é SÊNIOR')
else:
    print('classificação é MASTER')

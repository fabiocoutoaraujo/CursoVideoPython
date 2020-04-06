maior18 = homens = mulherMenor20 = 0
while True:
    print('-'*30)
    print('CADASTRE UMA PESSOA')
    print('-'*30)

    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip()[0]

    if idade > 18:
        maior18 += 1
    if sexo in 'Mm':
        homens += 1
    if sexo in 'Ff' and idade < 20:
        mulherMenor20 += 1

    opcao = str(input('Quer continuar? [S/N] ')).strip()[0]
    if opcao in 'Nn':
        break

print(f'Total de pessoas com mais de 18 anos: {maior18}.')
print(f'Ao todo, temos {homens} homens cadastrados.')
print(f'E temos {mulherMenor20} mulheres com menos de 20 anos.')

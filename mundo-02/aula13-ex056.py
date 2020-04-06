somarIdade = maiorIdadeHomem = mulheresMenos20 = 0
for c in range(1, 5):
    print(f'-----{c}ª PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    if sexo in 'Mm':
        if idade > maiorIdadeHomem:
            maiorIdadeHomem = idade
            nomeHomemVelho = nome
    else:
        if idade < 20:
            mulheresMenos20 += 1
    somarIdade += idade
print(f'A média de idade do grupo é de {somarIdade/4} anos.')
print(f'O homem mais velho tem {maiorIdadeHomem} anos e se chama {nomeHomemVelho}.')
print(f'Ao todo são {mulheresMenos20} mulheres com menos de 20 anos.')

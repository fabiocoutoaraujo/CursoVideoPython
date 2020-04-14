pessoa = {}
turma = []
somaIdade = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: ')).strip()
    while True:
        sexo = str(input('Sexo [M/F]: ')).strip()[0]
        if sexo in 'FfMm':
            pessoa['sexo'] = sexo
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    somaIdade += pessoa['idade']
    turma.append(pessoa.copy())
    continuar = ''
    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip()[0]
        if continuar in 'SsNn':
            break
        print('ERRO! Responda apenas S ou N.')
    if continuar in 'Nn':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(turma)} pessoas cadastradas.')
print(f'B) A média de idade é de {somaIdade / len(turma):.0f} anos.')
print(f'C) As mulheres cadastradas foram', end=' ')
for c in turma:
    if c['sexo'] in 'Ff':
        print(f'{c["nome"]}', end=', ')
print()
print('D) Lista das pessoas que estão acima da média:')
for c in turma:
    if c['idade'] > somaIdade / len(turma):
        for k, v in c.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')

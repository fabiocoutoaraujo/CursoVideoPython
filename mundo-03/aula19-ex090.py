aluno = dict()
aluno['nome'] = str(input('Nome: ')).strip()
aluno['media'] = float(input(f'Média de {aluno["nome"]}: ').strip())
aluno['situacao'] = 'Recuperação' if aluno['media'] < 7 else 'Aprovado'
print('-=' * 30)
for k, v in aluno.items():
    print('' * 4, '- ', f'{k} é igual a {v}')

from datetime import date
nome = str(input('Nome: ').strip())
anoNascimento = int(input('Ano de nascimento: '))
idade = date.today().year - anoNascimento
carteira = int(input('Carteira de trabalho (0 não tem): '))
dicionario = {
    'nome': nome,
    'idade': idade,
    'carteira': carteira
}
if carteira != 0:
    anoContratacao = int(input('Ano de contratação: '))
    salario = float(input('Salário R$: '))
    dicionario['cotratação'] = anoContratacao
    dicionario['salário'] = salario
    anosTrabalhados = date.today().year - anoContratacao
    dicionario['aposentadoria'] = 35 - anosTrabalhados + idade
print('-=' * 30)
for k, v in dicionario.items():
    print(f'  - {k} tem o valor {v}')

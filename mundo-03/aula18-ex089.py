i = 0
classe = []
continuar = ''
while True:
    nome = str(input('Nome: ').strip())
    nota1 = float(input('Nota 1: ').strip())
    nota2 = float(input('Nota 2: ').strip()) 
    classe.append([i, nome, nota1, nota2, (nota1 + nota2) / 2])
    while True:
        continuar = str(input('Quer continuar? [S/N] ').strip()[0])
        if continuar not in 'SsNn':
            print('\033[31mValor informado inválido!\033[m')
        else:
            break
    if continuar in 'Nn':
        break
    i += 1
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for c in classe:
    print(f'{c[0]:<4}{c[1]:<10}{c[4]:>8.1f}')
print('-' * 40)
while True:
    continuar = str(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if '999' in continuar:
        print('FINALIZANDO...')
        break
    for c in classe:
        if int(continuar) == c[0]:
            print(f'As notas de {c[1]} são [{c[2]}, {c[3]}]')
print(' <<< VOLTE SEMPRE >>> ')

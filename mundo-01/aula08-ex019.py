from random import choice

a1 = str(input('Primeiro aluno: ')).strip()
a2 = str(input('Segundo aluno: ')).strip()
a3 = str(input('Terceiro aluno: ')).strip()
a4 = str(input('Quarto aluno: ')).strip()

alunos = [a1, a2, a3, a4]

print('O aluno escolhido para apagar o quadro negro foi o {}.'.format(choice(alunos)))


from random import shuffle

n1 = str(input('Digite o primeiro aluno: '))
n2 = str(input('Digite o segundo aluno: '))
n3 = str(input('Digite o terceiro aluno: '))
n4 = str(input('Digite o quarto aluno: '))

lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem dos alunos será: ')
print(lista)

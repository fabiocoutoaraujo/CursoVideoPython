# Variáveis Compostas -> Listas
lanche = ['Hambúrguer', 'Suco', 'Pizza', 'Sorvete']
print(lanche)

lanche[0] = 'Esfiha'
print(lanche)

lanche.append('Cookie')
print(lanche)

lanche.insert(2, 'Kibe')
print(lanche)

del lanche[4]   # índice
print(lanche)

lanche.pop(-1)  # índice
print(lanche)

lanche.pop()    # remove o último elemento
print(lanche)

if 'Esfiha' in lanche:
    lanche.remove('Esfiha')  # remove a primeira ocorrência pelo CONTEÚDO informado
print(lanche)

valores = list(range(0, 11, 2))
print(valores)

valores = [8, 2, 5, 4, 3, 0]
valores.sort()
print(valores)

valores.sort(reverse=True)
print(valores)

print(len(valores))
'''
valores = list()
for c in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c}, encontrei o valor {v}!')
print('Cheguei ao final da lista')
'''

a = [2, 3, 4, 5]
b = a[:]  # Cria uma cópia de a dentro de b
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')

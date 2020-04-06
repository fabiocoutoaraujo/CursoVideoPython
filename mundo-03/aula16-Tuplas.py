# Tuplas são imutáveis
tupla1 = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
# tupla1[1] = 'Refrigerante'

print(tupla1)
print(tupla1[0])    # Hambúrguer
print(tupla1[3])    # Pudim
print(tupla1[-1])   # Batata Frita
print(tupla1[-2])   # Pudim
print(tupla1[1:3])  # Suco e Pizza
print(tupla1[2:])   # Pizza, Pudim, Batata Frita
print(tupla1[:2])   # Hambúrguer e Suco
print(tupla1[-2:])  # Pudim e Batata Frita
print(tupla1[-3:])  # Pizza, Pudim e Batata Frita

print('='*50)

tupla2 = 'São Paulo', 'Palmeiras', 'Santos'
print(tupla2)
print(f'A tupla2 possui {len(tupla2)} itens.')

print('='*50)

for comida in tupla1:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')

for pos in range(0, len(tupla1)):
    print(f'Eu vou comer {tupla1[pos]} na posição {pos}.')
print('Comi pra caramba!')

for pos, comida in enumerate(tupla1):
    print(f'Eu vou comer {comida} na posição {pos}.')
print('Comi pra caramba!')

print('='*50)

print(tupla1)
print(f'Ordenando uma tupla: {sorted(tupla1)}')   # Transfora e Lista []

print('='*50)

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(f'(2, 5, 4) + (5, 8, 1, 2) = {c}')
c = b + a
print(f'(5, 8, 1, 2) + (2, 5, 4) = {c}, onde c possui {len(c)} elementos, o número cinco aparece {c.count(5)} vezes e o número dois está na posição {c.index(2)}')
print(f'A segunda ocorrência no número cinco encontra-se na posição {c.index(5, 1)}.')

print('='*50)

'''
pessoa = ('Gustavo', 39, 'M', 99.88)
print(pessoa)
del(pessoa)
print(pessoa)
'''
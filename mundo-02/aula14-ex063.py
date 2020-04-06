# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
#    a, b, c
n = int(input('Digite um número: '))
i = 3
a = 0
b = 1
print(f'Sequência de fibonacci: {a}, {b}', end='')
while i <= n:
    c = a + b
    print(f', {c}', end='')
    a = b
    b = c
    i += 1
print('.')

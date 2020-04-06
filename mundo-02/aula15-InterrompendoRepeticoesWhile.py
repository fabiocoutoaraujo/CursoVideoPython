'''
cont = 1
while cont < 11:
    print(cont, '-> ', end='')
    cont += 1
print('FIM!')
'''

# No Python não declaramos variáveis. Inicializamos uma variável.
n = s = 0
while n != 999:  # Flag
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print('A soma vale {}'.format(s))

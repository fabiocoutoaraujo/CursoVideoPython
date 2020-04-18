def leiaInt(t):
    while True:
        num = input(t)
        if num.isnumeric():
            return int(num)
        print('\033[31mERRO! Digite um número inteiro válido.\033[m')

# Programa Principal
print('-' * 30) 
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')

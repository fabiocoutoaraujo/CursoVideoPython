extenso = ('zero', 'um', 'dois', 'três', 'quatro',
           'cinco', 'seis', 'sete', 'oito', 'nove',
           'dez', 'onze', 'doze', 'treze', 'quatorze',
           'quinze', 'dezesseis', 'dezessete', 'dezoito',
           'dezenove', 'vinte')
while True:
    n = -1
    while n < 0 or n > 20:
        n = int(input('Digite um número entre 0 e 20: '))
    print(f'Você digitou o número \033[34m{extenso[n]}\033[m.')
    resp = ' '
    while resp not in 'NS':
        resp = str(input('\033[32mDeseja continuar? [S/N]\033[m ')).strip().upper()[0]
    if resp == 'N':
        break
print('Obrigado e volte sempre!')

valores = []
while True:
    n = int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('\033[31mValor duplicado! Não vou adicionar...\033[m')
    resp = input('\033[32mDeseja continuar? [S/N]\033[m ').strip()[0]
    if resp in 'Nn':
        break
valores.sort()
print(f'Você digitou os valores {valores}')

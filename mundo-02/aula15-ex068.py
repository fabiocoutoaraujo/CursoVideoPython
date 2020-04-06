from random import randint
vitorias = 0
resultado = ''
while True:
    jogador = ''
    while not jogador.isnumeric():
        jogador = input('Diga um valor: ').strip()
    opcao = ' '
    while opcao not in 'PpIiÍí':
        opcao = str(input('Par ou Ímpar? [P/I] '))[0].strip().upper()
    computador = randint(0, 10)
    soma = int(jogador) + computador
    if soma % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'ÍMPAR'
    print(f'Você jogou {jogador} e o computador {computador}, totalizando {soma} que é {resultado}. ', end='')
    if (opcao in 'Pp' and resultado == 'PAR') or (opcao in 'IiÍí' and resultado == 'ÍMPAR'):
        vitorias += 1
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
    else:
        print('Você PERDEU!')
        break
print('GAME OVER! Você venceu {} vezes.'.format(vitorias))

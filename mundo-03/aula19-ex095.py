cod = 0
jogador = {}
time = []
while True:
    jogador.clear()
    cod += 1
    jogador['cod'] = cod
    jogador['nome'] = str(input('Nome do jogador: ')).strip()
    jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    listaGols = []
    for i in range(0, jogador['partidas']):
        listaGols.append(int(input(f'Quantos gols na partida {i+1}? ')))
    jogador['gols'] = listaGols
    time.append(jogador.copy())    
    resp = ''
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Digite Sim ou Não!')
    if resp == 'N':
        break
print('-=' * 30)
print(f'{"cod":>3} {"nome":<15}{"gols":<18}{"total":>5}')
print('-' * 42)
for i, v in enumerate(time):
    print(f'{v["cod"]:>3} {str(v["nome"]):<15}{str(v["gols"]):<18}{str(sum(v["gols"])):>5}')
print('-' * 42)
while True:
    resp = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if resp == 999:
        break
    if resp == 0 or resp > cod:
        print(f'ERRO! Não existe jogador com o código {resp}!')
    else:
        for i, v in enumerate(time):
            if v['cod'] == resp:
                print(f' -- LEVANTAMENTO DO JOGADOR {v["nome"]}:')
                for j, k in enumerate(v['gols']):
                    print(' ' * 4, f'No jogo {j+1} fez {k} gols.')
                break
    print('-' * 42)
print('  === < FIM! > ===')

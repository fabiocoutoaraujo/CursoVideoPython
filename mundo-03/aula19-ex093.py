jogador = str(input('Nome do jogador: ')).strip()
partidas = int(input(f'Quantas partidas {jogador} jogou? '))
dicionario = {
    'nome': jogador,
    'partidas': partidas
}
listaGols = []
if partidas > 0:
    for i in range(0, partidas):
        gols = int(input(f'   Quantos gols na partida {i + 1}? '))
        listaGols.append(gols)
    dicionario['gols'] = listaGols
    dicionario['total'] = sum(listaGols)
print('-='*30)
print(dicionario)
print('-=' * 30)
for k, v in dicionario.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {dicionario["nome"]} jogou {len(dicionario["gols"])} partidas.')
for i, v in enumerate(listaGols):
    print(f'   => Na partida {i + 1}, fez {v} gols.')
print(f'Foi um total de {dicionario["total"]} gols.')

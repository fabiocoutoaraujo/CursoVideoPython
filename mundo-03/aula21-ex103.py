def ficha(nome = '', gols = ''):
    if len(nome) == 0:
        nome = '<desconhecido>'
    if len(gols) == 0 or not gols.isnumeric():
        gols = '0'
    return f'O jogador {nome} fez {gols} gol(s) no campeonato.'    


# Programa Principal
print('-'*30)
nome = str(input('Nome do Jogador: ')).strip()
gols = str(input('Número de Gols: ')).strip()
print(ficha(nome, gols))

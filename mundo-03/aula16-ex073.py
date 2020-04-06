brasileirao2019 = ('Santos', 'Palmeiras', 'Flamengo', 'Atlético',
                   'São Paulo', 'Corinthians', 'Botafogo', 'Internacional',
                   'Ceará SC', 'Bahia', 'Athletico-PR', 'Fortaleza',
                   'Goiás', 'Grêmio', 'Vasco da Gama', 'Fluminense',
                   'Cruzeiro', 'Chapecoense', 'CSA', 'Avaí')
print('='*80)
print(f'Lista de times do Brasileirão 2019: {brasileirao2019}')
print('='*80)
print(f'Os 5 primeiros são: {brasileirao2019[0:5]}')
print('='*80)
print(f'Os 4 últimos são: {brasileirao2019[-4:]}')
print('='*80)
print(f'Times e ordem alfabética: {sorted(brasileirao2019)}')
print('='*80)
print(f'O Chapecoense está na {brasileirao2019.index("Chapecoense")+1}ª posição.')

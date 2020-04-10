filme = {
    'titulo': 'Star Wars',
    'ano': 1977,
    'diretor': 'George Lucas',
    'produtora': 'Lucasfilm'
}
print(filme)
print(filme['diretor'])
del filme['produtora']
print(filme.values())
print(filme.keys())
print(filme.items())

filme['elenco'] = 'Natalie Portman'

for k, v in filme.items():
    print(f'O {k} é {v}')

print('-' * 30)
print(f'{"CRIANDO ESTADOS":^30}')
print('-' * 30)
estado1 = {
    'uf': 'São Paulo',
    'sigla': 'SP'
}
estado2 = {
    'uf': 'Rio de Janeiro',
    'sigla': 'RJ'
}
brasil = []
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0]["sigla"])

print('-' * 30)
print(f'{"CRIANDO PAÍS":^30}')
print('-' * 30)
estados = dict()
brasil = list()
for c in range(0, 3):
    estados['uf'] = str(input('Unidade Federativa: '))
    estados['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estados.copy())  # para dicionários ñ consigo utilizar [:], por isso utilizar .copy()
for c in brasil:
    for u, s in c.items():
        print(f'O campo {u} tem o valor {s}.')


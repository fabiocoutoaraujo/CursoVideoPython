def exibeLinhas(n):
    print('-'*n)

def exibeCabecalho(msg):
    n = len(msg.strip()) + 15
    exibeLinhas(n)
    print(f'{msg.upper():^{n}}')
    exibeLinhas(n)

def contador(*tupla):
    print(f'Recebi {len(tupla)} números {tupla}, DESEMPACOTEI e a soma deles é {sum(tupla)}.')

def dobrarValores(lista):
    pos = 0
    listaDobrada = lista[:]
    while pos < len(listaDobrada):
        listaDobrada[pos] *= 2
        pos += 1
    print(f'A lista inicial foi {lista}, dobramos cada valor e temos {listaDobrada}.')

# Progama Principal
exibeCabecalho('analisando o PIB dos paises da zona do euro ')
print()
contador(2, 8, 4, 7, 3)
print()
dobrarValores([54, 42, 13, 34, 32])
print()

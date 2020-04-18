def notas(*numeros, sit=False):
    menor = maior = media = 0
    total = len(numeros)
    dicionario = {
        'total': total 
    }
    for p, v in enumerate(numeros):
        if p == 0:
            menor = maior = v
        else:
            if v > maior:
                maior = v
            if v < menor:
                menor = v
        media += v
    media /= total
    dicionario['maior'] = maior
    dicionario['menor'] = menor
    dicionario['media'] = media
    if sit:
        situacao = ''
        if media < 5:
            situacao = 'RUIM'
        elif media < 7.5:
            situacao = 'RAZOÁVEL'
        else:
            situacao = 'BOA'
        dicionario['situacao'] = situacao
    return dicionario        

def notas2(*numeros, sit=False):
    d = dict()
    d['total'] = len(numeros)
    d['maior'] = max(numeros)
    d['menor'] = min(numeros)
    d['media'] = sum(numeros) / len(numeros)
    if sit:
        if d['media'] >= 7:
            d['situacao'] = 'BOA'
        elif d['media'] >= 5:
            d['situacao'] = 'RAZOÁVEL'
        else:
            d['situacao'] = 'RUIM'
    return d

# Programa Principal
print('-'*78)
resp = notas(5.5, 6.5, 1, 6.5, sit=True)
print(resp)
print('-'*78)
resp = notas2(5.5, 6.5, 1, 6.5, sit=True)
print(resp)
print('-'*78)

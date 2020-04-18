def vota(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA'
    if idade < 18:
        return f'Com {idade} anos: VOTO FACULTATIVO.'
    if idade < 70:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
    else:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    

# Programa Principal
print('-'*30)
ano = int(input('Em que ano você nasceu? '))
print(vota(ano))

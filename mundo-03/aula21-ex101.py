from datetime import date
def vota(idade):
    if idade < 16:
        return 'NÃO VOTA'
    if idade < 18:
        return 'VOTO FACULTATIVO.'        
    if idade < 70:
        return 'VOTO OBRIGATÓRIO.'
    else:
        return 'VOTO OPCIONAL.'


# Programa Principal
print('-'*30)
ano = int(input('Em que ano você nasceu? '))
idade = date.today().year - ano
retorno = vota(idade)
print(f'Com {idade} anos: {retorno}')
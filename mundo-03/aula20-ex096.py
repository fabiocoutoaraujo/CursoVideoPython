def área(comprimento, largura):
    print(f'A área de um terreno {comprimento}x{largura} é {comprimento*largura}m².')


# Programa Principal
print('-'*25)
print(f'{"Controle de Terrenos":^25}')
print('-'*25)
comprimento = float(input('COMPRIMENTO (m): '))
largura = float(input('LARGURA (m): '))
área(comprimento, largura)

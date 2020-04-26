def leiaDinheiro(texto):
    while True:
        entrada = str(input(texto)).strip().replace(',', '.')
        if entrada.isalpha() or entrada == '':
            print(f'\033[31mERRO! "{entrada}" é um preço inválido!\033[m')
        else:
            return float(entrada)

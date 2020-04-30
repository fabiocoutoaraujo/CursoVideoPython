def leia_int(msg):    
    while True:
        try:
            valor = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um número inteiro válido.')
        except KeyboardInterrupt:
            print('Entrada de dados interrompida pelo usuário.')
        else:
            return int(valor)    


def leia_float(msg):
    while True:
        try:
            valor = float(str(input(msg)).replace(',', '.'))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um número real válido.')
        except KeyboardInterrupt:
            print('Entrada de dados interrompida pelo usuário.')
        else:
            return float(valor)        

inteiro = leia_int('Digite um Inteiro: ')
print(f'O número inteiro informado foi {inteiro}')

racional = leia_float('Digite um Real: ')
print(f'O número real informado foi {racional}')

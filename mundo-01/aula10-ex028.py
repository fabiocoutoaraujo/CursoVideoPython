from random import randint
from time import sleep

cores = {'limpa':    '\033[m',
         'branco':   '\033[30m',
         'vermelho': '\033[31m',
         'verde':    '\033[32m',
         'amarelo':  '\033[33m',
         'azul':     '\033[34m',
         'magenta':  '\033[35m',
         'ciano':    '\033[36m',
         'cinza':    '\033[37m'}

print('{}{}{}'.format(cores['amarelo'], '-=-' * 20, cores['limpa']))
print('{}Vou pensar em um número entre 0 e 5. Tente adivinhar...{}'.format(cores['azul'], cores['limpa']))
print('{}{}{}'.format(cores['amarelo'], '-=-' * 20, cores['limpa']))

computador = randint(0, 5)
jogador = int(input('Em que número eu pensei? '))

print('{}PROCESSANDO...{}'.format(cores['magenta'], cores['limpa']))
sleep(3)

if jogador == computador:
    print('{}PARABÉNS! Você conseguiu me vencer!{}'
          .format(cores['amarelo'],
                  cores['limpa']))
else:
    print('{}GANHEI! Eu pensei no número {} e não no {}!{}'
          .format(cores['vermelho'],
                  computador,
                  jogador,
                  cores['limpa']))

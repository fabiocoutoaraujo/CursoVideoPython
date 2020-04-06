from random import randint
computador = randint(0, 10)
jogador = -1
palpites = 0
print('Sou o seu computador e pensei em um número de 0 a 10. Será que você consegue adivinhar qual foi?')
while jogador != computador:
    palpites += 1
    jogador = int(input('Qual é seu palpite? '))
print('PARABÉNS!!! O computador pensou no número {} e você adivinhou após {} palpites.'.format(computador, palpites))

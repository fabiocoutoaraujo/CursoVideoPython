cont = soma = 0
núm = int(input('Digite umm número [999 para parar]: '))
while núm != 999:
    cont += 1
    soma += núm
    núm = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont, soma))

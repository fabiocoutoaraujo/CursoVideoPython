'''
Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o
menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''
maior = menor = soma = cont = 0
opcao = 'S'
while opcao in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    opcao = str(input('Quer continuar? [S/N] ')).strip()[0]
print(f'Você digitou {cont} números e a média foi {soma / cont :.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')

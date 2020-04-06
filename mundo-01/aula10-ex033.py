n1 = float(input('Digite o 1º número: '))
n2 = float(input('Digite o 2º número: '))
n3 = float(input('Digite o 3º número: '))
maior = n1
menor = n1

if n2 > n1:
    maior = n2
if n3 > maior:
    maior = n3

if n2 < n1:
    menor = n2
if n3 < menor:
    menor = n3

print('O menor valor digitado é {}'.format(menor))
print('O maior valor digitado é {}'.format(maior))

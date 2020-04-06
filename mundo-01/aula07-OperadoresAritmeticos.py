# Ordem de Precedência:
# 1 = ()
# 2 = **
# 3 = *, /, //, %
# 4 = +, -
# =========================================================================================
print('5 + 2 = {}'.format(5 + 2))
print('5 - 2 = {}'.format(5 - 2))
print('5 / 2 = {}'.format(5 / 2))
print('5 * 2 = {}'.format(5 * 2))
print('5² = {}'.format(5 ** 2))
print('A divisão inteira entre 5 e 2 = {}'.format(5 // 2))
print('O resto da divisão entre 5 e 2 = {}'.format(5 % 2))
# =========================================================================================
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
rq = n1**(1/2)
rc = n1**(1/3)

print('A soma é {}, o produto é {}, a divisão é {:.3f}' .format(s, m, d), end=' >>> ') # 'end' não quebra linha de 1 print pra outro
print('A divisão inteira é {} e a potência é {}' .format(di, e))
print('A raiz quadrada de {} é {}'.format(n1, rq))
print('A raiz cúbica de {} é {}'.format(n1, rc))
# =========================================================================================
print('Olá meu jovem {:20}!' .format(n1))
print('Olá meu jovem {:>20}!' .format(n1))
print('Olá meu jovem {:^20}!' .format(n1))
print('Olá meu jovem {:=^20}!' .format(n1))
# =========================================================================================

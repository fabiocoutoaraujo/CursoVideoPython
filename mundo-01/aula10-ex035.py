# Só irá existir um triângulo se, somente se, os seus lados obdeceram à seguinte regra:
# (1) um de seus lados deve ser maior que o valor absoluto (módulo) da diferença dos
# outros dois lados e (2) menor que a soma dos outros dois lados.

print('-='*20)
print('Analisando Triângulos')
print('-='*20)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima PODEM FORMAR um triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')

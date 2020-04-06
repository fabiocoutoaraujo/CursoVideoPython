# (a+b)*(c+d)
expressao = str(input('Digite uma expressão matemática: '))
lista = []
for e in expressao:
    if e == '(':
        lista.append(e)
    elif e == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(e)
            break
print('Sua expressão está válida!' if len(lista) == 0 else 'Sua expressão está inválida!')

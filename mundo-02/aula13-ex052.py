# Um número é primo se for > 1 e divisível APENAS por um e por ELE mesmo.
num = int(input('Digite um número: '))
primo = True
if num > 1:
    for c in range(2, num+1):
        if c != num:
            if num % c == 0:
                primo = False
                break
else:
    primo = False
print(f'{num} é um número primo!' if primo else f'{num} não é um número primo!')

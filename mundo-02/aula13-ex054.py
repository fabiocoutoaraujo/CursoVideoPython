from datetime import date
maior = menor = 0
atual = date.today().year
for c in range(1, 8):
    nascimento = int(input(f'Em que ano a {c}ª pessoa nasceu? '))
    if atual - nascimento > 20:
        maior += 1
    else:
        menor += 1
print(f'Ao todo, temos {maior} pessoas maiores de idade!')
print(f'Ao todo, temos {menor} pessoas menores de idade!')

people = []
fatter = thinner = 0
while True:
    person = [str(input('Nome: ')).strip(), float(input('Peso: '))]
    if len(people) == 0:
        fatter = thinner = person[1]
    else:
        if person[1] > fatter:
            fatter = person[1]
        if person[1] < thinner:
            thinner = person[1]
    people.append(person[:])
    person.clear()
    resp = ' '
    while resp not in 'NS':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-='*20)
print(f'Ao todo você cadastrou {len(people)} pessoas.')
print(f'O maior peso foi de {fatter}Kg. Peso de: ', end='')
for p in people:
    if p[1] == fatter:
        print(f'{p[0]}, ', end='')
print()
print(f'O menor peso foi de {thinner}Kg. Peso de: ', end='')
for p in people:
    if p[1] == thinner:
        print(f'{p[0]}, ', end='')
print()

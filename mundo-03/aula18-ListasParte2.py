dados1 = list()
dados1.append('Pedro')
dados1.append(25)

dados2 = list()
dados2.append('Maria')
dados2.append(19)

dados3 = list()
dados3.append('João')
dados3.append(32)

pessoas = [dados1[:], dados2[:], dados3[:], ['Fábio', 37]]  # [:] cria uma cópia
print(pessoas)
print('=-'*20)

print(pessoas[1][1])  # 19
print(pessoas[3])
print(pessoas[2:])
print('=-'*20)

for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos de idade.')
print('=-'*20)

galera = list()
dado = list()
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] > 20:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade.')

numeros = [[], []]
for i in range(1, 8):
    v = int(input(f"Digite o {i} º valor: "))
    if (v % 2 == 0):
        numeros[0].append(v)
    else:
        numeros[1].append(v)
print("-=" * 30)
numeros[0].sort()
numeros[1].sort()
print(f"Os valores PARES digitados foram: {numeros[0]}")
print(f"Os valores ÍMPARES digitados foram: {numeros[1]}")

frase = str(input('Digite uma frase: ')).strip().replace(' ', '').lower()
inverso = ''

for c in range(len(frase) - 1, - 1, - 1):
    inverso += frase[c]

print(f'v0 | A frase {frase} É um palíndromo!' if frase == inverso else f'v0 | A frase {frase} NÃO é um palíndromo!')
print(f'v0 | A frase {frase} É um palíndromo!' if frase == frase[::-1] else f'v0 | A frase {frase} NÃO é um palíndromo!')

# ''.join(frase.split())
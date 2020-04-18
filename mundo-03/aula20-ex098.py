from time import sleep
def contador(inicio, fim, passo):
    print('-=' * 30)
    if passo == 0:
        passo = 1
    if passo < 0:
        passo *= -1
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if (inicio > fim):     
        fim -= 1
        passo *= -1
    else:
        fim += 1
    for c in range(inicio, fim, passo):
        print(c, end=' ', flush=True)
        sleep(0.5)
    print('FIM!', end='')
    

# Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 30)
print('Agora é sua vez de personalizar a contagem!')
contador(int(input('Início: ')), int(input('Fim: ')), int(input('Passo: ')))

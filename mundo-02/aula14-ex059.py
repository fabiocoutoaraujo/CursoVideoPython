n1 = int(input('1º Valor: '))
n2 = int(input('2º Valor: '))
opcao = 0
while opcao != 5:
    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    opcao = int(input('>>>>> Qual é a sua opção? '))
    if opcao == 1:
        print(f'A soma entre {n1} e {n2} é {n1+n2}')
    elif opcao == 2:
        print(f'O resultado de {n1} e {n2} é {n1*n2}')
    elif opcao == 3:
        maior = n1
        if n2 > n1:
            maior = n2
        print(f'Entre {n1} e {n2} o maior valor é {maior}')
    elif opcao == 4:
        print('Informe os números novamente:')
        n1 = int(input('1º Valor: '))
        n2 = int(input('2º Valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
    print('=-='*10)

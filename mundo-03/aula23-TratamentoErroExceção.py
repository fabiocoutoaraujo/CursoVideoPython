#  Erro = Falha Sintática
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    c = a / b
except (ValueError, TypeError):
    print('Tivemos problemas com os tipos de dados que você digitou!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__class__}')
else:
    print(f'O resultado é {c:.1f}')
finally:
    print('Muito obrigado e volte sempre!')
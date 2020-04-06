velocidade = int(input('Qual é a velocidade do seu carro? Km/h '))

if velocidade > 80:
    print('\033[31mMULTADO! Você excedeu o limite permitido que é de 80Km/h')
    print('Você deve pagar uma multa de{} R${:.2f}'
          .format('\033[m',
                  (velocidade-80)*7))
else:
    print('\033[33mTenha um bom dia! Dirija com segurança!\033[m')

nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('[v0] Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
print('[v1] Seu nome tem ao todo {} letras'.format(len(nome.replace(' ', ''))))
print('[v0] Seu primeiro nome tem {} letras'.format(nome.find(' ')))
print('[v1] Seu primeiro nome tem {} letras'.format(len(nome.split()[0])))

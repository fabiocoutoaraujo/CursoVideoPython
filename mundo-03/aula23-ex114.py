from urllib import error, request
address = 'http://www.pudim.com.br/'
try:
     response = request.urlopen(address)
except error.URLError:
    print('ERRO: Verifique se o endereço do site foi informado corretamente!')
    print(address)
except Exception as erro:
    print(erro.__class__)
else:
    print('Consegui acessar o site Pudim com sucesso!')
    print('Código HTML:')
    print(response.read())

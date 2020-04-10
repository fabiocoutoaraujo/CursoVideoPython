cidade = str(input('Em que cidade você nasceu? ')).strip().lower()

print('v0 {}'.format(cidade[:5] == 'santo'))
print('v1 {}'.format('santo'in cidade.split()[0]))

from aula22_ex108 import formata_moeda
p = float(input('Digite o preço: R$ '))
print(f'A metade de {formata_moeda.formata(p)} é {formata_moeda.metade(p)}')
print(f'O dobro de {formata_moeda.formata(p)} é {formata_moeda.dobro(p)}')
print(f'Aumentando 10%, temos {formata_moeda.aumentar(p, 10)}')
print(f'Diminuindo 13%, temos {formata_moeda.diminuir(p, 13)}')

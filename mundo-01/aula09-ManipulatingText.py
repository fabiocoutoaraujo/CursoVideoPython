# C u r s o   e m   V  í d  e  o     P  y  t  h  o  n
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20

frase = 'Curso em Vídeo Python'

frase[9:13]     # 'Víde'
frase[9:21]     # 'Vídeo Python'
frase[9:21:2]   # 'VdoPto'
frase[:5]       # 'Curso'
frase[9]        # 'V'
frase[15:]      # 'Python'
frase[9::3]     # 'VePh'

len(frase)      # 21 caracteres

frase.count('o')            # 3 quantidades
frase.count('O')            # 0 quantidades
frase.upper().count('O')    # 3 quantidades
frase.count('o', 0, 13)     # 1 quantidade
frase.find('deo')           # 11 posição
frase.find('Android')       # -1
'Curso' in frase            # True
frase.replace('Python', 'Android')  # 'Curso em Vídeo Android'
frase.upper()
frase.lower()
frase.capitalize()          # 'Curso em vídeo python'
frase.title()               # 'Curso Em Vídeo Python'

frase = '   Aprenda Python  '

frase.strip()               # 'Aprenda Python'
frase.rstrip()              # '   Aprenda Python'
frase.lstrip()              # 'Aprenda Python  '

frase = 'Curso em Vídeo Python'

frase.split()               # ['Curso', 'em', 'Vídeo', 'Python']
'-'.join(frase)             # 'C-u-r-s-o- -e-m- -V-í-d-e-o- -P-y-t-h-o-n'

print(""" O cuidado em identificar pontos críticos no desafiador cenário globalizado 
nos obriga à análise do sistema de formação de quadros que corresponde às necessidades. 
As experiências acumuladas demonstram que o desenvolvimento contínuo de distintas formas 
de atuação prepara-nos para enfrentar situações atípicas decorrentes do orçamento setorial. 
Do mesmo modo, a crescente influência da mídia promove a alavancagem das diversas correntes 
de pensamento. """)


#   km    hm   dam   m   dm  cm   mm
# /1000  /100  /10      *10 *100 *1000
m = float(input('Uma distância em metros: '))

print('{} metros equivale à {:.3f} quilômetros' .format(m, (m/1000)))
print('{} metros equivale à {:.2f} hectômetros' .format(m, (m/100)))
print('{} metros equivale à {:.1f} decâmetros'  .format(m, (m/10)))
print('{} metros equivale à {:.0f} decímetros'  .format(m, (m*10)))
print('{} metros equivale à {:.0f} centímetros' .format(m, (m*100)))
print('{} metros equivale à {:.0f} milímetros'  .format(m, (m*1000)))

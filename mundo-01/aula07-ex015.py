k = float(input("Informe a quantidade de quilômetros percorridos: ").strip())
d = int(input("Informa a quantidade de dias: ").strip())
p = d * 60 + k * .15
print("O total a pagar é de R${:.2f}" .format(p))

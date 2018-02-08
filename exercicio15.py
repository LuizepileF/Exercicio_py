d = int(input('Quantos dias alugados?: '))
km = float(input('Quantos km rodado?: '))
rd = d * 60
rkm = km * 0.15
rf = rd + rkm
print("total a pagar e de R${:.2f}!".format(rf))

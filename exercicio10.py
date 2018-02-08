real = float(input('Quanto você tem na carteira? '))
dolar = real/3.41
yen = real/0.35
euro = real/4.19
print("com R${:.2f} você pode comprar U${:.2f}, ¥{:.2f}, €{:.2f}".format(real, dolar, yen, euro))

numero = float(input('Qual o pre�o do produto? '))
desconto = numero - (numero*5/100)
print("O produto que custava R${}, Com a promo��o de 5%, custara R${:.2f}".format(numero, desconto))

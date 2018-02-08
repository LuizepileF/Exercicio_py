numero = float(input('Qual o preço do produto? '))
desconto = numero - (numero*5/100)
print("O produto que custava R${}, Com a promoção de 5%, custara R${:.2f}".format(numero, desconto))

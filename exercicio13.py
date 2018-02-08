salario = float(input('Qual o salario do fucionario? R$'))
novo = salario + (salario * 15 / 100)
print("um fucionario que recebe R${:.2f}, com 15% de aumento, ele passa a receber R${:.2f}!".format(salario, novo))

resp = 'sim'
soma = 0
while resp == 'sim':
    print('deseja continuar? sim/nao')
    resp = raw_input()
    print('digite um valor: ')
    valor1 = input()
    soma = soma + valor1
    print(soma)

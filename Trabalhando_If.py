#! python3

def resPass():
    print('Digite 1- Para Se Cadastrar') #Printa Esse texto
    print('Digite 2- Para Fazer Login')
    resp = input() #Essa Linha ta uma entrada
    return resp

resp = resPass() #resp pode ter sido 1 ou 2

while True:
    if resp == '1': #comprando resp com um
        print('Bem Vindo - Área de Cadastro')
        print('Digite Seu Nome: ')
        name = input() #Se nome Lucas
        print('Digite Sua Senha: ')
        password1 = input()
        print('Digite Sua Senha Novamente: ')
        password2 = input()
        if password1 == password2: 
            print('Cadastrado Com Sucesso!')
            user = { name: password1}
            resp = resPass()
        elif password1 != password2:
            while password1 != password2:
                print('Suas Senhas Não Estão Iguais')
                print('Digite Sua Senha: ')
                password1 = input()
                print('Digite Sua Senha Novamente: ')
                password2 = input()
            print('Cadastrado Com Sucesso!')
            resp = resPass()
            user = { name: password1 }
    elif resp == '2':
        print('Bem Vindo Ao Nosso Programa')
        print('Digite Seu Login:')
        login = input()
        print('Digite Sua Senha')
        userPass = input()
        for key, value in user.items():
            if login == key and userPass == value:
                print('Logado Com Sucesso')
                break
            else:
                print('Você Não Se Encontra Cadastrado no Banco de Dados')
                resp = resPass()

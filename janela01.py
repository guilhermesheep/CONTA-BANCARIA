#usando while/else, para usar conta bancária
opcao = -1
saldo = 1000
saques = [] #criando uma lista de saques, para ser registrados no extrato
#inicio do programa
print('Bem vindo ao seu banco!, como podemos lhe ajudar?\nEscolha uma das opções para prosseguir no seu atendimento:\n')
print('Saldo:{}\n'.format(saldo))

while opcao != 0:
    opcao = int(input('[1] Sacar \n[2] Extrato \n[0] Sair \n:'))
    if opcao == 1:
        saque = float(input('Digite o valor do saque:'))
        if saldo >= saque:
            saldo -= saque
            saques.append(saque) #registra o saque na lista 
            print('Saque de {} realizado com sucesso!\nSeu saldo ficou:{}\n'.format(saque,saldo)) 
        else:
            print('saldo insuficiente')
    elif opcao == 2:
        print('exibindo extrato...')
        if len(saques) == 0:
            print('nenhuma saida registrada')
        else:
            for i, valor in enumerate(saques, start = 1): #enumerando os saques registrados da lista de saques []
                print('{}° saque:{}'.format(i,valor))
    elif opcao == 0:
        print('saindo...\n')
    else:
        print('opção invalida')
else:
    print('obrigado por usar nosso sistema bancário, até logo!')
    
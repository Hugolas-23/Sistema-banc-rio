def menu():
    print('Criar Conta - [1]')
    print('Realizar Depósito - [2]')
    print('Realizar Saque - [3]')
    print('Realizar Transferência - [4]')
    print('Verificar Saldo - [5]')
    print('Histórico de Transações - [6]')
    print('Verificar Valores - [7]')
    print("Informações da Conta - [8]")
    print('Sair - [0]')
    while True:
        try:
            opcao = int(input("\nDigite:\n"))
            if opcao not in [1, 2, 3, 4, 5, 6, 7, 8, 0]:
                print("\nOPÇÃO INVÁLIDA\n")
            else:
                break
        except ValueError:
            print("\nOPÇÃO INVÁLIDA\n")
    return opcao

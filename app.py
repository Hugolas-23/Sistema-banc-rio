from menu import *
from db import *
from construtor import *
from operacoes import *
from validacoes import *


if __name__ == '__main__':
    conexao = conexao()
    cursor = conexao.cursor()
    create_database(cursor)
    create_table_conta(cursor)
    create_table_transacoes(cursor)
    while True:
        op = menu()
        if op == 1:
            tc = input("QUAL O TIPO DA CONTA (pf/pj):")
            if tc == 'pf':
                nome = input('Digite seu nome:')
                saldo = float(input('Insira seu saldo:'))
                dt_nascimento = input('Digite sua data de nascimento:')
                cpf = input('Digite seu CPF:')
                conta = Conta_pf(nome, saldo, dt_nascimento, tc, cpf)
                criar_conta_pf(conta, conexao, cursor)
            elif tc == 'pj':
                nome = input('Digite seu nome:')
                saldo = float(input('Insira seu saldo:'))
                dt_nascimento = input('Digite sua data de criação:')
                cnpj = input('Digite seu CNPJ:')
                conta = Conta_pj(nome, saldo, dt_nascimento, tc, cnpj)
                criar_conta_pj(conta, conexao, cursor)
        elif op == 2:
            tipo, numero = tipo_conta(cursor)
            try:
                if tipo == 'pf':
                    deposito_pf(conexao, cursor, numero)
                else:
                    deposito_pj(conexao, cursor, numero)
            except ValueError as e:
                print(e)
        elif op == 3:
            tipo, numero = tipo_conta(cursor)
            try:
                if tipo == 'pf':
                    saque_pf(conexao, cursor, numero)
                else:
                    saque_pj(conexao, cursor, numero)
            except ValueError as e:
                print(e)
        elif op == 4:
            tipo, numero = tipo_conta(cursor)
            try:
                if tipo == 'pf':
                    transferencia_pf(conexao, cursor, numero)
                else:
                    transferencia_pj(conexao, cursor, numero)
            except ValueError as e:
                print(e)
        elif op == 5:
            tipo, numero = tipo_conta(cursor)
            mostra_saldo(cursor, numero)
        elif op == 6:
            tipo, numero = tipo_conta(cursor)
            historico_transacao(cursor, numero)
        elif op == 7:
            tipo, numero = tipo_conta(cursor)
            mostra_transacao(cursor, numero)
        elif op == 8:
            tipo, numero = tipo_conta(cursor)
            info_conta(cursor, tipo, numero)
        else:
            print("FIM")
            break

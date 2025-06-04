from validacoes import *


def criar_conta_pf(conta, conexao, cursor):
    cursor.execute('''
        INSERT INTO conta (nome, saldo, dt_nascimento, tipo_conta, cpf_cnpj)
        VALUES(%s, %s, %s, %s, %s)
    ''', (conta.nome, conta.saldo, conta.dt_nascimento, conta.tc, conta.cpf))
    conexao.commit()
    print("\nCONTA CRIADA\n")


def criar_conta_pj(conta, conexao, cursor):
    cursor.execute('''
            INSERT INTO conta (nome, saldo, dt_nascimento, tipo_conta, cpf_cnpj)
            VALUES(%s, %s, %s, %s, %s)
        ''', (conta.nome, conta.saldo, conta.dt_nascimento, conta.tc, conta.cnpj))
    conexao.commit()
    print("\nCONTA CRIADA\n")


def transferencia_pf(conexao, cursor, numero):
    transacao = 'transferência'
    limite = 2000
    taxa = 0.01
    id_transfere = numero
    cursor.execute('''
       SELECT saldo FROM conta
       WHERE numero = %s
       ''', (id_transfere,))
    resultado = cursor.fetchone()
    saldo_transfere = float(resultado[0])
    id_recebe = int(input('\nDigite o número da conta que irá receber:\n'))
    valida_numero(cursor, id_recebe)
    cursor.execute('''
       SELECT saldo FROM conta
       WHERE numero = %s
       ''', (id_recebe,))
    resultado = cursor.fetchone()
    saldo_recebe = float(resultado[0])
    valor = valida_negativo()
    if valor <= limite:
        valor_taxa = 0
        valida_operacao(valor, saldo_transfere)
        #serve para validar a operação
        saldo_transfere -= valor
        atualiza_saldo(cursor, conexao, saldo_transfere, id_transfere)
        saldo_recebe += valor
        atualiza_saldo(cursor, conexao, saldo_recebe, id_recebe)
        registrar_transacoes(conexao, cursor, transacao, id_transfere, id_recebe, valor, valor_taxa)
    else:
        valor_taxa = taxa * valor
        total = valor + valor_taxa
        #O TOTAL É PARA FACILITAR QUANDO PASSAR A VARIÁVEL PARA A FUNÇÃO
        print(f"\nSERÁ DESCONTADO O VALOR DE: R${valor_taxa}\n")
        valida_operacao(total, saldo_transfere)
        saldo_transfere -= total
        atualiza_saldo(cursor, conexao, saldo_transfere, id_transfere)
        saldo_recebe += valor
        atualiza_saldo(cursor, conexao, saldo_recebe, id_recebe)
        registrar_transacoes(conexao, cursor, transacao, id_transfere, id_recebe, total, valor_taxa)


def transferencia_pj(conexao, cursor, numero):
    transacao = 'transferência'
    limite = 5000
    taxa = 0.05
    id_transfere = numero
    cursor.execute('''
           SELECT saldo FROM conta
           WHERE numero = %s
           ''', (id_transfere,))
    resultado = cursor.fetchone()
    saldo_transfere = float(resultado[0])
    id_recebe = int(input('\nDigite o número da conta que irá receber:\n'))
    valida_numero(cursor, id_recebe)
    cursor.execute('''
           SELECT saldo FROM conta
           WHERE numero = %s
           ''', (id_recebe,))
    resultado = cursor.fetchone()
    saldo_recebe = float(resultado[0])
    valor = valida_negativo()
    if valor <= limite:
        valor_taxa = 0
        valida_operacao(valor, saldo_transfere)
        saldo_transfere -= valor
        atualiza_saldo(cursor, conexao, saldo_transfere, id_transfere)
        saldo_recebe += valor
        atualiza_saldo(cursor, conexao, saldo_recebe, id_recebe)
        registrar_transacoes(conexao, cursor, transacao, id_transfere, id_recebe, valor, valor_taxa)
    else:
        valor_taxa = taxa * valor
        total = valor + valor_taxa
        print(f"\nSERÁ DESCONTADO O VALOR DE: R${valor_taxa}\n")
        #O TOTAL É PARA FACILITAR QUANDO PASSAR A VARIÁVEL PARA A FUNÇÃO
        valida_operacao(total, saldo_transfere)
        saldo_transfere -= total
        atualiza_saldo(cursor, conexao, saldo_transfere, id_transfere)
        saldo_recebe += valor
        atualiza_saldo(cursor, conexao, saldo_recebe, id_recebe)
        registrar_transacoes(conexao, cursor, transacao, id_transfere, id_recebe, total, valor_taxa)


def deposito_pf(conexao, cursor, numero):
    transacao = 'depósito'
    limite = 2000
    taxa = 0.01
    valor = valida_negativo()
    cursor.execute('''
    SELECT saldo FROM conta
    WHERE numero = %s
    ''', (numero,))
    resultado = cursor.fetchone()
    saldo = float(resultado[0])
    if valor <= limite:
        valor_taxa = 0
        saldo += valor
        atualiza_saldo(cursor, conexao, saldo, numero)
        registrar_transacoes(conexao, cursor, transacao, None, numero, valor, valor_taxa)
    else:
        valor_taxa = taxa * valor
        print(f"\nSERÁ DESCONTADO O VALOR DE: R${valor_taxa}\n")
        saldo += (valor - valor_taxa)
        atualiza_saldo(cursor, conexao, saldo, numero)
        registrar_transacoes(conexao, cursor, transacao, None, numero, valor, valor_taxa)


def deposito_pj(conexao, cursor, numero):
    transacao = 'depósito'
    limite = 5000
    taxa = 0.05
    valor = valida_negativo()
    cursor.execute('''
    SELECT saldo FROM conta
    WHERE numero = %s
    ''', (numero,))
    resultado = cursor.fetchone()
    saldo = float(resultado[0])
    if valor <= limite:
        valor_taxa = 0
        saldo += valor
        atualiza_saldo(cursor, conexao, saldo, numero)
        registrar_transacoes(conexao, cursor, transacao, None, numero, valor, valor_taxa)
    else:
        valor_taxa = taxa * valor
        print(f"\nSERÁ DESCONTADO O VALOR DE: R${valor_taxa}\n")
        saldo += (valor - valor_taxa)
        atualiza_saldo(cursor, conexao, saldo, numero)
        registrar_transacoes(conexao, cursor, transacao, None, numero, valor, valor_taxa)


def saque_pf(conexao, cursor, numero):
    transacao = 'saque'
    limite = 2000
    taxa = 0.01
    valor = valida_negativo()
    cursor.execute('''
    SELECT saldo FROM conta
    WHERE numero = %s
    ''', (numero,))
    resultado = cursor.fetchone()
    saldo = float(resultado[0])
    if valor <= limite:
        valida_operacao(valor, saldo)
        valor_taxa = 0
        saldo -= valor
        atualiza_saldo(cursor, conexao, saldo, numero)
        registrar_transacoes(conexao, cursor, transacao, numero, None, valor, valor_taxa)
    else:
        valor_taxa = taxa * valor
        print(f"\nSERÁ DESCONTADO O VALOR DE: R${valor_taxa}\n")
        total = valor + valor_taxa
        #MESMA OPERAÇÃO UTILIZADA NA TRANSFERÊNCIA
        valida_operacao(total, saldo)
        saldo -= total
        atualiza_saldo(cursor, conexao, saldo, numero)
        registrar_transacoes(conexao, cursor, transacao, numero, None, total, valor_taxa)


def saque_pj(conexao, cursor, numero):
    transacao = 'saque'
    limite = 5000
    taxa = 0.05
    valor = valida_negativo()
    cursor.execute('''
    SELECT saldo FROM conta
    WHERE numero = %s
    ''', (numero,))
    resultado = cursor.fetchone()
    saldo = float(resultado[0])
    if valor <= limite:
        valida_operacao(valor, saldo)
        valor_taxa = 0
        saldo -= valor
        atualiza_saldo(cursor, conexao, saldo, numero)
        registrar_transacoes(conexao, cursor, transacao, numero, None, valor, valor_taxa)
    else:
        valor_taxa = taxa * valor
        print(f"\nSERÁ DESCONTADO O VALOR DE: R${valor_taxa}\n")
        total = valor + valor_taxa
        valida_operacao(total, saldo)
        saldo -= total
        atualiza_saldo(cursor, conexao, saldo, numero)
        registrar_transacoes(conexao, cursor, transacao, numero, None, total, valor_taxa)


def registrar_transacoes(conexao, cursor, transacao, n_conta_origem, n_conta_destino, valor_total, valor_taxa):

    sql = f'''
        INSERT INTO transacoes(transacao, n_conta_origem, n_conta_destino, valor_total, valor_taxa)
        VALUES(%s, %s, %s, %s, %s)
    '''
    #USO DE PLACEHOLDERS PARA PASSAR O VALOR NULL (NÃO FUNCIONA COM F') OBS: Com placeholders, os valores são identificados como valores de tupla. Por isso pode ser null
    cursor.execute(sql, (transacao, n_conta_origem, n_conta_destino, valor_total, valor_taxa))
    conexao.commit()
    print("SUA TRANSAÇÃO FOI REGISTRADA")


def info_conta(cursor, tipo, numero):
    cursor.execute('''
    SELECT * FROM conta
    WHERE numero = %s
    ''', (numero,))
    resultado = cursor.fetchall()
    if tipo == 'pf':
        for i in resultado:
            print(f'Número da conta: {i[0]}')
            print(f'Data de Criação: {i[1]}')
            print(f'Nome: {i[2]}')
            print(f'Saldo: {i[3]}')
            print(f'Data de Nascimento: {i[4]}')
            print(f'Tipo da conta: {i[5].upper()}')
            print(f'CPF/CNPJ: {i[6]}')
    else:
        for i in resultado:
            print(f'Número da conta: {i[0]}')
            print(f'Data de Criação: {i[1]}')
            print(f'Nome: {i[2]}')
            print(f'Saldo: {i[3]}')
            print(f'Data de Criação: {i[4]}')
            print(f'Tipo da conta: {i[5].upper()}')
            print(f'CPF/CNPJ: {i[6]}')


def mostra_saldo(cursor, numero):
    cursor.execute('''
        SELECT nome, saldo FROM conta
        WHERE numero = %s
    ''', (numero,))
    resultado = cursor.fetchone()
    print(f'{resultado[0]}: R${resultado[1]}')


def historico_transacao(cursor, numero):
    cursor.execute('''
        SELECT * FROM transacoes 
        WHERE n_conta_origem = %s OR
        n_conta_destino = %s
    ''', (numero, numero))
    resultado = cursor.fetchall()
    if resultado:
        for i in resultado:
            print(f'ID: {i[0]}; Transação: {i[1]}; Conta origem: {i[2]}; Conta destino: {i[3]}; Valor Total: R${i[4]}; Valor Taxa: R${i[5]}; Horário: {i[6]}')
    else:
        print("NENHUMA TRANSAÇÃO RESGISTRADA")


def mostra_transacao(cursor, numero):
    cursor.execute('''
        SELECT c.nome, t.transacao, t.valor_total FROM conta as c
        INNER JOIN transacoes as t
        ON c.numero = t.n_conta_origem OR c.numero = t.n_conta_destino
        WHERE c.numero = %s
    ''', (numero,))
    resultado = cursor.fetchall()
    for i in resultado:
        print(
            f'Nome: {i[0]}; Saldo: R${i[1]}; Transação: {i[2]}; Valor Total: R${i[3]}')

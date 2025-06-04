def tipo_conta(cursor):
    numero = input("\nDigite o número da conta\n")
    valida_numero(cursor, numero)
    cursor.execute(f'''
        SELECT tipo_conta FROM conta
        WHERE numero = %s
    ''', (numero,))
    resultado = cursor.fetchone()
    return resultado[0], numero


def atualiza_saldo(cursor, conexao, saldo, numero):
    cursor.execute('''
                    UPDATE conta
                    SET saldo = %s
                    WHERE numero = %s
                    ''', (saldo, numero))
    conexao.commit()
    print("\nSALDO ATUALIZADO\n")


def valida_negativo():
    valor = float(input('\nDigite o valor a ser depositado: \n'))
    if valor <= 0:
        raise ValueError("\nVALOR INVÁLIDO\n")
    else:
        print("\nVALOR VALIDADO\n")
        return valor


def valida_operacao(valor, saldo):
    if valor > saldo:
        raise ValueError("\nOPERAÇÃO INVALIDADA\n")
    else:
        print("\nOPERAÇÃO VALIDADA\n")


def valida_numero(cursor, numero):
    cursor.execute(f'''
        SELECT numero FROM conta
        WHERE numero = %s
    ''', (numero, ))
    teste = cursor.fetchall()
    if len(teste) == 0:
        raise ValueError("\nO NÚMERO DA CONTA NÃO EXISTE\n")
    else:
        print("\nCONTA VALIDADA\n")

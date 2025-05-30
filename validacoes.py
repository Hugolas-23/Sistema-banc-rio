def tipo_conta(cursor):
    numero = input("DIGITE O NÚMERO DA SUA CONTA")
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
    print("SALDO ATUALIZADO")


def valida_negativo():
    valor = float(input('digite o valor a ser depositado:'))
    if valor <= 0:
        raise ValueError("VALOR INVÁLIDO")
    else:
        print("VALOR VALIDADO")
        return valor


def valida_operacao(valor, saldo):
    if valor > saldo:
        raise ValueError("OPERAÇÃO INVALIDADA")
    else:
        print("OPERAÇÃO VALIDADA")


def valida_numero(cursor, numero):
    cursor.execute(f'''
        SELECT numero FROM conta
        WHERE numero = %s
    ''', (numero, ))
    teste = cursor.fetchall()
    if len(teste) == 0:
        raise ValueError("O NÚMERO DA CONTA NÃO EXISTE")
    else:
        print("CONTA VALIDADA")
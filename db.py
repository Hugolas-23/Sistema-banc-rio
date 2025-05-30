import mysql.connector


def conexao():
    conexao_db = mysql.connector.connect(user='root', password='hugo23125', host='localhost')
    print('CONEXÃO:', conexao_db)
    return conexao_db


def create_database(cursor):
    sql = '''CREATE DATABASE IF NOT EXISTS db_banco
    '''
    cursor.execute(sql)
    sql_use = '''USE db_banco'''
    cursor.execute(sql_use)


def create_table_transacoes(cursor):
    sql = '''
        CREATE TABLE IF NOT EXISTS transacoes(
        id_transacao integer AUTO_INCREMENT,
        transacao VARCHAR(20) NOT NULL,
        n_conta_origem integer NULL,
        n_conta_destino integer NULL,
        valor_total DECIMAL(9,2) NOT NULL,
        valor_taxa DECIMAL(9,2) NULL,
        horario TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (n_conta_origem) REFERENCES conta(numero),
        FOREIGN KEY (n_conta_destino) REFERENCES conta(numero),
        PRIMARY KEY(id_transacao)
        )
    '''
    cursor.execute(sql)


def create_table_conta(cursor):
    sql = '''
       CREATE TABLE IF NOT EXISTS conta(
       numero integer AUTO_INCREMENT,
       dt_criacao DATE DEFAULT (CURDATE()),
       nome VARCHAR(50),
       saldo DECIMAL(9,2),
       dt_nascimento DATE,
       tipo_conta enum('pf','pj') NOT NULL,
       cpf_cnpj VARCHAR(14) UNIQUE,
       PRIMARY KEY(numero)
       )
    '''
    cursor.execute(sql)

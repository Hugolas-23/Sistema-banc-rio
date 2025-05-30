class Conta:
    def __init__(self, nome='', saldo=0, dt_nascimento='', tc='', taxa=0, limite=0):
        self.nome = nome
        self.saldo = saldo
        self.dt_nascimento = dt_nascimento
        self.taxa = taxa
        self.limite = limite
        self.tc = tc

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_saldo(self):
        return self.saldo

    def set_saldo(self, saldo):
        if saldo >= 0:
            self.saldo = saldo
        else:
            print("Saldo não pode ser negativo.")

    def get_dt_nascimento(self):
        return self.dt_nascimento

    def set_dt_nascimento(self, dt_nascimento):
        self.dt_nascimento = dt_nascimento

    def get_taxa(self):
        return self.taxa


class Conta_pf(Conta):
    def __init__(self, nome='', saldo=0, dt_abertura='', tc='', cpf='', taxa=0.01, limite=2000):
        super().__init__(nome, saldo, dt_abertura, tc, taxa, limite)
        self.cpf = cpf

    def get_cpf(self):
        return self.cpf

    def set_cpf(self, cpf):
        self.cpf = cpf


class Conta_pj(Conta):
    def __init__(self, nome, saldo, dt_nascimento, tc='', cnpj='', taxa=0.05, limite=5000):
        super().__init__(nome, saldo, dt_nascimento, tc, taxa, limite)
        self.cnpj = cnpj

    def get_cnpj(self):
        return self.cnpj

    def set_cnpj(self, cnpj):
        self.cnpj = cnpj

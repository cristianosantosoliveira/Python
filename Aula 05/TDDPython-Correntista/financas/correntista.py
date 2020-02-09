class Correntista:
    def __init__(self, nome, cpf, saldo_inicial):
        self.__nome = nome
        self.__cpf = cpf
        self.__saldo = saldo_inicial

    def nome(self):
        return self.__nome

    def cpf(self):
        return self.__cpf

    def saldo(self):
        return self.__saldo

    def deposita(self, valor, auditor):
        if not isinstance(valor, float):
            raise TypeError("Valor deve ser float")

        if valor <= 0.0:
            raise ValueError(f"Valor '{valor}' não permitido para deposito")

        self.__saldo += valor
        auditor.auditar(self.__cpf, 'deposito', valor)

    def saque(self, valor, auditor):
        if not isinstance(valor, float):
            raise TypeError("Valor deve ser float")

        if valor <= 0.0:
            raise ValueError(f"Valor '{valor}' não permitido para saque")

        if valor > self.__saldo:
            raise ValueError(f"Saldo insuficiente para saque no valor de '{valor}'")

        self.__saldo -= valor
        auditor.auditar(self.__cpf, 'saque', valor)

    def serialize(self):
        return {
            'nome': self.__nome,
            'cpf': self.__cpf,
            'saldo': self.__saldo
        }

    @classmethod
    def deserialize(cls, data):
        return Correntista(
            data['nome'],
            data['cpf'],
            data['saldo']
        )

    
from .correntista import Correntista
from .auditoria import Auditoria

class Banco:
    def __init__(self):
        self.__correntistas = []
        self.__auditoria = Auditoria()

    def auditor(self):
        return self.__auditoria

    def cadastra_correntista(self, correntista):
        self.__correntistas.append(correntista)

    def correntistas(self):
        return self.__correntistas

    def procura_correntista(self, nome):
        procura = []

        for c in self.__correntistas:
            if nome in c.nome():
                procura.append(c)

        return procura

    def serialize(self):
        return {
            'correntistas': [ c.serialize() for c in self.__correntistas ],
            'auditoria': self.__auditoria.serialize()
        }

    @classmethod
    def deserialize(cls, data):
        b = Banco()
        b.__correntistas = [Correntista.deserialize(c) for c in data['correntistas']]
        b.__auditoria = Auditoria.deserialize(data['auditoria'])

        return b
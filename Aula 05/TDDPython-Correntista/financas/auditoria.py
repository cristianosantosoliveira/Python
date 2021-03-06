class Auditoria:
    def __init__(self):
        self.__audicoes = []

    def auditar(self, cpf, tipo, valor):
        self.__audicoes.append({
            'cpf': cpf,
            'tipo': tipo,
            'valor': valor
        })
        
    def registros(self, cpf=''):
        if cpf == '':
            return self.__audicoes

        filtrado = []
        for aud in self.__audicoes:
            if aud['cpf'] == cpf:
                filtrado.append(aud)

        return filtrado

    def serialize(self):
        return {
            'audicoes': self.__audicoes
        }
        
    @classmethod
    def deserialize(cls, data):
        a = Auditoria()
        a.__audicoes = data['audicoes']

        return a
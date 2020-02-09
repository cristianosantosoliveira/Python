deposito = 0.00
valor = 0.00

class Correntista:
    def __init__(self, name, conta, agencia, saldo=0.0):
        self.name = name
        self.conta = conta
        self.agencia = agencia
        self.saldo = saldo
        self.historico = []
        self.index = 0

 
    def imrprime(self):
        print("Nome: ", self.name)
        print("Número da Conta: ", self.conta)
        print("Agência: ", self.agencia)
        print("Saldo: ", self.saldo)

    
    def depositar(self, deposito):
        if (deposito > 0):
            self.saldo += deposito
            self.historico.append({"Tipo":'Deposito', "Valor":deposito})
        else:
            print("Opereção recusada.")
    
    def sacar(self, saque):
        if (self.saldo >= saque):
            if(saque > 0):
                self.saldo -= saque
                self.historico.append({"Tipo":'Saque', "Valor":saque})
            else: 
                print("Valor inválido.")
        else:
            print("Saldo insuficiente.")

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.historico):
            raise StopIteration
        self.index = self.index + 1
        return self.historico[self.index - 1]
 

d = Correntista('Cristiano Oliveira','5525-9', 5158, 200)
e = Correntista('Cristiano Silva E', '66090-4', 6548, 300)
f = Correntista('Cristiano Ronaldo', '66907-4', 8984, 400)
g = Correntista('Cristiano Ronaldo da Silva', '1505-3', 5554, 900)
 

print("Entrato Correntista OLIST")
print('-' * 40)

d.depositar(100.00)
d.imrprime()

print('-' * 40)
e.sacar(150)
e.imrprime()

print('-' * 40)
f.imrprime()

print('-' * 40)
g.imrprime()

for historico in e:
    print(historico)







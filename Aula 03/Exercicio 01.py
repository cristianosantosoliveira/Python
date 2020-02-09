
class Correntista:
    numero = 5517
    nome = "Cristiano"
    saldo = 1000.00

    numero2 = 1436
    nome2 = "Cristiano Oliveira"
    saldo2 = 500.00

    deposito = 900.00

    def depositar (self, deposito):
        self.saldo + deposito
    
    def sacar (self, saque):
        if (self.saldo >= saque):
            self.saldo - saque
        else:
            print("Saldo insuficiente.")

    
    print('-' * 40)
    print("Conta número: ", numero, "Correntista: ", nome, "Saldo: ", saldo)
    print("O valor depositado é:", deposito)
    #print("O valor sacado foi: ", saque)

 



  
             
class InputOverflowError(Exception):
    pass

'''
class AuditriaCorrentista(Auditoria):
    pass

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.auditoria):
            raise StopIteration
        self.index = self.index + 1
        return self.auditoria[self.index - 1]

'''
class banco():
    pass
    def __init__(self, name = '', conta = '', agencia = '', cpf = '', codigo_banco = '', banco = '', saldo=0.0):
        self.name = name
        self.conta = conta
        self.agencia = agencia
        self.cpf = cpf
        self.codigo_banco = codigo_banco
        self.saldo = saldo
        self.auditoria = []
        self.index = 0

    def cadastrar_correntista(self, name, conta, agencia, cpf, codigo_banco, banco, saldo):
        name = input ("Digite o nome do cliente: ")
        conta = input ("Digite o numero da conta: ")
        agencia = input ("Por favor, informe a agencia: ")
        cpf = input ("Informe o CPF: ")
        codigo_banco = input ("Digite o do Banco: ")
        banco = input ("Digite o Banco: ")
        saldo = input ("Informe o saldo inicial: ")


class correntista:
from .banco import banco
    def __init__(self, name = '', conta = '', agencia = '', cpf = '', saldo=0.0):
        self.name = name
        self.conta = conta
        self.agencia = agencia
        self.cpf = cpf
        self.saldo = saldo
        self.historico = []
        self.index = 0

 
    def imprime(self):
        print("Nome: ", self.name)
        print("Número da Conta: ", self.conta)
        print("Agência: ", self.agencia)
        print("CPF: ", self.cpf)
        print("Saldo: ", self.saldo)

    
    def depositar(self, deposito):
        if (deposito > 0):
            self.saldo =+ deposito
            self.historico.append({"Tipo":'Deposito', "Valor":deposito})
        else:
            print("Opereção recusada.")
    
    def sacar(self, saque):
        if (self.saldo >= saque):
            if(saque > 0):
                self.saldo =- saque
                self.historico.append({"Tipo":'Saque', "Valor":saque})
            else: 
                print("Valor inválido.")
        else:
            print("Saldo insuficiente.")

    

cc = Correntista('','', 0, 0, 0)
#d = sacar('Cristiano Oliveira','5525-9', 5158, 0)


   
def imprimeMenu():
    print ("1 - Fazer Depósito")
    print ("2 - Fazer Saque")
    print ("3 - Auditoria")
    print ("4 - Cadastrar Correntista")
    print ("5 - Selecionar Correntista")
    print ("6 - Sair")


while True:
    try:
        print("================= OPERAÇÕES DISPONIVEIS =================")
        imprimeMenu()
        opcao = int (input ("Por favor, escolha uma opção valida: "))
        if int (opcao) == 1:
            print("============= DEPOSITO EM PROCESSAMENTO =============")
            deposito = int(input ("Quanto você quer depositar? "))
            Correntista.depositar(cc, int(deposito))    

        elif int (opcao) == 2:
            print("============== SAQUE EM PROCESSAMENTO ==============")
            saque = int(input ("Quanto voce quer sacar? "))
            Correntista.sacar(cc, saque)    
            
            continue
        elif opcao == 3:
            print("=============== HISTORICO CORRENTISTA ===============")
            Correntista.imprime(cc)
            continue
        elif int (opcao) == 4:
            print("=============== CADASTRAR CORRENTISTA ===============")
            cc = Correntista(Banco.cadastrar_correntista(name, conta, agencia, cpf, codigo_banco, banco, saldo))               
        
            continue
        elif int (opcao) == 5:
            print("============== HISTORICO EM PROCESSAMENTO ==============")
            Correntista.imprime(cc)
            continue
        elif int (opcao) == 6:
            print("============== FECHANDO O SISTEMA ==============")
            break
        else:
            break 
    except InputOverflowError as error:    
        print ("Um erro ocorreu tente novamente!", error)  
        break  
print ("Até Breve!")


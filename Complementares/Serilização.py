import pickle

class Computador:
    def __init__(self, marca, processador, ram):
        self.marca = marca
        self.processador = processador
        self.ram = ram
    
    def __repr__(self):
        return 'Marca: {} - Processador: {} - RAM: {}'.format(self.marca, self.processador, self.ram)

computador = Computador('DELL', 'I5', '128GB')

print(computador)

print(type(computador))





 ##Serilização
 arquivo_destino = 'persistencia.dat'

 with open(arquivo_destino, 'wb') as f:
     print(pickle.dumps(computador))
     pickle.dump(computador, f)
print()

##Deserilização do Objeto
with open(arquivo_destino, 'rb') as f:
    dados = pickle.load(f)

    print(dados)
    print(type(dados))

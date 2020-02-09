import json
from financas.correntista import Correntista
from financas.banco import Banco

b = Banco()
c = Correntista('Leo', '11111111111', 10.0)
c.saque(5.0, b.auditor())
c.deposita(42.0, b.auditor())
b.cadastra_correntista(c)

# Persiste...
salvo_no_arquivo = json.dumps(b.serialize(), indent=4)

# Carrega...
data = json.loads(salvo_no_arquivo)
novo_b = Banco.deserialize(data)
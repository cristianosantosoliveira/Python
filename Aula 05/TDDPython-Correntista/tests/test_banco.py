import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from unittest.mock import Mock
from financas.banco import Banco

class Correntista:
    pass

class TestBanco(unittest.TestCase):
    def setUp(self):
        self.banco = Banco()

    def test_cadastro_correntista(self):
        correntista = Mock(spec=Correntista)
        correntista.cpf = Mock(return_value='01234567890')

        self.banco.cadastra_correntista(correntista)

        correntistas = self.banco.correntistas()
        self.assertIsInstance(correntistas[0], Correntista)
        self.assertEqual(correntistas[0].cpf(), '01234567890')

    def test_listagem_correntistas(self):
        correntista1 = Mock(spec=Correntista)
        correntista1.cpf = Mock(return_value='01234567890')
        correntista2 = Mock(spec=Correntista)
        correntista2.cpf = Mock(return_value='11111111111')

        self.banco.cadastra_correntista(correntista1)
        self.banco.cadastra_correntista(correntista2)
        correntistas = self.banco.correntistas()

        self.assertIsInstance(correntistas[0], Correntista)
        self.assertIsInstance(correntistas[1], Correntista)
        self.assertEqual(correntistas[0].cpf(), '01234567890')
        self.assertEqual(correntistas[1].cpf(), '11111111111')

    def test_procura_correntista(self):
        correntista1 = Mock(spec=Correntista)
        correntista1.cpf = Mock(return_value='01234567890')
        correntista1.nome = Mock(return_value='Homer Simpson')
        correntista2 = Mock(spec=Correntista)
        correntista2.cpf = Mock(return_value='11111111111')
        correntista2.nome = Mock(return_value='Bart Simpson')

        self.banco.cadastra_correntista(correntista1)
        self.banco.cadastra_correntista(correntista2)

        procura1 = self.banco.procura_correntista('Homer')
        self.assertEqual(procura1[0].cpf(), '01234567890')

        procura2 = self.banco.procura_correntista('Simpson')
        cpfs_procura = [c.cpf() for c in procura2]
        self.assertCountEqual(cpfs_procura, ['01234567890', '11111111111'])

if __name__ == "__main__":
    unittest.main()
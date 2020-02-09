import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from unittest.mock import Mock
from financas.correntista import Correntista

class TestCorrentista(unittest.TestCase):
    def setUp(self):
        self.correntista = Correntista("Nome", "12345678901", 10.0)

    def test_atributos(self):
        self.assertEqual(self.correntista.nome(), "Nome")
        self.assertEqual(self.correntista.cpf(), "12345678901")
        self.assertEqual(self.correntista.saldo(), 10.0)

    def test_deposito(self):
        auditor = Mock()

        self.correntista.deposita(10.0, auditor)
        self.assertEqual(self.correntista.saldo(), 20.0)

        auditor.auditar.assert_called_with(self.correntista.cpf(), 'deposito', 10.0)

    def test_deposito_invalido(self):
        auditor = Mock()

        with self.assertRaises(ValueError):
            self.correntista.deposita(-5.0, auditor)
        with self.assertRaises(ValueError):
            self.correntista.deposita(0.0, auditor)
        with self.assertRaises(TypeError):
            self.correntista.deposita("aa", auditor)

        auditor.auditar.assert_not_called()

    def test_saque(self):
        auditor = Mock()

        self.correntista.saque(5.0, auditor)
        self.assertEqual(self.correntista.saldo(), 5.0)
        self.correntista.saque(1.0, auditor)
        self.assertEqual(self.correntista.saldo(), 4.0)

        auditor.auditar.assert_any_call(self.correntista.cpf(), 'saque', 5.0)
        auditor.auditar.assert_any_call(self.correntista.cpf(), 'saque', 1.0)

    def test_saque_invalido(self):
        auditor = Mock()

        with self.assertRaises(ValueError):
            self.correntista.saque(-10.0, auditor)
        with self.assertRaises(ValueError):
            self.correntista.saque(0.0, auditor)
        with self.assertRaises(TypeError):
            self.correntista.saque("a", auditor)

        auditor.auditar.assert_not_called()

    def test_saque_proibido(self):
        auditor = Mock()
        
        with self.assertRaises(ValueError):
            self.correntista.saque(20.0, auditor)

        auditor.auditar.assert_not_called()

if __name__ == "__main__":
    unittest.main()
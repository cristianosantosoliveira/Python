import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from financas.auditoria import Auditoria

class TestAuditoria(unittest.TestCase):
    def setUp(self):
        self.auditoria = Auditoria()

    def test_auditar(self):
        self.auditoria.auditar('01234567891', 'deposito', 10.0)
        self.auditoria.auditar('01234567891', 'saque', 10.0)
        
        self.assertEqual(len(self.auditoria.registros('01234567891')), 2)

    def test_registros(self):
        self.assertEqual(len(self.auditoria.registros()), 0)
        self.assertEqual(len(self.auditoria.registros('99999999999')), 0)

        self.auditoria.auditar('01234567891', 'deposito', 10.0)
        self.auditoria.auditar('01234567891', 'deposito', 5.0)
        self.auditoria.auditar('65465465465', 'deposito', 20.0)
        self.assertEqual(len(self.auditoria.registros()), 3)
        self.assertEqual(len(self.auditoria.registros('99999999999')), 0)
        
        filtrado = self.auditoria.registros('01234567891')
        auditoria = filtrado[0]
        self.assertEqual(len(filtrado), 2)
        self.assertEqual(auditoria['cpf'], '01234567891')
        self.assertEqual(auditoria['valor'], 10.0)

if __name__ == "__main__":
    unittest.main()

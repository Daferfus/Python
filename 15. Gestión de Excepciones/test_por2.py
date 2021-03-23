import unittest
from por2 import *
import sys
sys.path.insert(1, './')
class Pruebas(unittest.TestCase):
    # test
    def test_pruebas(self):
        ret = por2(5)
        self.assertEqual(ret, 10)
        #assertRaisesRegex(excepción, mensaje, función, parámetros)
        self.assertRaisesRegex(ValueError, "El valor es negativo", por2, -1)
if __name__ == "__main__":
    unittest.main()
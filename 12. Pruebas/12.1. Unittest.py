import unittest
from funciones import *

class Pruebas(unittest.TestCase):

    def test_max_num_in_list(self):
        self.assertEqual(max_num_in_list([3,4,5]), 5)
        self.assertEqual(max_num_in_list([4,5,3]), 5)
        self.assertEqual(max_num_in_list([5,4,3]), 5)
        self.assertEqual(max_num_in_list([-3,-4,-5]), -3)
        self.assertEqual(max_num_in_list([]), "undefined")

if __name__ == "__main__":
    unittest.main()

def test_max_num_in_list(self):
        lista = [3,4,5]
        self.assertEqual(max_num_in_list(lista), 5)
        lista = [4,5,3]
        self.assertEqual(max_num_in_list(lista), 5)
        lista.append(-50)
        self.assertEqual(len(lista), 4)
        self.assertEqual(max_num_in_list(lista), 5)
        lista = []
        self.assertEqual(max_num_in_list([]), "undefined")
        lista = [-1, -5, -15]
        self.assertEqual(max_num_in_list(lista), -1)

import unittest

class Pruebas(unittest.TestCase):

    def test_1(self):
        lista = [3,4,5]
        self.assertEqual(max_num_in_list(lista), 5)
    
    def test_2(self):
        lista = [-1, -5, -15]
        self.assertEqual(max_num_in_list(lista), -1)

class Suite(unittest.TestSuite):

    def __init__(self):
        super(Suite, self).__init__()        
        self.addTest(Pruebas('test_1'))
        self.addTest(Pruebas('test_2'))
        #el siguiente código sería equivalente
        #self.addTests([Pruebas('test_1'),Pruebas('test_2')])

if __name__ == "__main__":    
    runner = unittest.TextTestRunner()
    my_suite = Suite()
    runner.run(my_suite)
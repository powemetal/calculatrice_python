import unittest
from src.calculatrice.operations import Operations

class TestOperations(unittest.TestCase):

    def setUp(self):
        self.operations = Operations()
        self.operations.ajouter_terme(5)
        self.operations.ajouter_operation("+")

    def test_initialisation(self):
        self.assertEqual(self.operations.termes, [5])
        self.assertEqual(self.operations.operateurs, ["+"])

    def test_ajouter_terme(self):
        self.operations.ajouter_terme(10)
        self.assertEqual(self.operations.termes, [5, 10])

    def test_ajouter_mauvais_terme(self):
        with self.assertRaises(ValueError):
            self.operations.ajouter_terme("dix")
    
    def test_ajouter_operation(self):
        self.operations.ajouter_operation("*")
        self.assertEqual(self.operations.operateurs, ["+", "*"])

    def test_ajouter_mauvaise_operation(self):
        with self.assertRaises(ValueError):
            self.operations.ajouter_operation("%")
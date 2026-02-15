import unittest
from src.calculatrice.app import Calculatrice

class TestCalculatrice(unittest.TestCase):

    def setUp(self):
        self.calculatrice = Calculatrice()

    def test_initialisation(self):
        self.assertEqual(self.calculatrice.resultat, 0)
        self.assertIsNotNone(self.calculatrice.memoires)
        self.assertIsNotNone(self.calculatrice.console)
        self.assertIsNotNone(self.calculatrice.validate_input)

        # Test addition
    def test_calculer(self):
        nombres = iter([5, 10])
        operateurs = iter(["+", "="])
        self.calculatrice.validate_input.input_number = lambda memoires: next(nombres)
        self.calculatrice.validate_input.input_operateur = lambda: next(operateurs)
        resultat = self.calculatrice.calculer()
        self.assertEqual(resultat, 15)

        # Test division by zero
    def test_diviser_par_zero(self):
        nombres = iter([5, 0])
        operateurs = iter(["/", "="])
        self.calculatrice.validate_input.input_number = lambda memoires: next(nombres)
        self.calculatrice.validate_input.input_operateur = lambda: next(operateurs)
        resultat = self.calculatrice.calculer()
        self.assertEqual(resultat, 0)
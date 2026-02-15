import unittest
from src.calculatrice.memoires import Memoires

class TestMemoires(unittest.TestCase):

    def setUp(self):
        self.memoires = Memoires()

    def test_initialisation(self):
        self.assertEqual(self.memoires.memoires, {"M1": None, "M2": None, "M3": None, "M4": None, "M5": None})

    def test_sauvegarder_memoire(self):
        self.memoires.sauvegarder_memoire("M1", 5)
        self.assertEqual(self.memoires.memoires["M1"], 5)
        self.assertEqual(self.memoires.memoires, {"M1": 5, "M2": None, "M3": None, "M4": None, "M5": None})

    def test_sauvegarder_memoire_invalide(self):
        with self.assertRaises(KeyError):
            self.memoires.sauvegarder_memoire("M6", 5)

    def test_effacer_toute_la_memoire(self):
        self.memoires.sauvegarder_memoire("M1", 5)
        self.memoires.sauvegarder_memoire("M2", 10)
        self.memoires.effacer_toute_la_memoire()
        self.assertEqual(self.memoires.memoires, {"M1": None, "M2": None, "M3": None, "M4": None, "M5": None})

    def test_utiliser_memoire(self):
        self.memoires.sauvegarder_memoire("M1", 5)
        self.assertEqual(self.memoires.utiliser_memoire("M1"), 5)
        self.assertEqual(self.memoires.utiliser_memoire("M2"), None)


    def test_utiliser_memoire_invalide(self):
        with self.assertRaises(KeyError):
            self.memoires.utiliser_memoire("M6")

    def test_effacer_memoire(self):
        self.memoires.sauvegarder_memoire("M1", 5)
        self.memoires.effacer_memoire("M1")
        self.assertEqual(self.memoires.memoires["M1"], None)

    def test_effacer_memoire_invalide(self):
        with self.assertRaises(KeyError):
            self.memoires.effacer_memoire("M6")

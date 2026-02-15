class Memoires:
    def __init__(self):
        self.memoires = {"M1" : None, "M2" : None, "M3" : None, "M4" : None, "M5" : None}

    def utiliser_memoire(self, memoire):

        return self.memoires[memoire]

    def sauvegarder_memoire(self, memoire, valeur):
        if memoire not in self.memoires:
            raise KeyError(f"Memoire {memoire} n'existe pas!")
        self.memoires[memoire] = valeur

    def effacer_memoire(self, memoire):
        if memoire not in self.memoires:
            raise KeyError(f"Memoire {memoire} n'existe pas!")
        self.memoires[memoire] = None

    def effacer_toute_la_memoire(self):
        for cle in self.memoires:
            self.memoires[cle] = None

    def __str__(self):
            valeurs = []
            for memoire, valeur in self.memoires.items():
                valeurs.append(f"{memoire} : {valeur}")
            return " ".join(valeurs)

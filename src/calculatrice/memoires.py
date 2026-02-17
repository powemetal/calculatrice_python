class Memoires:
    def __init__(self):
        self.memoires = {"M1" : None, "M2" : None, "M3" : None, "M4" : None, "M5" : None}

    def utiliser_memoire(self, memoire):
        """
        Retourne la valeur de la memoire specifiee
        :param memoire: Nom de la memoire a utiliser (example: M1...M5)
        :raises KeyError: Si la mémoire n'existe pas.
        """
        if memoire not in self.memoires:
            raise KeyError(f"Memoire {memoire} n'existe pas!")
        return self.memoires[memoire]

    def sauvegarder_memoire(self, memoire, valeur):
        """
        Sauvegarde la valeur dans la memoire specifiee

        :param memoire: Nom de la memoire a utiliser (example: M1...M5)
        :param valeur: Valeur a sauvegarder dans la memoire
        :raises KeyError: Si la mémoire n'existe pas.
        """
        if memoire not in self.memoires:
            raise KeyError(f"Memoire {memoire} n'existe pas!")
        self.memoires[memoire] = valeur

    def effacer_memoire(self, memoire):
        """
        Efface la valeur dans la memoire choisie
        
        :param memoire: Nom de la memoire a utiliser (example: M1...M5)
        :raises KeyError: Si la mémoire n'existe pas.
        """
        if memoire not in self.memoires:
            raise KeyError(f"Memoire {memoire} n'existe pas!")
        self.memoires[memoire] = None

    def effacer_toute_la_memoire(self):
        """
        Efface toutes les memoires en les reinitialisant a None        
        """
        for cle in self.memoires:
            self.memoires[cle] = None

    def __str__(self):
        """
        Representation textuelle des memoires et de leur valeurs
        """
        valeurs = []
        for memoire, valeur in self.memoires.items():
            valeurs.append(f"{memoire} : {valeur}")
        return " ".join(valeurs)

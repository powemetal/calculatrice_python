class ConsoleUI:

    def __init__(self):
        pass

    
    def afficher_message(self, message):
        print(message)

    def afficher_menu(self, resultat, memoires):
        self.afficher_message(f"""
-------------------------------
      Calculatrice Python
{memoires}
Dernier resultat: {resultat}
-------------------------------
1- Effectuer un calcul
2- Enregistrer le resultat dans la memoire
3-
4- Quitter

""")
    
    def afficher_menu_gestion_memoire(self, resultat, memoires):
        self.afficher_message(f"""
-------------------------------
      Calculatrice Python
{memoires}
Dernier resultat: {resultat}
-------------------------------
1- Enregistrer le resultat actuel dans une mémoire
2- Effacer le contenu d'une mémoire
3- Effacer toute la mémoire
4- Quitter

""")

    def afficher_operations(self, calcul_en_cours):
        affichage_calculs = []
        for nombre, operation in zip(calcul_en_cours.termes, calcul_en_cours.operateurs):
            affichage_calculs.append(str(nombre))
            affichage_calculs.append(operation)
        affichage_calculs.append(str(calcul_en_cours.termes[-1]))
        return " ".join(affichage_calculs)

    def afficher_total(self, resultat, calcul_en_cours):
        return self.afficher_operations(calcul_en_cours) + " = " + str(resultat)

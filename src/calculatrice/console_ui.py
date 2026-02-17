class ConsoleUI:

    def __init__(self):
        pass

    
    def afficher_message(self, message):
        """
        Affiche un message à l'utilisateur dans la console
        
        :param message: Message à afficher dans la console
        """
        print(message)

    def afficher_menu(self, resultat, memoires):
        """
        Affiche le menu principal de la calculatrice avec les options disponibles,
        les mémoires et le dernier résultat.

        :param resultat: Le dernier résultat calculé
        :param memoires: L'état actuel des mémoires
        """
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
        """Affiche le menu de gestion de la mémoire avec les options disponibles, 
        les mémoires et le dernier résultat.

        :param resultat: Le dernier résultat calculé
        :param memoires: L'état actuel des mémoires"""
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
        """
        Affiche les opérations en cours de saisie par l'utilisateur pour le calcul en cours.
        
        :param calcul_en_cours: L'objet de la classe Operations qui contient les termes et les opérateurs saisis par l'utilisateur pour le calcul en cours
        :return: Une chaîne de caractères représentant les opérations en cours de saisie
        """
        affichage_calculs = []
        for nombre, operation in zip(calcul_en_cours.termes, calcul_en_cours.operateurs):
            affichage_calculs.append(str(nombre))
            affichage_calculs.append(operation)
        affichage_calculs.append(str(calcul_en_cours.termes[-1]))
        return " ".join(affichage_calculs)

    def afficher_total(self, resultat, calcul_en_cours):
        """
        Affiche le résultat final du calcul en cours avec les opérations effectuées.

        :param resultat: Le résultat final du calcul en cours
        :param calcul_en_cours: L'objet de la classe Operations qui contient les termes et les opérateurs saisis par l'utilisateur pour le calcul en cours
        :return: Une chaîne de caractères représentant les opérations effectuées et le résultat final
        """
        return self.afficher_operations(calcul_en_cours) + " = " + str(resultat)


from .operations import Operations
from .memoires import Memoires
from .console_ui import ConsoleUI
from .validate_input import ValidateInput


class Calculatrice:
    
    def __init__(self):
        self.memoires = Memoires()
        self.console = ConsoleUI()
        self.validate_input = ValidateInput(self.console)
        self.resultat = 0

    #boucle while de la calculatrice
    def main_menu(self):
        """
        Menu principal de la calculatrice qui affiche les options disponibles et gère les choix de l'utilisateur pour effectuer des calculs, gérer les mémoires ou quitter l'application.
            L'utilisateur peut choisir entre 4 options:
            1. Effectuer un calcul
            2. Gérer les mémoires
            3. Afficher l'historique des calculs (en cours de développement)
            4. Quitter l'application
            La fonction boucle jusqu'à ce que l'utilisateur choisisse de quitter l'application.        
        """
        while True:
            self.console.afficher_menu(self.resultat, self.memoires)
            match self.validate_input.input_menu():
                case 1:
                    self.resultat = self.calculer()
                case 2:
                    self.gestion_de_la_memoire_menu()
                case 3:
                    self.console.afficher_message("En cours de developpement")
                case 4:
                    self.console.afficher_message("Merci d'avoir utilisé la calculatrice, au revoir!")
                    break
                case _:
                    self.console.afficher_message("Ce choix est invalide! choisissez entre 1 et 4")


    def calculer(self):
        """
        Effectue un calcul en respectant l'ordre des opérations et en gérant les erreurs telles que la division par zéro ou les entrées invalides.
        
        La fonction boucle jusqu'à ce que l'utilisateur entre un opérateur "=" pour indiquer la fin du calcul, puis affiche le résultat final. 
        Pendant le processus de calcul, les entrées de l'utilisateur sont validées pour s'assurer qu'elles sont des nombres valides et que les 
        opérateurs sont parmi les options supportées (+, -, *, /). En cas d'erreur, un message approprié est affiché et le calcul est interrompu.
        """
        while True:
            calcul_en_cours = Operations() 
            #----les entrees utilisaeurs sont doublement validees, une fois dans la classe validate_input et une autre fois dans la classe operations, pour assurer que les erreurs sont bien geres et que le programme ne plante pas
            try:
                calcul_en_cours.ajouter_terme(self.validate_input.input_number(self.memoires))
            except ValueError as e:
                self.console.afficher_message(str(e))
                return 0

                #boucle jusqu'a temps d'avoir un operateur =
            while True:
                self.console.afficher_message(self.console.afficher_operations(calcul_en_cours))
                try:
                    operateur = self.validate_input.input_operateur()
                except ValueError as e:
                    self.console.afficher_message(str(e))
                    return 0
                if operateur == "=":
                    try:
                        resultat_final = calcul_en_cours.total()
                    except ZeroDivisionError:
                        self.console.afficher_message("Erreur: Division par zéro!")
                        return 0
                    self.console.afficher_message(self.console.afficher_total(resultat_final, calcul_en_cours))
                    return resultat_final
                    
                else:
                    calcul_en_cours.ajouter_operation(operateur)
                    calcul_en_cours.ajouter_terme(self.validate_input.input_number(self.memoires))


    def gestion_de_la_memoire_menu(self):
        """
        Menu de gestion de la mémoire qui permet à l'utilisateur de sauvegarder le résultat d'un calcul dans une mémoire spécifique, d'effacer une mémoire ou d'effacer toutes les mémoires.
            L'utilisateur peut choisir entre 4 options:
            1. Sauvegarder le résultat dans une mémoire (M1 à M5)
            2. Effacer une mémoire spécifique (M1 à M5)
            3. Effacer toutes les mémoires
            4. Retourner au menu principal
            La fonction boucle jusqu'à ce que l'utilisateur choisisse de retourner au menu principal.
        """
        while True:
            self.console.afficher_menu_gestion_memoire(self.resultat, self.memoires)
            match self.validate_input.input_menu():
                case 1:
                    memoire = self.validate_input.input_memoire(self.memoires)
                    if memoire is None:
                        self.console.afficher_message("Sauvegarde annulée.")
                        continue
                    try:
                        self.memoires.sauvegarder_memoire(memoire, self.resultat) 
                    except KeyError as e:
                        self.console.afficher_message(str(e))
                case 2:
                    try:
                        self.memoires.effacer_memoire(self.validate_input.input_memoire(self.memoires))
                    except KeyError as e:
                        self.console.afficher_message(str(e))   
                case 3:
                    self.memoires.effacer_toute_la_memoire()
                case 4:
                    break
                case _:
                    self.console.afficher_message("Ce choix est invalide! choisissez entre 1 et 4")
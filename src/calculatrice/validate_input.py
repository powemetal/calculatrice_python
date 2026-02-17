class ValidateInput():
    """
    Classe pour valider les entrees de l'utilisateur 
    autant dans les menus que dans les calculs
    """
    def __init__(self, console):
        self.console = console


    def input_number(self, memoires):
        """
        Valide l'entrée d'un nombre ou l'utilisation d'une mémoire.

        L'utilisateur peut entrer :
        - un nombre (converti en float)
        - le nom d'une mémoire (M1 à M5), auquel cas la valeur stockée est retournée

        La fonction boucle jusqu'à obtenir une entrée valide.

        :param memoires: Instance de la classe Memoires.
        :return: Un float ou la valeur d'une mémoire.
        """

        self.console.afficher_message("")
        while True:
            number = input("Entrez un nombre: ").strip()
            if number in memoires.memoires:
                self.console.afficher_message(f"Memoire {number}: {memoires.memoires[number]}")
                return memoires.memoires[number]
            else:
                try:
                    number = float(number)
                except ValueError:
                    self.console.afficher_message("Veuillez entrer un nombre valide")
                    continue
                return number
            
                

    def input_operateur(self):
        """
        Valide l'opérateur utilisé pour un calcul.

        L'utilisateur doit entrer un opérateur parmi : +, -, *, / ou =.
        La fonction boucle jusqu'à obtenir une entrée valide.

        :return: Un opérateur valide.
        """

        self.console.afficher_message("")
        while True:
            operateur = input("Entrez l'operateur souhaité ( + - * / = ): ").strip()
            if operateur in ["/", "*", "-", "+", "="]:
                return operateur
            else:
                self.console.afficher_message("Veuillez entrer un operateur valide (+ - * / =)")


    def input_memoire(self, memoires):
        """
        Validation du choix de la memoire pour stocker le resultat ou l'effacer
        L'utilisateur peut entrer : un choix de memoire parmi M1 à M5 pour stocker le resultat ou a pour annuler le choix de la memoire
        La fonction boucle jusqu'à obtenir une entrée valide.
        
        :param memoires: l'objet de la classe Memoires pour valider l'utilisation de la memoire dans les calculs
        :return: le nom de la memoire choisie ou None si l'utilisateur annule le choix de la memoire
        """
        self.console.afficher_message("")
        while True:
            self.console.afficher_message(memoires)
            choix_memoire = input("Choisissez une mémoire (M1-M5 ou a pour annuler): ")
            if choix_memoire.upper() in ["M1", "M2", "M3", "M4", "M5"]:
                return choix_memoire.upper()
            elif choix_memoire.lower() == "a":
                return None
            else:
                self.console.afficher_message("Ce choix de mémoire est invalide! Choisissez entre (M1-M5) ou a pour annuler")

    def input_menu(self):
        """
        Valide le choix de l'utilisateur dans les menus (principal ou gestion mémoire).

        L'utilisateur doit entrer un nombre entier correspondant aux options affichées.
        La fonction boucle jusqu'à obtenir une entrée valide.

        :return: Le choix validé
        """

        self.console.afficher_message("")
        while True:
            try:
                number = int(input("Entrez un nombre de 1 a 4: ").strip())
            except ValueError:
                self.console.afficher_message("Veuillez entrer un nombre valide")
                continue
            return number

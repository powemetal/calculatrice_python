class ValidateInput():
    def __init__(self, console):
        self.console = console


    def input_number(self, memoires):
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
                    self.console.afficher_message("Veuillez un nombre valide")
                    continue
                return number
            
                

    def input_operateur(self):
        self.console.afficher_message("")
        while True:
            operateur = input("Entrez l'operateur souhaité ( + - * / = ): ").strip()
            if operateur in ["/", "*", "-", "+", "="]:
                return operateur
            else:
                self.console.afficher_message("Veuillez entrer un operateur valide (+ - * / =)")


    def input_memoire(self, memoires):
        self.console.afficher_message("")
        while True:
            self.console.afficher_message(memoires)
            choix_memoire = input("Choisissez une mémoire (M1-M5) ou a pour annuler): ")
            if choix_memoire.upper() in ["M1", "M2", "M3", "M4", "M5"]:
                return choix_memoire.upper()
            elif choix_memoire.lower() == "a":
                return None
            else:
                self.console.afficher_message("Ce choix de mémoire est invalide! Choisissez entre (M1-M5) ou a pour annuler")

    def input_menu(self):
        self.console.afficher_message("")
        while True:
            try:
                number = int(input("Entrez un nombre de 1 a 4: ").strip())
            except ValueError:
                self.console.afficher_message("Veuillez un nombre valide")
                continue
            return number

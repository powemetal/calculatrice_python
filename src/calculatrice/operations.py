class Operations():
    def __init__(self):
        self.operateurs = []
        self.termes = []

    def ajouter_terme(self, terme):
        """
        Revalidation du terme et ajout du terme a la liste des termes pour le calcul
        
        :param self: Description
        :param terme: Description
        """
        if not isinstance(terme, (int, float)):
            raise ValueError("Le terme doit être un nombre entier ou à virgule flottante.")
        self.termes.append(terme)

    def ajouter_operation(self, operateur):
        """
        Validation de l'operateur et ajout de l'operateur a la liste des operateurs pour le calcul
        
        :param self: Description
        :param operateur: Description
        """
        if operateur not in ["+", "-", "*", "/"]:
            raise ValueError("L'opérateur doit être l'un des suivants: +, -, *, /.")
        self.operateurs.append(operateur)

    def total(self):
        """
        Effectue le calcul en respectant l'ordre des operations et en vérifiant qu'il n'y a pas de division par zéro
        
        :param self: Description
        """
        calculs = []
        for nombre, operation in zip(self.termes, self.operateurs):
            calculs.append(nombre)
            calculs.append(operation)
        calculs.append(self.termes[-1])

        for i, terme in enumerate(calculs):
            if terme == "/":
                if calculs[i + 1] == 0:
                    raise ZeroDivisionError("Erreur! Division par Zero impossible")

        for operateur in ["/", "*", "+", "-"]:
            index = 1
            while index < len(calculs):
                if calculs[index] == operateur:
                    resultat = (
                        calculs[index - 1] / calculs[index + 1] if operateur == "/" else
                        calculs[index - 1] * calculs[index + 1] if operateur == "*" else
                        calculs[index - 1] + calculs[index + 1] if operateur == "+" else
                        calculs[index - 1] - calculs[index + 1]
                    )
                    calculs[index - 1] = resultat
                    del calculs[index + 1]
                    del calculs[index]
                else:
                    index += 1
        return calculs[0]

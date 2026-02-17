from .app import Calculatrice

def main():
    """
    Point d'entrée de l'application de la calculatrice.
    Crée une instance de la classe Calculatrice et lance le menu principal.
    """
    cal = Calculatrice()
    cal.main_menu()

if __name__ == "__main__":
    main()

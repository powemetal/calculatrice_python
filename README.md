# Calculatrice Python
![Python](https://img.shields.io/badge/Python-3.12-blue)![Code Style](https://img.shields.io/badge/Code%20Style-PEP8-informational)

##    Description
Une simple calculatrice Python créée comme exercice de pratique et de révision pour l'examen de fin de session du cours Concepts de programmation 1 de l’AEC Développement de logiciels du Collège de Maisonneuve.  

L’objectif principal était de renforcer ma compréhension de l’utilisation des classes dans un projet modulaire, extensible et maintenable.  Ce projet vise également à démontrer une architecture propre, une séparation claire des responsabilités et une couverture complète des tests unitaires — le tout en partant de zéro.

---
## Objectifs pédagogiques
Cet exercice m’a permis de travailler plusieurs compétences: :
- Solidier ma compréhension de la programmation orientée objet
- Structurer un projet Python de manière professionnelle
- Développer de façon modulaire et testable
- Gérer l’ordre des opérations sans utiliser `eval()` a l'aide d'un algorithme 
- Écrire des tests unitaires
- Manipuler des structures de données pour interpréter des expressions
Ces objectifs ont guidé mes choix techniques et la structure du projet.


---
## Choix techniques

### Séparation des classes

J’ai choisi de séparer les classes en fonction de leurs responsabilités afin de respecter le principe de responsabilité unique (Single Responsibility Principle).

Chaque composant a un rôle précis :
- `Operations` Gère les operations et applique l'ordre des opérations
- `Memoires` Gère l'acces aux mémoires de la calculatrice
- `ConsoleUI` Gère l'affichage des messages d'entrée ou d'erreur
- `ValidateInput` Contrôle les entrées utilisateur
- `Calculatrice` Orchestre l'ensemble dans l'ordre établit

Cette séparation permet d’avoir un code plus facile à lire et à maintenir, d’écrire plus facilement des tests unitaires et d’ajouter de nouvelles fonctionnalités sans modifier toute la structure.

### Pourquoi ne pas utiliser eval() ou des modules externes

Même si Python permet d’évaluer une expression avec `eval()`, j'ai préféré implémenter moi-même la logique de calcul.

L’objectif était de tester ma compréhension du traitement des opérations en gérant manuellement la priorité des opérateurs et en manipulant les structures de données.Je voulais renforcer ma compréhension des algorithmes plutôt que d’utiliser une solution déjà intégrée.


---

##    Fonctionnalités principales
- Évaluation d'expressions complètes
- Gestion de mémoires (M1 - M5)
- Validation robuste des entrées
- Tests unitaires
- Prise en charge de l'ordre des opérations

Exemples :
- Calculs en chaîne et prise en charge de l'ordre des opérations: 5 + 8 * 4 - 32 = 5
- Les mémoires peuvent être utilisées directement en écrivant M1-M5 au lieu d'un terme dans les équations
- Les entrées sont vérifiées autant a l'entrée utilisateur que lors de l'ajout dans les operations


---

##    Architecture du projet

```
src/
└── calculatrice/
    ├── app.py
    ├── operations.py
    ├── memoires.py
    ├── console_ui.py
    └── validate_input.py

tests/
├── test_app.py
├── test_memoires.py
└── test_operations.py


```

##  Principes d’architecture
Séparation UI / logique métier
Validation défensive
Code modulaire, extensible et testable


## Installation et exécution
1. Cloner le projet.
```bash
git clone https://github.com/powemetal/calculatrice_python/
cd calculatrice_python
```

2. Lancer l’application.
```bash
python -m src.calculatrice.main
```

3. Lancer les tests.
```bash
python -m unittest discover tests
```

## Ce que j’ai appris
- Organiser un projet Python de manière professionnelle
- Écrire des tests unitaires
- Séparer les responsabilités dans une architecture modulaire
- Gérer les erreurs proprement

## Améliorations possibles
- Prise en charge des parenthèses
- Ajout d’opérations avancées (exposants, modulo, racine)
- Ajouter un historique des calculs
- Utiliser des @staticmethod dans validate_input
- Faire une classe ErrorManager pour centraliser la gestion des erreurs


## Licence
MIT

## Auteur
**Francis Boisvert**  
Étudiant en développement logiciel  
Collège de Maisonneuve



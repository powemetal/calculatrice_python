# Calculatrice Python
![Python](https://img.shields.io/badge/Python-3.14-blue)![Code Style](https://img.shields.io/badge/Code%20Style-PEP8-informational)

##    Description
Une simple calculatrice Python créée comme exercice de pratique et de révision pour l'examen de fin de session du cours Concepts de programmation 1 de l’AEC Développement de logiciels du Collège de Maisonneuve.  

L’objectif principal était de renforcer ma compréhension de l’utilisation des classes dans un projet modulaire, extensible et maintenable. Ce projet vise également à démontrer une architecture propre, une séparation claire des responsabilités et une couverture complète des tests unitaires — le tout en partant de zéro.

---


##    Fonctionnalités principales
- Évaluation d'expressions complètes
- Gestion de mémoires (M1 - M5)
- Validation robuste des entrées
- Tests unitaires
- Prise en charge de l'ordre des opérations

Exemples :
- Calculs en chaîne (+, -, *, /)
- Gestion de mémoires M1–M5
- Validation robuste des entrées
- Tests unitaires complets

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


## Licence
MIT

## Auteur
**Francis Boisvert**  
Étudiant en développement logiciel  
Collège de Maisonneuve

# Calculatrice python
![Python](https://img.shields.io/badge/Python-3.14-blue)![Code Style](https://img.shields.io/badge/Code%20Style-PEP8-informational)

##    Description
Une simple calculatrice python créée comme exercice de pratique et de révision pour l'examen de fin de session du cours "Concepts de programmation 1" de l'AEC "Développement de logiciels" du collège de Maisonneuve. L'objectif principal était de renforcer ma compréhesion de l'utilisation des classes dans le cadre d'un projet modulaire, extensible et maintenable. Ce projet vise également à demontrer une architecture prope, une separation claire des responsabilités et une couverture des tests unitaires, le tout, en partant de zéro.


---

##    Fonctionnalités principales
- Evaluation d'expressions complètes
- Gestion de mémoires (M1 - M5)
- Validation robuste des entrées
- Tests unitaires
- Prise en charge de l'ordre des operations

Exemple :
- Calculs en chaîne (+, -, *, /)
- Gestion de mémoires M1–M5
- Validation robuste des entrées
- Tests unitaires complets


---

##    Architecture du projet
src/
  calculatrice/
    app.py
    operations.py
    memoires.py
    console_ui.py
    validate_input.py
tests/
  test_app.py
  test_memoires.py
  tests_operations.py


##  Principes d’architecture
Séparation UI / logique métier
Validation défensive
Code modulaire, extensible et testable


## Installation et exécution
1. Cloner le projet
git clone <URL de ton dépôt>
cd <nom_du_dossier>
git clone <URL de ton dépôt>
cd <nom_du_dossier>


## Lancer l’application
python -m src.calculatrice.main

## Lancer les test
python -m unittest discover tests

## Ce que j’ai appris
- Organiser un projet Python de manière professionnelle
- Écrire des tests unitaires
- Séparer les responsabilités dans une architecture modulaire
- Gérer les erreurs proprement

## Améliorations possible
- Prise en charge des parenthèses
- Prise en charge d'autres opérations (exposants, modulo, racine)
- Ajouter un historique des calculs


## Licence


## Auteur
Francis Boisvert  
Étudiant en développement logiciel  
Collège de Maisonneuve

# Simulation d'interaction proies-prédateurs avec Python (Wa-Tor)

README

Il s'agit d'un algorithme permettant d'observer le comportement d'une population de poissons et d'une population de requins dans une mer de forme torique.

## Pré-requis
- Python, en particulier la Programmation Orientée Objet (POO)

## Démarrage
Exécutez le programme avec **VSCODE**. Vous pourrez observer dans la console la création d'une mer suivant des dimensions qui peuvent varier, dans laquelle interagissent la population de **proies (notée 1)** avec la population de **prédateurs (notée 2)**. Les '**-**' représent les **cases vides**, c'est-à-dire de l'eau.

## Comprendre les différents comportements
Les poissons:
  1. **se déplacent** si les cases autour d'eux sont libres
  2. **se reproduisent** s'ils ont atteint un certain nombre de chonons (ou unités de temps) et s'ils peuvent se déplacer
 
Les requins:
  1. **se nourrissent** des proies adjacentes, ce qui leur procurent de l'énergie
  2. **se déplacent** suivant les mêmes critères que les poissons mais perdent des unités d'énergie à chaque tour
  3. **se reproduisent** aussi de la même façon 
  
Le programme se termine dès que l'une ou l'autre population est éteinte.
  
## Fabriqué avec
  - **Visual Studio Code** - Editeur de code
  - **Git** - Logiciel de gestion.
  - **GitHub** - Site web et service de cloud pour stocker et gérer le code.
  - **Python** - Langage de programmation interprété.

## Version
  Dernière version: 1.0
  
## Auteur.e.s
  - Yanis KAHOUL alias yaniskahoul
  - Nina NUSBAUMER alias NinaNusb

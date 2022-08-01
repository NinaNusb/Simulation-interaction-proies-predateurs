from random import randint
import os
from time import sleep

ENERGIE_REPRODUCTION_POISSON = 2
ENERGIE_REPRODUCTION_REQUIN = 5
ENERGIE_REQUIN_MAX = 4

class Monde:
    def __init__(self, largeur_monde, hauteur_monde):
        self.grille = [[None for _ in range(hauteur_monde)] for _ in range(largeur_monde)]
        self.largeur = largeur_monde
        self.hauteur = hauteur_monde

    def afficher_monde(self):
        for ligne in self.grille:
            for case in ligne:
                if case is None:
                    print("-", end=" ")
                elif isinstance(case, Requin):
                   print("X", end=" ")
                else:
                    print("O", end=" ")
            print("\n")

    def peupler(self, nb_requin, nb_poisson):
        for i in range(nb_poisson):
            x_rand = randint(0, self.largeur -1)
            y_rand = randint(0, self.hauteur - 1)
            while self.grille[x_rand][y_rand] is not None:
                x_rand = randint(0, self.largeur-1)
                y_rand = randint(0, self.hauteur-1)
            self.grille[x_rand][y_rand] = Poisson(x_rand, y_rand)
        for i in range(nb_requin):
            x_rand = randint(0, self.largeur -1)
            y_rand = randint(0, self.hauteur - 1)
            while self.grille[x_rand][y_rand] is not None:
                x_rand = randint(0, self.largeur-1)
                y_rand = randint(0, self.hauteur-1)
            self.grille[x_rand][y_rand] = Requin(x_rand, y_rand)
    
    def tour_du_monde(self):
        for ligne in self.grille:
            for elt in ligne:
                if elt is not None:
                    elt.jouer_tour(self)

class Animaux:
    def __init__(self, pos_x, pos_y):
        self.x = pos_x
        self.y = pos_y
        self.compteur_reproduction = 0
    
    def obtenir_cases_adjacente_libre(self, monde):
        cases_vide = []
        if monde.grille[self.x][self.y - 1] is None:
            #Vérifie la case nord
            cases_vide.append((self.x, (self.y - 1)%monde.hauteur))

        if monde.grille[self.x][(self.y + 1)%monde.hauteur] is None:
            #Vérifie la case sud
            cases_vide.append((self.x, (self.y + 1)%monde.hauteur))

        if monde.grille[(self.x + 1)%monde.largeur][self.y] is None:
            #Vérifie la case est
            cases_vide.append(((self.x + 1)%monde.largeur, self.y))

        if monde.grille[(self.x - 1)%monde.largeur][self.y] is None:
            cases_vide.append(((self.x - 1)%monde.largeur, self.y))
        
        return cases_vide

    def se_deplacer(self, monde):
        coups_possibles = Animaux.obtenir_cases_adjacente_libre(self, monde)
        if len(coups_possibles) > 0:
            x_precedent = self.x
            y_precedent = self.y
            coup_a_jouer = coups_possibles[randint(0, len(coups_possibles)-1)]
            self.x, self.y = coup_a_jouer
            monde.grille[coup_a_jouer[0]][coup_a_jouer[1]] = self
            monde.grille[x_precedent][y_precedent] = None


class Requin(Animaux):
    compteur = 0
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
        self.energie = ENERGIE_REQUIN_MAX
        Requin.compteur += 1
    
    def __del__(self):
        Requin.compteur -= 1
    
    def proies_adjacentes(self, monde):
        cases_proie = []
        if type(monde.grille[self.x][self.y - 1]) is Poisson:
            #Vérifie la case nord
            cases_proie.append((self.x, (self.y - 1)%monde.hauteur))

        if type(monde.grille[self.x][(self.y + 1)%monde.hauteur]) is Poisson:
            #Vérifie la case sud
            cases_proie.append((self.x, (self.y + 1)%monde.hauteur))

        if type(monde.grille[(self.x + 1)%monde.largeur][self.y]) is Poisson:
            #Vérifie la case est
            cases_proie.append(((self.x + 1)%monde.largeur, self.y))

        if type(monde.grille[self.x - 1][self.y]) is Poisson:
            cases_proie.append(((self.x - 1)%monde.largeur, self.y))
            
        return cases_proie
    
    def se_reproduire(self, monde, x_preced, y_preced):
        monde.grille[x_preced][y_preced] = Requin(x_preced, y_preced)

    def manger(self, monde):
        coups_possibles = Requin.proies_adjacentes(self, monde)
        if len(coups_possibles) > 0:
            x_precedent = self.x
            y_precedent = self.y
            coup_a_jouer = coups_possibles[randint(0, len(coups_possibles)-1)]
            self.x, self.y = coup_a_jouer
            monde.grille[self.x][self.y] = self
            monde.grille[x_precedent][y_precedent] = None
            self.energie = ENERGIE_REQUIN_MAX
                  
    def jouer_tour(self, monde):
        x_preced, y_preced = self.x, self.y
        if self.energie == 0:
            monde.grille[self.x][self.y] = None
        elif len(self.proies_adjacentes(monde)) >= 1:
            self.manger(monde)
        elif len(self.obtenir_cases_adjacente_libre(monde)) >= 1:
            self.se_deplacer(monde)
        
        if self.compteur_reproduction >= ENERGIE_REPRODUCTION_REQUIN:
            self.se_reproduire(monde, x_preced, y_preced)
            self.compteur_reproduction = 0
        self.energie -= 1
        self.compteur_reproduction += 1
    
class Poisson(Animaux):
    compteur = 0
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
        Poisson.compteur += 1
    
    def __del__(self):
        Poisson.compteur -= 1
        
    def se_reproduire(self, monde, x_preced, y_preced):
        monde.grille[x_preced][y_preced] = Poisson(x_preced, y_preced)
    
    def jouer_tour(self, monde):
        x_preced, y_preced = self.x, self.y
        if len(self.obtenir_cases_adjacente_libre(monde)) >= 1:
            self.se_deplacer(monde)
        if self.compteur_reproduction >= ENERGIE_REPRODUCTION_POISSON:
            self.se_reproduire(monde, x_preced, y_preced)
            self.compteur_reproduction = 0
        else:
            self.se_deplacer(monde)
        self.compteur_reproduction += 1


monde = Monde(15, 45)
monde.peupler(15, 100)
max_poisson = 0
max_requin = 0

while Poisson.compteur != 0 and Requin.compteur != 0:
    if Poisson.compteur > max_poisson:
        max_poisson = Poisson.compteur
    if Requin.compteur > max_requin:
        max_requin = Requin.compteur
    monde.tour_du_monde()
    monde.afficher_monde()
    print("Nb Requins : " + str(Requin.compteur), end=" ")
    print("Nb Poisson : " + str(Poisson.compteur))
    sleep(0.8 )
    os.system("clear")

print("Nb max de requin : " + str(max_requin) + " survivants : " + str(Requin.compteur))
print("Nb max de poisson : " + str(max_poisson) + " survivants : " + str(Poisson.compteur))



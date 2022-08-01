from random import randint, choice
import os 
from time import sleep


class World:
    """La classe monde nous permet de déterminer la taille de l'environnement, de l'afficher, de remplir de manière aléatoire les cases soit de poisson, soit de requin.
    Cette classe permet de passer un jour donc de voir l'évolution des animaux."""

    def __init__(self, largeur_x, hauteur_y):
        self.grille = [[None for _ in range(largeur_x)] for _ in range(hauteur_y)]
        self.largeur_x = largeur_x
        self.hauteur_y = hauteur_y

    def afficher_world(self): 
        for ligne in self.grille:
            str_ligne = ''
            for case in ligne:
                if isinstance(case, Fish): 
                    str_ligne += ' 1 '
                elif isinstance(case, Requin):
                    str_ligne += ' 2 '
                else:
                    str_ligne += ' 0 '
            print(str_ligne)

    def peupler(self, pop_fish, pop_shark): #rajouter condition 'pas l'un sur l'autre'
        for _ in range(pop_fish):
            position_x = randint(0,self.largeur_x -1)
            position_y = randint(0, self.hauteur_y -1)
            while self.grille[position_y][position_x] is not None: 
                position_x = randint(0, self.largeur_x -1)
                position_y = randint(0, self.hauteur_y -1)
            self.grille[position_y][position_x] = Fish(position_x, position_y) 
        for _ in range(pop_shark):
            position_x = randint(0,self.largeur_x -1)
            position_y = randint(0, self.hauteur_y -1)
            while self.grille[position_y][position_x] is not None: #potentielle erreur
                position_x = randint(0, self.largeur_x -1)
                position_y = randint(0, self.hauteur_y -1)
            self.grille[position_y][position_x] = Requin(position_x, position_y) #potentielle erreur
        
  
    def passer_un_jour(self):
        for ligne in self.grille:
            for case in ligne:
                if isinstance(case, Animal): #a verifier
                    case.vivre_une_journée(self)
                        
 
          

class Animal:
    """Cette classe permet aux animaux de se déplacer et de se reproduire. """
    def __init__(self, position_x, position_y): #tout ce qui se passe à la création d'un animal #param car au moment de l'appel ce sont les choses qui peuvent changer
        self.position_x = position_x #placer 1 animal par case de façon random
        self.position_y = position_y
        self.chronon_to_breed = 0 #unité en chronons
        #self.coordonnees = [self.position_x] [self.position_y]


    def case_adjacente_libre(self, monde):
        coup_possible = []
        if monde.grille[(self.position_y+1) % monde.hauteur_y][self.position_x] == None:
            coup_possible.append((self.position_x, (self.position_y +1) % monde.hauteur_y))
        if monde.grille[(self.position_y-1)% monde.hauteur_y][self.position_x] == None:
            coup_possible.append((self.position_x, (self.position_y -1) % monde.hauteur_y))
        if monde.grille[self.position_y][(self.position_x+1) % monde.largeur_x] == None:
            coup_possible.append(((self.position_x+1) % monde.largeur_x, self.position_y))
        if monde.grille[self.position_y][(self.position_x-1) % monde.largeur_x] == None:
            coup_possible.append(((self.position_x-1) % monde.largeur_x, self.position_y))
        return(coup_possible)

    def move(self, mer): 
        #if len(coups_possibles) > 0:
        ex_pos_x = self.position_x
        ex_pos_y = self.position_y
        new_position = choice(self.case_adjacente_libre(mer))
        self.position_x = new_position[0] #permet de faire une copie (car référence vers objet stoqué et non l'objet lui-même)
        self.position_y = new_position[1]
        mer.grille[self.position_y][self.position_x] = self
        mer.grille[ex_pos_y][ex_pos_x] = None

    def breed(self):
        if self.chronon_to_breed %3 == 0:
            ex_pos_x = self.position_x
            ex_pos_y = self.position_y
            new_position = choice(self.case_adjacente_libre(mer))
            self.position_x = new_position[0]
            self.position_y = new_position[1]
            mer.grille[self.position_y][self.position_x] = self
            mer.grille[ex_pos_y][ex_pos_x] = Animal(ex_pos_y, ex_pos_x)
        return True 


    def vivre_une_journée(self, monde): #à modifier
        ex_pos_x = self.position_x
        ex_pos_y = self.position_y
        if len(self.case_adjacente_libre(monde)) > 0:
            self.move(monde)
        if self.chronon_to_breed > 3: #reproduction
            monde.grille[ex_pos_x][ex_pos_y] = Requin(ex_pos_x, ex_pos_y)
            self.chronon_to_breed = 0
        else:
            self.move(monde)
        self.chronon_to_breed += 1
   
        
class Fish(Animal): #compteur manquant
    def __init__(self, position_x, position_y):
        super().__init__(position_x, position_y)

class Requin(Animal): #compteur manquant
    def __init__(self, position_x, position_y):
        super().__init__(position_x, position_y)
        self.energy = 7


    def poissons_adjacents(self, monde): 
        proies_possibles= []
        
        if type(monde.grille[(self.position_y+1) % monde.hauteur_y][self.position_x]) == Fish:
            proies_possibles.append((self.position_x, (self.position_y +1) % monde.hauteur_y))

        if type(monde.grille[(self.position_y-1)% monde.hauteur_y][self.position_x]) == Fish:
            proies_possibles.append((self.position_x, (self.position_y -1) % monde.hauteur_y))

        if type(monde.grille[self.position_y][(self.position_x+1) % monde.largeur_x]) == Fish:
            proies_possibles.append(((self.position_x+1) % monde.largeur_x, self.position_y))

        if type(monde.grille[self.position_y][(self.position_x-1) % monde.largeur_x]) == Fish:
            proies_possibles.append(((self.position_x-1) % monde.largeur_x, self.position_y))
        return(proies_possibles)
    
    

    def eat(self, mer): #A TESTER
        #le requin regarde les 4 position adjacentes et si il ya un poisson il le tue
        #food = self.case_adjacente_occupée 
        #if food == True:
        shark_pos_x = self.position_x           
        shark_pos_y = self.position_y
        fish_position = choice(self.case_adjacente_occupée(mer))
        self.position_x = fish_position[0]
        self.position_y = fish_position[1]
        mer.grille[self.position_y][self.position_x] = self
        mer.grille[shark_pos_y][shark_pos_x] = None
        self.energy += 3
            
    
    def vivre_une_journée(self, monde):
        ex_pos_x = self.position_x
        ex_pos_y = self.position_y
        if self.energy== 0: #énergie de vie du requin
            monde.grille[ex_pos_x][ex_pos_y] = None
        elif len(self.poissons_adjacents(monde))>0:
            self.eat(monde)
            #a continuer avec correction
        elif len(Animal.case_adjacente_libre(monde))>0:
            Animal.move(monde)
            self.energy -= 1 
            self.chronon_to_breed += 1
        #si besoin ajouter compteur


    def breed(self):
        if self.chronon_to_breed %9 == 0: 
            ex_pos_x = self.position_x
            ex_pos_y = self.position_y
            new_position = choice(self.case_adjacente_libre(mer))
            self.position_x = new_position[0]
            self.position_y = new_position[1]
            mer.grille[self.position_y][self.position_x] = self
            mer.grille[ex_pos_y][ex_pos_x] = Requin(ex_pos_y, ex_pos_x)
        
        


    



mer= World(15, 45)
mer.peupler(15, 100)

while True:
#tant qu'il y a encore des requins et des cases vides:
    
    mer.passer_un_jour()
    mer.afficher_world()
    sleep(0.6)
    os.system("clear")
    if len(Animal.case_adjacente_libre) > 0:
        Animal.move()
    if len(Requin.poissons_adjacents) > 0:
        Requin.eat()









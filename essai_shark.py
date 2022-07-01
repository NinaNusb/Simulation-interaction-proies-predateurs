from random import randint
from random import choice
from tkinter import * 
from pip import main
from pkg_resources import Requirement
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
            while self.grille[position_y][position_x] is not None: #pourquoi pas juste NONE ??
                position_x = randint(0, self.largeur_x -1)
                position_y = randint(0, self.hauteur_y -1)
            self.grille[position_y][position_x] = Fish(position_x, position_y) 
        for _ in range(pop_shark):
            position_x = randint(0,self.largeur_x -1)
            position_y = randint(0, self.hauteur_y -1)
            while self.grille[position_y][position_x] is not None:
                position_x = randint(0, self.largeur_x -1)
                position_y = randint(0, self.hauteur_y -1)
            self.grille[position_y][position_x] = Requin(position_x, position_y)
        

    def passer_un_jour(self, monde): #A TESTER
        un_jour = 1
        for ligne in monde.grille:
            for case in ligne:
                #while isinstance(case, Animal) in self.grille:
                while case == None :  #ou '0' 
                    monde.afficher_world()
                else:
                    None 
        un_jour += 1
                    
    def passer_un_tour(self):
        for ligne in self.grille:
            for case in ligne:
                if isinstance(case, Fish):
                    case.vivre_une_journée(self)
                        
    #def chronon_to_breed 
          

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


    def vivre_un_jour(self,monde):
        for ligne in monde.grille:
            for case in ligne:
                if isinstance(case, Animal): 
                    if self.breed == True: #si Animal a suffisamment de chronons (=3) alors appeler méthode breed sur Animal. 
                        self.breed() 
                    elif self.move == True: # si non, si cases adjacentes à Animal vides alors appeler méthode move sur Animal
                        self.move()
                    else: # si non, ANimal ne bouge pas / reste sur place
                        None
        self.chronon_to_breed += 1 #A TESTER

    def vivre_une_journée(self, monde):
        ex_pos_x = self.position_x
        ex_pos_y = self.position_y
        self.chronon_to_breed += 1
        deplacement_effectue = True #à verifier
        if len(self.case_adjacente_libre(monde)) > 0:
            self.se_deplacer(monde)
            deplacement_effectue = False #à verifier
        if self.chronon_to_breed > 3 and deplacement_effectue: #reproduction
            monde.grille[ex_pos_x][ex_pos_y] = Requin(ex_pos_x, ex_pos_y)
            self.chronon_to_breed = 0

   
    """def mort (self,monde):
        if case.fish == case.requin:
            self.destroy()"""
        
class Fish(Animal):
    pass
    """def __init__(self, position_x, position_y):
        super().__init__(position_x, position_y)"""

class Requin(Animal):
    def __init__(self, position_x, position_y):
        super().__init__(position_x, position_y)
        self.energy = 7


    def case_adjacente_occupée(self, monde): #A TESTER
        coup_possible = []
        
        if type(monde.grille[(self.position_y+1) % monde.hauteur_y][self.position_x]) == Fish:
            coup_possible.append((self.position_x, (self.position_y +1) % monde.hauteur_y))

        if type(monde.grille[(self.position_y-1)% monde.hauteur_y][self.position_x]) == Fish:
            coup_possible.append((self.position_x, (self.position_y -1) % monde.hauteur_y))

        if type(monde.grille[self.position_y][(self.position_x+1) % monde.largeur_x]) == Fish:
            coup_possible.append(((self.position_x+1) % monde.largeur_x, self.position_y))

        if type(monde.grille[self.position_y][(self.position_x-1) % monde.largeur_x]) == Fish:
            coup_possible.append(((self.position_x-1) % monde.largeur_x, self.position_y))
        return(coup_possible)
    
    

    def move(self, mer): #A TESTER
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
        print(self.energy)
            
    
    def vivre_une_journée(self, monde):
        ex_pos_x = self.position_x
        ex_pos_y = self.position_y
        a_mange = False
        deplacement_effectue = False
        self.chronon_to_breed += 1
        if len(self.case_adjacente_occupée(monde)):
            self.move
            #a continuer avec correction
        new_position = choice(self.case_adjacente_libre(mer))
        self.position_x = new_position[0]
        self.position_y = new_position[1]
        mer.grille[self.position_y][self.position_x] = self
        mer.grille[ex_pos_y][ex_pos_x] = None
        self.energy -= 1 
        print(self.energy)


    def breed(self):
        if self.chronon_to_breed %9 == 0: 
            ex_pos_x = self.position_x
            ex_pos_y = self.position_y
            new_position = choice(self.case_adjacente_libre(mer))
            self.position_x = new_position[0]
            self.position_y = new_position[1]
            mer.grille[self.position_y][self.position_x] = self
            mer.grille[ex_pos_y][ex_pos_x] = Requin(ex_pos_y, ex_pos_x)
        #return True #à remettre?
        


    

 


mer.afficher_world()

print('-----------------------------------')
Fish.chronon_to_breed = 2


for ligne in mer.grille:
    for case in ligne:
        if isinstance(case, Fish):
            case.breed()

mer.afficher_world()
print('---------------------------------------------------------------')


"""dans le main on va afficher monde et passer un jour """

#tant qu'il y a encore des requins et des cases vides:

mer= World(5, 5)
mer.peupler(2, 1)

while True:
    mer.passer_un_tour()
    mer.afficher_monde()
    sleep(0.2)
    os.system("clear")








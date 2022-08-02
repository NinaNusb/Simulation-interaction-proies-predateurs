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
        self.grille = [[None for _ in range(int(largeur_x))] for _ in range(int(hauteur_y))]
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
        coup_possible = Animal.case_adjacente_libre(self,mer)
        if len(coup_possible) > 0:
            ex_pos_x = self.position_x
            ex_pos_y = self.position_y
            new_position = coup_possible[randint(0, len(coup_possible)-1)]
            self.position_x, self.position_y = new_position
            mer.grille[self.position_y][self.position_x] = self
            mer.grille[ex_pos_y][ex_pos_x] = None


   
    """def mort (self,monde):
        if case.fish == case.requin:
            self.destroy()"""
        
class Fish(Animal):
    compteur = 0
    def __init__(self, position_x, position_y):
        super().__init__(position_x, position_y)
        Fish.compteur +=1 

    def __del__(self):
        Fish.compteur -= 1


    def breed(self, mer, ex_pos_x, ex_pos_y):
        if self.chronon_to_breed %3 == 0:
            Fish.move(self,mer)
            ex_pos_x, ex_pos_y = self.position_x, self.position_y
            new_position = choice(self.case_adjacente_libre(mer))
            self.position_x, self.position_y = new_position
            mer.grille[self.position_y][self.position_x] = self 
            mer.grille[ex_pos_y][ex_pos_x] = Fish(ex_pos_y, ex_pos_x)
            Fish.compteur +=1 

    def vivre_un_jour(self, monde):
        ex_pos_x, ex_pos_y = self.position_x, self.position_y
        if len(self.case_adjacente_libre(monde)) >= 1:
            self.move(monde)
        if self.chronon_to_breed %3 == 0: 
            self.breed(monde, ex_pos_x, ex_pos_y) 
        else: 
            self.move(monde) #PAS SUR INCHALLAH CA MARCHE
        self.chronon_to_breed += 1 #A TESTER


class Requin(Animal):
    compteur = 0 
    def __init__(self, position_x, position_y):
        super().__init__(position_x, position_y)
        self.energy = 7
        Requin.compteur += 1

    def __del__(self):
        Requin.compteur -= 1

    def case_adjacente_occupée(self, monde): #A TESTER
        cases_proies = []
        
        if type(monde.grille[self.position_y+1]  [self.position_x]) is Fish:
            cases_proies.append (((self.position_y +1) % monde.hauteur_y , (self.position_x)))

        if type(monde.grille [self.position_y-1]  [self.position_x]) is Fish:
            cases_proies.append (((self.position_y -1) % monde.hauteur_y , (self.position_x)))

        if type(monde.grille [self.position_y] [self.position_x+1] ) is Fish:
            cases_proies.append (((self.position_y) , (self.position_x+1) % monde.largeur_x))

        if type(monde.grille [self.position_y][self.position_x-1] ) is Fish:
            cases_proies.append(((self.position_y) , (self.position_x-1) % monde.largeur_x ))
        return cases_proies
    

    def move(self, monde): #A TESTER
        #le requin regarde les 4 position adjacentes et si il ya un poisson il le tue
        #food = self.case_adjacente_occupée 
        #if food == True:..00
        cases_proies = Requin.case_adjacente_occupée(self, monde)
        if len(cases_proies) > 0:
            ex_pos_x, ex_pos_y = self.position_x, self.position_y
            new_position = choice(self.case_adjacente_occupée(monde))
            self.position_x, self.position_y = new_position
            Fish.position_x = None
            Fish.position_y  = None
            Fish.compteur -= 1
            mer.grille[self.position_y][self.position_x] = self
            mer.grille[ex_pos_y][ex_pos_x] = None
            self.energy += 4
            # print(self.energy)
            
        else:
            ex_pos_x, ex_pos_y = self.position_x, self.position_y
            coup_possible = Animal.case_adjacente_libre(self,mer)
            new_position = coup_possible[randint(0, len(coup_possible)-1)]
            self.position_x, self.position_y = new_position
            mer.grille[self.position_y][self.position_x] = self
            mer.grille[ex_pos_y][ex_pos_x] = None
            self.energy -= 1 
            #print(self.energy)


    def breed(self):
        if self.chronon_to_breed %9 == 0: 
            ex_pos_x, ex_pos_y = self.position_x, self.position_y
            Requin.move(self,mer)
            ex_pos_x, ex_pos_y = self.position_x, self.position_y
            new_position = choice(self.case_adjacente_libre(mer)) 
            self.position_x, self.position_y = new_position
            mer.grille[self.position_y][self.position_x] = self 
            mer.grille[ex_pos_y][ex_pos_x] = Requin(ex_pos_y, ex_pos_x)
            Requin.compteur +=1 
        #return True #à remettre?
        


    

 
mer= World(10, 10)


mer.peupler(30, 15)

mer.afficher_world()

print('-----------------------------------')
Requin.chronon_to_breed = 9


for ligne in mer.grille:
    for case in ligne:
        if isinstance(case, Requin):
            case.move(mer)

mer.afficher_world()
print('---------------------------------------------------------------')


"""dans le main on va afficher monde et passer un jour """

#tant qu'il y a encore des requins et des cases vides:








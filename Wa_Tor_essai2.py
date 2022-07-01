from random import randint
from random import choice
from tkinter import * 
from pip import main


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
                if isinstance(case, Animal): 
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
            self.grille[position_y][position_x] = Animal(position_x, position_y) 
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
        ex_pos_x = self.position_x
        ex_pos_y = self.position_y
        new_position = choice(self.case_adjacente_libre(mer))
        self.position_x = new_position[0]
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

   
    """def mort (self,monde):
        if case.fish == case.requin:
            self.destroy()"""
        


class Requin(Animal):
    def __init__(self, position_x, position_y):
        super().__init__(position_x, position_y)
        self.energy = 7


    def case_adjacente_occupée(self, monde): #A TESTER
        coup_possible = []
        if monde.grille[(self.position_y+1) % monde.hauteur_y][self.position_x] == ' 1 ':
            coup_possible.append((self.position_x, (self.position_y +1) % monde.hauteur_y))
        if monde.grille[(self.position_y-1)% monde.hauteur_y][self.position_x] == ' 1 ':
            coup_possible.append((self.position_x, (self.position_y -1) % monde.hauteur_y))
        if monde.grille[self.position_y][(self.position_x+1) % monde.largeur_x] == ' 1 ':
            coup_possible.append(((self.position_x+1) % monde.largeur_x, self.position_y))
        if monde.grille[self.position_y][(self.position_x-1) % monde.largeur_x] == ' 1 ':
            coup_possible.append(((self.position_x-1) % monde.largeur_x, self.position_y))
        return(coup_possible)

    def move(self, mer): 
        #le requin regarde les 4 position adjacentes et si il ya un poisson il le tue
        for ligne in mer.grille:
            for case in ligne: 
                food = self.case_adjacente_occupée 
                if food is True:
                    shark_pos_x = self.position_x                           #Animal.position_x = 0 // Animal.position_y = 0
                    shark_pos_y = self.position_y
                    fish_position = choice(self.case_adjacente_occupée(mer))
                    self.position_x = fish_position[0]
                    self.position_y = fish_position[1]
                    mer.grille[self.position_y][self.position_x] = self
                    mer.grille[shark_pos_y][shark_pos_x] = None
                    self.energy += 3
                else:
                    ex_pos_x = self.position_x
                    ex_pos_y = self.position_y
                    new_position = choice(self.case_adjacente_libre(mer))
                    self.position_x = new_position[0]
                    self.position_y = new_position[1]
                    mer.grille[self.position_y][self.position_x] = self
                    mer.grille[ex_pos_y][ex_pos_x] = None
                    self.energy -= 1 



    def breed(self):
        if self.chronon_to_breed %9 == 0: #A TESTER
            ex_pos_x = self.position_x
            ex_pos_y = self.position_y
            new_position = choice(self.case_adjacente_libre(mer))
            self.position_x = new_position[0]
            self.position_y = new_position[1]
            mer.grille[self.position_y][self.position_x] = self
            mer.grille[ex_pos_y][ex_pos_x] = Animal(ex_pos_y, ex_pos_x)
        return True 
        


    

main 
mer= World(10, 5)
mer.peupler(4)


mer.afficher_world()
print('-----------------------------------')

for ligne in mer.grille:
    for case in ligne:
        if isinstance(case, Animal):
            case.move(mer)

mer.afficher_world()
print('---------------------------------------------------------------')


"""dans le main on va afficher monde et passer un jour """

#tant qu'il y a encore des requins et des cases vides:






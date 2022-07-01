from random import randint
import random


class World:
    def __init__(self, largeur_x, hauteur_y):
        self.grille = [[None for _ in range(int(largeur_x))] for _ in range(int(hauteur_y))]
        self.largeur_x = largeur_x
        self.hauteur_y = hauteur_y

    def afficher_world(self): 
        for ligne in self.grille:
            str_ligne = ''
            for case in ligne:
                if isinstance(case, Animal): #Animal à remplacer par Fish ou Shark
                    str_ligne += ' 1 '
                else:
                    str_ligne += ' 0 '
            print(str_ligne)

    def peupler(self, pop_fish, pop_shark): #ajouter pop_shark
        for _ in range(pop_fish):
            position_x = randint(0,self.largeur_x -1)
            position_y = randint(0, self.hauteur_y -1)
            while self.grille[position_y][position_x] is not None:
                position_x = randint(0, self.largeur_x -1)
                position_y = randint(0, self.hauteur_y -1)
            self.grille[position_y][position_x] = Animal(position_x, position_y) #pour chaque sous-classe

        
grille= World(10, 5)
grille.afficher_world()
    
 
    
    def passer_un_jour

    
    def chronon_to_breed 
    += 1
    

class Animal:
    #type = rect(50, 250, 55, 55) #taille et couleur
    nb_animal = 100
    taille = rect(50, 250, 55, 55)
    def __init__(self, position_x, position_y): #tout ce qui se passe à la création d'un animal #param car au moment de l'appel ce sont les choses qui peuvent changer
        self.position_x = position_x #placer 1 animal par case de façon random
        self.position_y = position_y
        self.chronon_to_breed = 0 #unité en chronons

    def renvoyer_cases_adjacentes_libres(self, world):

         
    def move(self, grille, animal, case):
        case = "position_y" and "position_x"
        if case == None:
            case += (random("position_x" or "position_y")) + 1 #ajouter directions (N, S, E, O)
            
    def breed(self, chronon_to_breed, move, animal):
        self.chronon_to_breed = 0
        Animal_0 = Animal #préciser diff père fils
        return (Animal(self.couleur, Animal_0.position_x, Animal_0.position_y))
        
    def vivre_un_jour(self, world):
        if self.chronon_to_breed = 3 alors se reproduit
        sinon se deplace 
        sinon None 

    def mort(self)
        
class Fish(Animal):
    def mort(self, grille, animal):
        self.grille = grille
        self.animal = animal

    if lifetime == 3:
        fish_père = Animal
        fish_père.breed(0, case, fish) # appeler méthode breed() sur fish_père 

class Shark(Animal):
    def __init__(self, position_x, position_y, chronon_to_breed):
        super().__init__(position_x, position_y, chronon_to_breed)
        self.energy = 7
    déplacement_shark = Animal.move() + energy -= 1 
    déplacement_shark = False 

    def vivre_un_jour(self, world): #reprendre code + spécificité
        

    def feed_Shark(self, energy, position, case_adjacente):
        self.energy = (energy -= 1)
        self.position = position 
        self.case_adjacente = case_adjacente

    def Fish_adjacent(self):    
        if case_adjacente == Fish:
            #déplacement_shark = (Shark.position_x += Fish.position_x) and (Shark.position_y += Fish.position_y) 
            Shark = Fish 
            nb_fish -= 1
            Shark.energy += 6 #énergie suite à l'absorption d'un Fish
        else:
            return True  #perte d'énergie à chaque tour 
    




def setup():

mer = []

var = Animal("red", 5)
var.move(

    
def draw(): #boucles
    

            
 
    
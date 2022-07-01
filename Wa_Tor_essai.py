from random import randint
from random import choice


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

    def peupler(self, pop_fish): #ajouter pop_shark
        for _ in range(pop_fish):
            position_x = randint(0,self.largeur_x -1)
            position_y = randint(0, self.hauteur_y -1)
            while self.grille[position_y][position_x] is not None:
                position_x = randint(0, self.largeur_x -1)
                position_y = randint(0, self.hauteur_y -1)
            self.grille[position_y][position_x] = Animal(position_x, position_y) #pour chaque sous-classe
        
    
    def passer_un_jour(self, monde):
        for ligne in monde.grille:
            for case in ligne:
                if isinstance(case, Animal): 
                    pass #à modifier

    #def chronon_to_breed 
    # += 1      

 
class Animal:
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
        print(coup_possible)           
        return(coup_possible)

    def move(self, monde):
        ex_pos_x = self.position_x
        ex_pos_y = self.position_y
        new_position = choice(self.case_adjacente_libre(mer))
        self.position_x = new_position[0]
        self.position_y = new_position[1]
        mer.grille[self.position_y][self.position_x] = self
        mer.grille[ex_pos_y][ex_pos_x] = None

    def breed(self, monde):
        ex_pos_x = self.position_x
        ex_pos_y = self.position_y
        new_position = choice(self.case_adjacente_libre(mer))
        self.position_x = new_position[0]
        self.position_y = new_position[1]
        mer.grille[self.position_y][self.position_x] = self
        mer.grille[ex_pos_y][ex_pos_x] = Animal(ex_pos_y, ex_pos_x)

    def vivre_un_jour(self, monde):
        if self.chronon_to_breed %3 == 0:
            self.breed(monde) 
        else:
            self.move(monde)
        self.chronon_to_breed += 1


#Fish = Animal(3,4)

mer= World(10, 5)
mer.peupler(4)
mer.afficher_world()

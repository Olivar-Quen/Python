import random 
import os
import time


#Définition des 3 règles 

def calcul() :
    temp = [row[:] for row in state]
    for x in range(largeur):
	    for y in range(hauteur):
		    nb_voisins = calcul_voisins(x, y)

            # Règle 1 : cellule vivante et a moins de 2 voisins en vie, elle meurt
            if state[y][x] == 1 and nb_voisins < 2:
                temp[y][x] = 0

            # Règle 2 : Toute cellule avec 2 ou 3 voisins vivant survit
            elif state[y][x] == 1 and (nb_voisins == 2 or nb_voisins == 3):
                temp[y][x] = 1

            # Règle 3 : Plus de 3 voisins, alors meurt
            elif state[y][x] == 1 and nb_voisins > 3:
                temp[y][x] = 0

            # Règle 4 : Si une cellule morte a exactement 3 voisins vivants, elle naît
            elif state[y][x] == 0 and nb_voisins == 3:
                temp[y][x] = 1

    return temp  # Retourne la nouvelle grille
    
def calcul_voisins(x,y) : 
        nb_voisins = 0 

        #Diag Haut Gauche 
        if state[(x-1)%largeur][(y+1)%hauteur] == 1 :
            nb_voisins += 1


        #Haut
        if state[x][(y+1)%hauteur] == 1 :
            nb_voisins += 1


        #Diag Haut Droite 
        if state[(x+1)%largeur][(y+1)%hauteur] == 1 :
            nb_voisins += 1


        #Gauche 
        if state[(x-1)%largeur][y] == 1 :
            nb_voisins += 1


        #Droite 
        if state[(x+1)%largeur][y] == 1 :
            nb_voisins += 1


        #Bas Gauche 
        if state[(x-1)%largeur][(y-1)%hauteur] == 1 :
            nb_voisins += 1


        #Bas 
        if state[x][(y-1)%hauteur] == 1 :
            nb_voisins += 1


        #Bas Droite 
        if state[(x+1)%largeur][(y-1)%hauteur] == 1 :
            nb_voisins += 1



        return nb_voisins  # On récupère le nombre de voisins 




#-----Programme Principal----

#Définition des variables 

largeur = int(input("Nombre de lignes : ")) # Pour parcourir les lignes on utilise la lettre i
hauteur = int(input("Nombre de colonnes: "))# Pour parcourir les colonnes on utilise la lettre j
vivant = 1 
mort = 0 


#Préparation des matrices 

state = [[random.choice([0 , 1]) for row in range(hauteur)] for col in range(largeur)]




# Boucle d'évolution du jeu
while True:
    os.system("cls" if os.name == "nt" else "clear")  # Efface l'écran
    for row in state:
        print(" ".join(map(str, row)))  # Affiche la grille
    time.sleep(0.5)  # Pause pour voir l'évolution
    state = calcul()  # Mettre à jour la grille







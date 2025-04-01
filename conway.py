import random 
import os
import time

rows = ""
cols = ""


#Définition des 3 règles 

def calcul() :
    temp = [row [:] for row in state] 
    for x in range(rows) :
        for y in range (cols) :
            nombre_voisins = calcul_voisins(x,y)   
        
        # Règle 1 : Si une cellule a exactement 3 voisines vivantes alors elle devient vivante 
        if state [x][y] == 0 and nombre_voisins == 3 :
            temp [x][y] = 1 

        # Règle 2 : Si une cellule a exactement 2 voisines vivantes, elle reste dans son état actuel à l'étape suivante 
        if state [x][y] == 1 and nombre_voisins == 2 : 
            temp [x][y] = 1
        
        # Règle 3 : Si une cellule a strictement moins de deux ou strictement plus de trois voisins vivante, elle meurt 
        if state [x][y] == 1 and nombre_voisins < 2 or nombre_voisins > 2 : 
            temp [x][y] = 0 

        #Règle 4 : Si une cellule a plus de 3 voisins vivants, alors elle meurt  

        if state [x][y] == 1 and nombre_voisins > 3 : 
            temp [x][y] = 0

   
    return temp # Prend la valeur de la variable temporaire 


def calcul_voisins(x,y) : 
    nombre_voisins = 0


    #Diagonale Haut - Gauche 

    if state [(x-1)%rows][(y+1)%cols] : 
        nombre_voisins +=1 

    #Haut  

    if state [x][(y+1)%cols] : 
        nombre_voisins +=1 

    #Diagonale Haut - Droite

    if state [(x+1)%rows][(y+1)%cols] : 
        nombre_voisins +=1 


   #Gauche 

    if state [(x-1)%rows][y] : 
        nombre_voisins +=1 

    
    #Droite

    if state [(x+1)%rows][y] : 
        nombre_voisins +=1 

    
    #Diagonale Bas - Gauche 

    if state [(x-1)%rows][(y-1)%cols] : 
        nombre_voisins +=1 


   #Bas

    if state [x][(y-1)%cols] : 
        nombre_voisins +=1 


    #Diagonale Bas - Droite 

    if state [(x+1)%rows][(y-1)%cols] : 
        nombre_voisins +=1 


    return nombre_voisins # Récupération de la valeur de la variable 


#-----Programme Principal----

#Définition des variables 

rows = int(input("Insérez le nombre de lignes :"))
cols = int(input("Insérez le nombre de colonnes :"))



#Préparation des matrices 

state = [[random.choice([0 , 1]) for row in range(cols)] for col in range(rows)]
temp = [[0 for row in range(cols)] for col in range(rows)]


calcul()  # Mise à jour de la grille

for row in state:
        print(" ".join(map(str, row)))  # Affichage de la grille








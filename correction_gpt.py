import random
import os
import time

# Définition des règles du Jeu de la Vie

def calcul():
    global state
    temp = [row[:] for row in state]  # Copie indépendante de l'état actuel

    for y in range(rows):
        for x in range(cols):
            nb_voisins = calcul_voisins(x, y)

            # Règle 1 : Moins de 2 voisins vivants -> Meurt
            if state[x][y] == 1 and nb_voisins < 2:
                temp[x][y] = 0
            
            # Règle 2 : 2 ou 3 voisins vivants -> Survit
            elif state[x][y] == 1 and (nb_voisins == 2 or nb_voisins == 3):
                temp[x][y] = 1 
            
            # Règle 3 : Plus de 3 voisins -> Meurt
            elif state[x][y] == 1 and nb_voisins > 3:
                temp[x][y] = 0
            
            # Règle 4 : Cellule morte avec 3 voisins vivants -> Naît
            elif state[x][y] == 0 and nb_voisins == 3:
                temp[x][y] = 1 

    state = temp  # Met à jour l'état général

def calcul_voisins(x, y):
    nb_voisins = 0

    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue  # Ignore la cellule elle-même
            
            voisin_x = (x + dx) % cols
            voisin_y = (y + dy) % rows

            if state[voisin_y][voisin_x] == 1:
                nb_voisins += 1

    return nb_voisins


# ----- Programme Principal -----
rows = int(input("Nombre de lignes : "))
cols = int(input("Nombre de colonnes: "))

# Création de la grille de départ
state = [[random.choice([0, 1]) for _ in range(cols)] for _ in range(rows)]

# Boucle principale du jeu
while True:
    os.system("cls" if os.name == "nt" else "clear")  # Efface l'écran
    
    for row in state:
        print(" ".join(map(str, row)))  # Affiche la grille
    
    time.sleep(0.5)  # Pause pour voir l'évolution
    
    calcul()  # Met à jour la grille

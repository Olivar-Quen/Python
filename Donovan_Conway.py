

import random
import os
import time

# Code ANSI pour le vert
VERT = "\033[33m"
RESET = "\033[0m"

def cycle(matrice):
    lignes = len(matrice)
    colonnes = len(matrice[0])
    nouvelle_matrice = [[0 for _ in range(colonnes)] for _ in range(lignes)]

    def compter_voisins_vivants(x, y):
        total = 0
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if (i == x and j == y) or i < 0 or j < 0 or i >= lignes or j >= colonnes:
                    continue
                total += matrice[i][j]
        return total

    for i in range(lignes):
        for j in range(colonnes):
            voisins = compter_voisins_vivants(i, j)
            if matrice[i][j] == 1:
                nouvelle_matrice[i][j] = 1 if voisins in [2, 3] else 0
            else:
                nouvelle_matrice[i][j] = 1 if voisins == 3 else 0

    return nouvelle_matrice

def printmatrice(m):
    for row in m:
        line = ""
        for item in row:
            if item == 1:
                line += VERT + "1 " + RESET
            else:
                line += "0 "
        print(line)

# Entrée utilisateur
lar = int(input("Largeur : "))
lon = int(input("Longueur : "))
matrice = [[random.randint(0, 1) for _ in range(lon)] for _ in range(lar)]
nbc = int(input("Nombre de cycles : "))

# Boucle principale
for x in range(nbc):
    os.system('cls' if os.name == 'nt' else 'clear')  # Efface l'écran
    print(f"Cycle {x + 1}/{nbc}")
    printmatrice(matrice)
    matrice = cycle(matrice)
    time.sleep(0.3)





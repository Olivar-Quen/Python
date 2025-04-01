
import random
import os
import time

class matrices:
    lignes = 0
    colonnes = 0
    matrice = []
    VERT = "\033[33m"
    RESET = "\033[0m"
    
    def __init__(self, ligne , colonne):
        self.lignes = ligne
        self.colonnes = colonne
        self.matrice = [[random.randint(0, 1) for _ in range(ligne)] for _ in range(colonne)]
        
    def compter_voisins_vivants(self, x, y):
        total = 0
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if (i == x and j == y) or i < 0 or j < 0 or i >= self.lignes or j >= self.colonnes:
                    continue
                total += self.matrice[i][j]
        return total

    def cycle(self):
        mt = [[0 for _ in range(self.colonnes)] for _ in range(self.lignes)]
        for i in range(self.lignes):
            for j in range(self.colonnes):
                voisins = self.compter_voisins_vivants(i, j)
                if self.matrice[i][j] == 1:
                    mt[i][j] = 1 if voisins in [2, 3] else 0
                else:
                    mt[i][j] = 1 if voisins == 3 else 0

        self.matrice = mt
    def printmatrice(self):
        for row in self.matrice:
            line = ""
            for item in row:
                if item == 1:
                    line += self.VERT + "1 " + self.RESET
                else:
                    line += "0 "
            print(line)
lar = int(input("Largeur : "))
lon = int(input("Longueur : "))
nbc = int(input("Nombre de cycles : "))
matrice = matrices(lar,lon)
# Boucle principale
for x in range(nbc):
    os.system('cls' if os.name == 'nt' else 'clear')  # Efface l'écran
    print(f"Cycle {x + 1}/{nbc}")
    matrice.cycle()
    matrice.printmatrice()
    time.sleep(0.3)


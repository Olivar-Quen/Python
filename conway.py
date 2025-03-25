import random 

rows = ""
cols = ""

rows = int(input("Nombre de lignes : ")) # Pour parcourir les lignes on utilise la lettre i
cols = int(input("Nombre de colonnes: "))# Pour parcourir les colonnes on utilise la lettre j


grid = [[random.choice([0 , 1]) for _ in range(cols)] for _ in range(rows)]

for row in grid :
    print(row)

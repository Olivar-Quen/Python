import random 

rows = ""
cols = ""

rows = int(input("Nombre de lignes : "))
cols = int(input("Nombre de colonnes: "))


grid = [[random.choice([0 , 1]) for _ in range(cols)] for _ in range(rows)]

for row in grid :
    print(row)

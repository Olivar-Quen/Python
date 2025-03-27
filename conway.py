import random 

rows = ""
cols = ""



#Initialisation suivant les données rentrées par l'utilisateur 

rows = int(input("Nombre de lignes : ")) # Pour parcourir les lignes on utilise la lettre i
cols = int(input("Nombre de colonnes: "))# Pour parcourir les colonnes on utilise la lettre j


state = [[random.choice([0 , 1]) for x in range(cols)] for y in range(rows)]
temp[x][y] = 0



#Définition des 3 règles 

def calcul 
	for x range(cols)
		for y range(rows)
			nb_voisins = calcul_voisins(x,y) 

			#règle 1 : cellule a strictement 3 cellules vivantes, elle reste en vie

			if nb_voisins == 3 

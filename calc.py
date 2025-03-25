A = ""
B = ""
operateur = ""
resultat = ""
op = ["+","-","*","/"] 


while not ( A.isnumeric()) :
	A = input("Nombre 1 :") 
	pass 

while not operateur in op :
	operateur = input("Opérateur :")
	pass
			
while not ( B.isnumeric()) :

	B = input("Nombre 2 :") 
	pass 

A = int(A)
B = int(B)

if operateur == "+" : 
	resultat = A + B 

elif operateur == "-" :
	resultat = A - B 

elif operateur == "*" : 
	resultat = A * B 

elif operateur == "/" :
	if B != 0:
		resultat = A / B
	else :
		resultat = "Erreur : Division par zéro"

print (f"Le resultat de {A} {operateur} {B} est {resultat}")

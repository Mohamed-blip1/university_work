#  * Exercice B – Sommation
#  * Auteur: Mohamed Bouharti
#  * Université Chouaib Doukkali – IA
#  * Semestre 1 – 2025/2026

#  Question:
#  -Écrire un programme en Python qui permet de lire un entier N strictement positif,
#  puis calcule et affiche la somme S suivante : $S = 1^2+2^2+3^3+....+N^N$. 
#  (si l'utilisateur donne par exemple pour N la valeur 3 le programme affiche : S=32).


S=0
N = int(input("Entre un entier N strictement positive: "))

while N<=0:
    N = int(input("Entre un entier N strictement positive: "))

for i in range(0,N):
    S += (i+1)**(i+1) # S = S + N**N

print("S = ",S) 
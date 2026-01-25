#  * Exercice F – Tableaux 2D
#  * Auteur: Mohamed Bouharti
#  * Université Chouaib Doukkali – IA
#  * Semestre 1 – 2025/2026

# Question:
# -Ecrire un programme en Python qui permet de saisir deux matrices M et N de taille 3x3
# puis calcule et affiche sur l'écran la matrice G somme de M et N.
# Exemple :
# si M est : 5 3 2     et N est : 2 5 1     alors G est: 7 8 3
#            7 1 5                1 3 3                  8 4 8
#            1 4 2                2 1 5                  3 5 7

M=[[None for i in range(3)] for i in range(3)]
N=[[None for i in range(3)] for i in range(3)]
G=[[None for i in range(3)] for i in range(3)]


print("Entre les element de la matrice M: ")
for i in range(0,3):
    for j in range(0,3):
            M[i][j]=int(input("Entre un number: "))

print("Entre les element de la matrice N: ")
for i in range(0,3):
    for j in range(0,3):
            N[i][j]=int(input("Entre un number: "))

for i in range(0,3):
    for j in range(0,3):
            G[i][j]=M[i][j]+N[i][j]

print("matrice G: ")
for i in range(0,3):
    for j in range(0,3):
        print(G[i][j],end=' ')
    print()
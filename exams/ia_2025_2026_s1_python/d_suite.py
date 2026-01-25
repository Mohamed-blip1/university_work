#  * Exercice D – Suite
#  * Auteur: Mohamed Bouharti
#  * Université Chouaib Doukkali – IA
#  * Semestre 1 – 2025/2026

# Question:
# -Ecrire un programme en Python qui demande à l'utilisateur un entier positif n 
# puis calcule et affiche les termes U_i de la suite définie par :
# U_0=1, U_i=5*U_{i-1} + 2 (pour i allant de 1 à n)
# (Si l'utilisateur donne pour n la valeur 4 Le programme affiche : 1 7 37 187)

U=1
n = int(input("Entre un entier positive :"))

while n<=0:
    n = int(input("Entre un entier positive :"))

for i in range(0,n):
    print(U,end=' ')
    U=5*U+2

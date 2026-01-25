#  * Exercice C – permutation
#  * Auteur: Mohamed Bouharti
#  * Université Chouaib Doukkali – IA
#  * Semestre 1 – 2025/2026

# Question:
# -Écrire un programme en Python qui permet de lire trois entiers x,
# y et z et fait la permutation circulaire de leurs valeurs 
# (mettre la valeur de x dans y, la valeur de y dan z et la valeur de z dans x),
# et affiche à l'écran : leur valeur avant et après permutation.
# (exemple : l'utilisateur donne pour x la valeur 5, 
# pour y la valeur 7 et pour z la valeur 10 et le programme affiche : 
# avant permutation : x=5 y=7 et z=10, après permutation x=10 y=5 et z=7)

x=int(input("Entre un entier x: "))
y=int(input("Entre un entier y: "))
z=int(input("Entre un entier z: "))

print(f"avant permutation: x = {x}, y = {y}, et z = {z}")

tempy = y
y = x

tempz = z
z = tempy

x = tempz


print(f"après permutation: x = {x}, y = {y}, et z = {z}")
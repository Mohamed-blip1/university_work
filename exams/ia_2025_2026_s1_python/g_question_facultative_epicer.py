#  * Exercice G - Question facultative epicer
#  * Auteur: Mohamed Bouharti
#  * Université Chouaib Doukkali – IA
#  * Semestre 1 – 2025/2026

# Question:
# -Écrire un programme en Python qui permet de fournir à un épicier un logiciel qui lui calcule 
# et affiche sur l'écran la somme et la moyenne des produits vendus dans la journée saisis au clavier.

T=[]

somme=0
moyenne=0

while True:
    prix=float(input("Entre un prix ([0] pour arreter): "))

    if prix == 0:
        break

    somme += prix
    T.append(prix)

if len(T)>0:
    moyenne = somme/len(T)
    print(f"La somme = {somme}")
    print(f"La moyenne = {moyenne}")
else:
    print("Aucun produit saisi.")
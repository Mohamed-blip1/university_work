#  * Exercice E – Tableaux 1D
#  * Auteur: Mohamed Bouharti
#  * Université Chouaib Doukkali – IA
#  * Semestre 1 – 2025/2026

# Question:
# -Ecrire un programme en Python qui lit un tableau de 40 notes saisies par l'utilisateur,
# puis classe ces notes par ordre décroissant et 
# enfin affiche sur l'écran les notes classées et devant chaque note la mention : 
# « Très bien » si >= 16, « Bien » si >= 14,
# « Assez bien » si >= 12, « Passable » si >= 10, et «  » si < 10

T=[None for i in range(40)]

for i in range(0,40):
    T[i]=float(input(f"Entre la note nomber '{i+1}' :"))

for i in range(0,39):
    for j in range(i+1,40):
        if T[i]<T[j]:
            temp=T[i]
            T[i]=T[j]
            T[j]=temp

for i in range(0,40):
    if T[i]>=16:
        print(f"{T[i]} : Tres bien.")
    elif T[i]>=14:
        print(f"{T[i]} : bien.")
    elif T[i]>=12:
        print(f"{T[i]} : Assez bien.")
    elif T[i]>=10:
        print(f"{T[i]} : Passable.")
    elif T[i]<10:
        print(f"{T[i]} : Ajourne.")
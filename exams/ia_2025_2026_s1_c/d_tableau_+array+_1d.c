/* Exercice D - Tableau(array) 1D
 * Auteur: Mohamed Bouharti
 * Université Chouaib Doukkali – IA
 * Semestre 1 – 2025/2026
 */

/*
    Question:
    - Ecrire un algorithme qui permet de saisir un tableau T de notes réelles (sur 20) de taille 700. Puis
    calcule la moyenne M des 700 notes et l’écart type E (E = sqrt(Σ{i=1},{i=700} (T[i] - M)^2))
    puis calcule le nombre N de valeurs supérieurs à la moyenne M, et affiche M, E et N.

*/

#include <stdio.h>
#include <stdbool.h>
#include <math.h>

int main()
{

    float T[700];
    float moyenne = 0;
    float E = 0;
    int N = 0;

    // Saisie des notes
    for (int i = 0; i < 700; i++)
    {
        printf("Entre une note (sur 20): ");
        scanf("%f", &T[i]);
    }

    // Calcul de la moyenne
    for (int i = 0; i < 700; i++)
    {
        moyenne = moyenne + T[i];
    }
    moyenne = moyenne / 700;

    // Calcul de l’écart type
    for (int i = 0; i < 700; i++)
    {
        E = E + pow((T[i] - moyenne), 2);
    }
    E = sqrt(E);

    // Comptage des valeurs supérieures à la moyenne
    for (int i = 0; i < 700; i++)
    {
        if (T[i] > moyenne)
        {
            N += 1; // N = N+1
        }
    }

    printf("M = %.2f\n", moyenne);
    printf("E = %.2f\n", E);
    printf("N = %d\n", N);

    return 0;
}
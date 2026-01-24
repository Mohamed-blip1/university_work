/* Exercice E - Tableau(array) 2D
 * Auteur: Mohamed Bouharti
 * Université Chouaib Doukkali – IA
 * Semestre 1 – 2025/2026
 */

/*
    Question:
    - Ecrire un algorithme qui permet de saisir un tableau de taille 128x128 de valeurs réels et l’affiche.
    Puis calcule et affiche le nombre N des valeurs de ce tableau qui ont la même partie entières.
*/

#include <stdio.h>
#include <stdbool.h>

int main()
{
    float T[128][128];
    int N = 0;

    // Input
    for (int i = 0; i < 128; i++)
    {
        for (int j = 0; j < 128; j++)
        {
            printf("Entre un nombre reel: ");
            scanf("%f", &T[i][j]);
        }
    }

    // Affiche le tableau
    for (int i = 0; i < 128; i++)
    {
        for (int j = 0; j < 128; j++)
        {
            printf("%.2f ", T[i][j]);
        }
        printf("\n");
    }

    for (int i = 0; i < 128; i++)
    {
        for (int j = 0; j < 128; j++)
        {
            int elem = (int)T[i][j];
            int count = 0;

            for (int x = 0; x < 128; x++)
            {
                for (int y = 0; y < 128; y++)
                {
                    if (elem == (int)T[x][y])
                    {
                        count++;
                    }
                }
            }

            if (count > 1)
            {
                N++;
            }
        }
    }

    printf("N = %d\n", N);

    return 0;
}
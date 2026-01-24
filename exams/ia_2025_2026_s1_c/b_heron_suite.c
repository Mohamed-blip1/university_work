/* Exercice B – Heron suite
 * Auteur: Mohamed Bouharti
 * Université Chouaib Doukkali – IA
 * Semestre 1 – 2025/2026
 */

/*
    Question:
    -On souhaite calculer le terme n de la suite récursive de Héron suivante :
    S_0 = 1 , S_n = (S_{n-1} + (A / S_{n-1}))/2
    A est un entier positif non nul donné par l’utilisateur du programme.
*/

#include <stdio.h>
#include <stdbool.h>

int main()
{
    int n, A;
    float S = 1;

    // Input n >= 0
    do
    {
        printf("Entre n (nombre de trerms): ");
        scanf("%d", &n);
    } while (n < 0);

    // Input A > 0
    do
    {
        printf("Entre A (entier positive): ");
        scanf("%d", &A);

    } while (A <= 0);

    printf("S0 = %.2f\n", S);

    for (int i = 0; i < n; i++)
    {
        // Heron formula
        S = (S + ((float)A / S)) / 2;

        printf("S%d = %.2f\n", i + 1, S);
    }
    return 0;
}
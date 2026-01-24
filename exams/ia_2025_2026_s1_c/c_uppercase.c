/* Exercice C - Uppercase
 * Auteur: Mohamed Bouharti
 * Université Chouaib Doukkali – IA
 * Semestre 1 – 2025/2026
 */

/*
    Question:
    - Ecrire un algorithme qui permet de saisir une phrase (sous forme de chaine de caractère
    qui ne dépasse pas 100 caractères),
    puis calcule le nombre N de lettres majuscules contenues dans cette phrase et affiche N.
*/


#include <stdio.h>

int main()
{
    char C[100];
    int N = 0;

    printf("Entrez une phrase (ne dépasse pas 100 caractères): ");
    // scanf("%s", C);
    fgets(C, 100, stdin); // Lire tout la phrase par les espace

    for (int i = 0; C[i] != '\0'; i++)
    {
        if (C[i] >= 'A' && C[i] <= 'Z')
        {
            N = N + 1; // N += 1 ou N++;
        }
    }

    printf("nombre de Majuscules est : %d\n", N);

    return 0;
}
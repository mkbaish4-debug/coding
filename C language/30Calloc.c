#include <stdio.h>
#include <stdlib.h>

int main() {
    int numbers = 0;
    printf("Enter the number of scores: ");
    scanf("%d", &numbers);
    int *scores = calloc(numbers, sizeof(int));
    if(scores == NULL) {
        printf("Memory allocation failed!");
        return 1;
    }
     for(int i = 0; i < numbers; i++) {
        printf("Enter score no.%d: ", (i + 1));
        scanf("%d", &scores[i]);
    }
     for(int i = 0; i < numbers; i++) {
        printf("Score no.%d: %d\n", (i + 1), scores[i]);
    }
    free(scores);
    scores = NULL;

    return 0;

}
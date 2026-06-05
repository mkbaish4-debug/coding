#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    srand(time(NULL));
    int guess = 0;
    int tries = 0;
    int max = 100;
    int min = 1;
    int randomnum = (rand() % (max - min + 1)) + min;
    printf(" *** NUMBER GUESSING GAME *** \n");
   do {
     printf("Guess a number between 1-100: \n");
    scanf("%d", &guess);
    tries++;
    if (guess < randomnum) {
        printf("TOO LOW!\n");
    } else if (guess > randomnum) {
        printf("TOO HIGH!\n");
    }

   } while (guess != randomnum); 
    printf("CONGRATULATIONS! YOU'RE GUESS IS CORRECT.\n");
        printf("Total number of tries: %d", tries);
    return 0;
    
}
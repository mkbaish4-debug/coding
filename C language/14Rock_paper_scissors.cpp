#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int computer(int randomnum) {
    int max = 3;
    int min = 1;

   randomnum = (rand() % (max - min + 1)) + min;
    return randomnum;
}

int main() {
    srand(time(NULL));
    
    int choice;
     int randomnum;
    int computerchoice;
   do { printf("*** ROCK, PAPER, SCISSORS GAME ***\n");
    printf("Choose an option: \n");
    printf("1.Rock.\n");
    printf("2.Paper.\n");
    printf("3.Scissors.\n");
    printf("Enter your choice: \n");
    scanf("%d", &choice);
   
  
} while (choice < 1 || choice > 3);
   computerchoice = computer(randomnum);
  switch(choice) {
     case 1:
            printf("You choose Rock.\n");
            break;
     case 2:
            printf("You choose Paper.\n");
            break;
     case 3:
            printf("You choose Scissors.\n");
            break;
}

     switch(computerchoice) {
     case 1:
            printf("computer choose Rock.\n");
            break;
     case 2:
            printf("computer choose Paper.\n");
            break;
     case 3:
            printf("computer choose Scissors.\n");
            break;
}  
  
   if (choice == computerchoice) {
    printf("It's a Tie!\n");
    } else if (choice == 1 && computerchoice == 3) {
        printf("You win!\n");
      } else if (choice == 2 && computerchoice == 1) {
        printf("You win!\n");
      } else if (choice == 3 && computerchoice == 2) {
        printf("You win!\n");
} else {
    printf("You Lose!\n");
}
return 0;
}

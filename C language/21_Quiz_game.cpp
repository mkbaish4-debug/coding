#include <stdio.h>
int main() {
    int score = 0;
    int choice = 0;
    char questions[][100] = {"\nWhat is the largest planet in the Solar system?\n1.Earth.\n2.Mars.\n3.Jupiter.\n4.Mercury.\n", 
                             "\nIs earth flat?\n1.No.\n2.Yes.\n3.Maybe.\n4.Sometimes.\n", 
                             "\nAre you human?\n1.No.\n2.Yes.\n3.Maybe.\n4.Sometimes.\n",
                             "\nAre you a lizard?\n1.No.\n2.Yes.\n3.Maybe.\n4.Sometimes.\n"};

    printf("*** QUIZ GAME ***\n");
    for (int i = 0; i < 4; i++) {
        printf("%s", questions[i]);
        printf("Enter your choice: \n");
        scanf("%d", &choice);
        if(i == 0 && choice == 3 || i == 1 && choice == 1 || i == 2 && choice == 2 || i == 3 && choice == 1) {
            printf("Correct!\n");
            score++;
        } else {
            printf("Incorrect!\n");
        }
    } 
    printf("Your score is %d", score);
    return 0;
} 
   /*we can have many array variables and at i = 0 that is at first index will have connectivity 
   to each other cause we can call them at i = 0. also by #include <ctype.h> we have another function
   which is just that it converts lower characters to upper know as toupper example 
   guess = toupper(guess);*/
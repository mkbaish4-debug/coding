#include <stdio.h>
int main() {
    char name[] = "Happy Diwali Bhaiyo";
    printf("%s\n", name);
    int happiness;
    printf("How happy are you on a scale of 1-5:\n", happiness);
    scanf("%d", &happiness);
    if (happiness == 1) {
    printf("Sorry buddy\n");
    } else if (happiness == 2) {
    printf("Time will fly buddy\n");
    } else if (happiness == 3) {
        printf("What's wrong buddy, just move on\n");
    } else if (happiness <= 5) {
        printf("Enjoy buddy\n");
    } else {
        printf("Invalid input Stupid\n");
    }
    return 0;
}
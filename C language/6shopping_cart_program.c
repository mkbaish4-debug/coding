#include <stdio.h>
#include <string.h>
int main() {
    int quantity = 0;
    float price = 0.0f;
    float total = 0.0f;
    char item[50] = "";
    char exit[10] = "";

    printf("Which item would you like to buy: ");
    fgets(item, sizeof(item), stdin);
    item[strlen(item) - 1] = '\0';

    printf("What is the price for each?: $");
    scanf("%f", &price);

    printf("How many would you like?: ");
    scanf("%d", &quantity);

    printf("You've bought %d %s/s! \n", quantity, item);

    total = quantity*price;

    printf("The total is: $%.2f only\n", total);
    
    printf("Thank you for shopping with us!\n");

    printf("press anything and ENTER it to exit... ");
    scanf("%s", exit);

    return 0;
}
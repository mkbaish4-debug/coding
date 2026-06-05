#include <stdio.h>
#include <stdlib.h>


int main() {
    int number = 0;
    printf("Enter the number of prices: ");
    scanf("%d", &number);

    float *prices = calloc(number, sizeof(float));
    if(prices == NULL) {
        printf("Memory allocation failed!");
        return 1;
    }

    for(int i = 0; i < number; i++) {
        printf("Enter the price no.%d: ", (i + 1));
        scanf("%f", &prices[i]);
    }

    int newnumber = 0;
    printf("Enter new number of prices: ");
    scanf("%d", &newnumber);

    float *newNumber = realloc(prices, newnumber * sizeof(float));

       for(int i = number; i < newnumber; i++) {
        printf("Enter the price no.%d: ", (i + 1));
                scanf("%f", &newNumber[i]);
    }

    for(int i = 0; i < newnumber; i++) {
        printf("$%.2f ", newNumber[i]);
    }

    free(prices);
    prices = NULL;
    return 0;
}
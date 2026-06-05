#include <stdio.h>
int main() {
    float principal;
    float rate;
    float months;
    float interest;
    float total_amount;

     printf("Enter the initial amount: ");
    scanf("%f", &principal);
   
    printf("Enter the monthly interest rate (in percentage): ");
    scanf("%f", &rate);

    printf("Enter the number of months after which you want the final amount to be calculated: ");
    scanf("%f", &months);

    interest = (principal*rate*months)/100;
    total_amount = principal + interest;
    printf("The total amount after %.0f months is: %.2f\n", months, total_amount);
    return 0; 
}
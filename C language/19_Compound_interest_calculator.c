#include <stdio.h>
#include <math.h>
int main() {
    printf("Compound interest calculator!\n");

    double principal, rate, total;
    int time, n;
    char currency = '$';

    printf("Enter the initial amount: ");
    scanf("%lf", &principal);

    printf("Enter the annual interest rate (%): ");
    scanf("%lf", &rate);

     printf("Enter the number of years: ");
      scanf("%d", &time);

       printf("Enter the amount of times interest is compounded per year: ");
       scanf("%d", &n);

       rate = rate / 100;
       total = principal * pow(1 + rate/n, n*time);

       printf("Total amount after %d years is %c%.2lf\n", time, currency, total);
       return 0;

}
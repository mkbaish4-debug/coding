#include <stdio.h>
#include <string.h>
int main() {
    printf("Temperature Conversion Calculator\n");
    printf("C. Celsius to Fahrenheit\n");
    printf("f. Fahrenheit to Celsius\n");

    char choice;
    double celsius, fahrenheit;

   do { printf("Enter your choice (C or F): ");
    scanf(" %c", &choice);

    if (choice == 'C'){
        printf("What's the temperature in Celsius: ");
        scanf("%lf", &celsius);
    
        fahrenheit = celsius*(9.0/5.0) + 32;

        printf("Temperature in fahrenheit is %.2lf", fahrenheit);

    } else if (choice == 'F'){
        printf("What's the temperature in Fahrenheit: ");
        scanf("%lf", &fahrenheit);

        celsius = (5.0/9.0) * (fahrenheit - 32);

        printf("Temperature in Celsius: %.2lf", celsius);


    } else {
        printf("Invalid input! Please type C or F!\n");
    }
} while(choice != 'C' && choice != 'F');
    return 0;
}
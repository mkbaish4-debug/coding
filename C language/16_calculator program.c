#include <stdio.h>
int main() {

    int num1;
    float num2;
    char operator = '\0';
    float result;

    printf("Enter the first number: \n");
    scanf("%d", &num1);

    printf("Enter the operator(+, -, *, /): \n");
    scanf(" %c", &operator);

    printf("Enter the second number: \n");
    scanf("%f", &num2);

    switch(operator) {
          case '+':
            result = num1 + num2;
            break;
            case '-':
            result = num1 - num2;
            break;
            case '*':
            result = num1 * num2;
            break;
            case '/':
            if(num2 == 0) {
                printf("You can't divide by 0!\n");
                return 1;
            } else {
            result = num1 / num2;
            }
        break;
            
       default:
       printf("Please enter a valid operator(+, -, *, /): \n");
       return 1;
    }
         printf("The result is: %.2f", result);
    return 0;


}
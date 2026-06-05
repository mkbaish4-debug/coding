#include <stdio.h>
int main() {

    printf("Weight conversion calculator\n");
    printf("1.Pounds to Kilograms.\n");
    printf("2.Kilograms to Pounds.\n");

     int choice;
     double kilograms, pounds;

   do {  printf("\nEnter your choice (1 or 2): ");
     scanf("%d", &choice);
     
     if(choice == 1){
        printf("Enter the weight in pounds: ");
        scanf("%lf", &pounds);
        kilograms = pounds*0.453529;
        printf("Weight in Kilograms: %.2lf\n", kilograms);
     } else if(choice == 2){
        printf("Enter weight in Kilograms: ");
        scanf("%lf", &kilograms);
        pounds = kilograms / 0.453529;
        printf("Weight in Pounds: %.2lf", pounds);
     } else {
        printf("Invalid choice.\n");
     } 
    } while(choice != 1 && choice != 2);

     return 0;
}
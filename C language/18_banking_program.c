#include <stdio.h>
void checkbalance(float balance);
float depositamount(float deposit);
float withdrawamount(float withdraw, float balance);

int main() {
    int choice;
    float balance = 0.0f;
    float deposit = 0.0f;
    float withdraw = 0.0f;



   printf("*** welcome to the bank ***\n");
    do { printf("choose an option: \n");
    printf("1.check balance.\n");
    printf("2.deposit money.\n");
    printf("3.withdraw money.\n");
    printf("4.exit.\n");
    printf("choose an option: ");
    scanf(" %d", &choice);
    switch (choice) {
        case 1:
        checkbalance(balance);
        break;
        case 2:
        balance += depositamount(deposit);
        break;
        case 3:
        balance -= withdrawamount(withdraw, balance);
        break;
        case 4:
        printf("Thanks for using the bank.\n");
        break;
        default:
        printf("Please enter a valid choice (1-4)\n ");
        
    }
    

    } while (choice != 4);
    
return 0;
}
void checkbalance(float balance) {
    printf("Your balance is %.2f\n", balance);
}
float depositamount(float deposit) {
    printf("Enter the amount you want to deposit: \n");
    scanf("%f", &deposit);
    printf("%.2f Successfully deposited!\n", deposit);
    return deposit;
}
float withdrawamount(float withdraw, float balance) {
        printf("Enter the amount you want to withdraw: \n");
    scanf("%f", &withdraw);
        if (withdraw <= balance) {
      printf("%.2f Successfully withdrawn!\n", withdraw);
      return withdraw;
        } else {
            printf("Can't withdraw this much amount!\n");
            return 0;
        }
    
    


}
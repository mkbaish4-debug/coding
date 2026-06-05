#include <stdio.h>
#include <string.h>
 
void happybirthday(char name[50], int age) {
    printf("Happy birthday to you!\n");
        printf("Happy birthday to you!\n");
        printf("Happy birthday to you dear %s!\n", name);
        printf("Happy birthday to you!\n");
            printf("You are %d years old!\n", age);

}

int main() {
    char name[50] = "";
    int age;
    printf("Enter the name of birthday boy/girl: \n");
    fgets(name, sizeof(name), stdin);
    name[strlen(name) - 1] = '\0';
     printf("Enter your age: \n");
     scanf("%d", &age);
      
     happybirthday(name, age);
     return 0;
}
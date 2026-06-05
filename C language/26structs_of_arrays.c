#include <stdio.h>


typedef struct {
    char name[100];
    int year;
    int price;

} Car;

int main() {
    Car cars[] = {{"Mustang", 2025, 32000}, 
                  {"Corvette", 2026, 68000},
                  {"Lamborghini", 2000, 5000000}};
    int number = sizeof(cars) / sizeof(cars[0]);

    for(int i = 0; i < number; i++){ 
        printf("name: %s\n", cars[i].name);
        printf("year: %d\n", cars[i].year);
        printf("model: %d\n\n", cars[i].price);
    }

  return 0;
}
#include <stdio.h>
#include <stdbool.h>
int main() {
    int x = 5;
    int y = 5;
    for(int i = 1; i <= 100; i = i + 1) {
        if(i%5 == 0) {
            printf("%d\n", x);
            x = y + 5;
            y = x + 5; 
        } else {
            printf("%d\n", i);
        }
    }
   return 0;
}
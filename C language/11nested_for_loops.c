#include <stdio.h>

int main () {
    int i, j;
    int r, c;
    char symbol = '\0';
    printf("Enter the number of rows: \n");
    scanf("%d", &r);
    printf("Enter the number of columns: \n");
    scanf("%d", &c);
    printf("Enter the symbol: \n");
    scanf(" %c", &symbol);
    for(i = 1; i <= r; i++) {
        for(j = 1; j <= c; j++) {
            printf("%c ", symbol);
        }
      printf("\n");
    }
    return 0;
}
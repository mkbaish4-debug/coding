#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <windows.h>

int main() {
    srand(time(NULL));
    int max = 20;
    int min = 10;
    int randomnum1 = (rand() % (max - min + 1)) + min;
    int randomnum2 = (rand() % (max - min + 1)) + min;
    int randomnum3 = (rand() % (max - min + 1)) + min;
    printf("%d\n", randomnum1);
    Sleep(1000);
     printf("%d\n", randomnum2);
     Sleep(1000);
      printf("%d\n", randomnum3);
      Sleep(1000);
    return 0;
}
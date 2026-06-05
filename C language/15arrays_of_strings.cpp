#include <stdio.h>
#include <string.h>
int main() {
    char names[5][100] = {};
    int size = sizeof(names)/ sizeof(names[0]);
    for(int i = 0; i < size; i++) {
    printf("Enter the name no.%d: ", (i + 1));
    fgets(names[i], sizeof(names), stdin);
    names[i][strlen(names[i]) - 1] = '\0';
    }
    for(int i = 0; i < size; i++) {
    printf("%s\n", names[i]);
    }
    return 0;
}
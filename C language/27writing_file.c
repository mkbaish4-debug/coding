#include <stdio.h>
int main() {
     FILE *pFile = fopen("output.txt", "w");
     char text[] = {"Booty Booty Booty\nRockin everywhere."};
     
     if (pFile == NULL) {
          printf("Error!\n");
          return 1;
     } else {
         
          printf("File was successfully opened.");
          fprintf(pFile, "%s", text);
     }
     fclose(pFile);
     return 0;
}

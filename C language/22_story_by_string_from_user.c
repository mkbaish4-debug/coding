#include <string.h>
#include <stdio.h>
int main() {
    char noun[100] = "";
    char verb[100] = "";
    char adjective1[100] = "";
    char adjective2[100] = "";
    char adjective3[100] = "";
     printf("Enter a noun (animal or person): ");
      fgets(noun, sizeof(noun), stdin);
      noun[strlen(noun) - 1] = '\0';

     printf("Enter a verb (ending with -ing): ");
      fgets(verb, sizeof(verb), stdin);
       verb[strlen(verb) - 1] = '\0';

      printf("Enter adjective1: ");
       fgets(adjective1, sizeof(adjective1), stdin);
       adjective1[strlen(adjective1) - 1] = '\0';

       printf("Enter adjective2: ");
        fgets(adjective2, sizeof(adjective2), stdin);
        adjective2[strlen(adjective2) - 1] = '\0';

        printf("Enter adjective3: ");
    fgets(adjective3, sizeof(adjective3), stdin);
     adjective3[strlen(adjective3) - 1] = '\0';

     printf("\nHere is your story:\n");
     printf("One day you saw %s, %s. he was %s, %s, and %s.\n", noun, verb, adjective1, adjective2, adjective3);
     return 0;
}
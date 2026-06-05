#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <windows.h>

#pragma comment(linker, "/subsystem:console")
int _CRT_glob = 0;
#ifdef _UNICODE
#define _tmain wmain
#else
#define _tmain main
#endif

int _tmain(int argc, char *argv[]) {
    if (argc < 2) {
        printf("Usage: %s sourcefile.c\n", argv[0]);
        printf("Example: %s program.c\n", argv[0]);
        return 1;
    }

    char command[1024];
    
    // Build full command with all necessary Windows console flags
    snprintf(command, sizeof(command),
        "gcc -municode -mconsole \"-D_UNICODE\" \"-DUNICODE\" "
        "\"-Wl,--subsystem,console\" \"-e_mainCRTStartup\" "
        "-o \"%s.exe\" \"%s\"",
        argv[1], argv[1]);

    printf("Compiling with command:\n%s\n\n", command);
    
    int result = system(command);
    
    if (result == 0) {
        printf("Compilation successful!\n");
        printf("Running the program:\n");
        printf("-------------------\n");
        
        char run_command[256];
        snprintf(run_command, sizeof(run_command), "\"%s.exe\"", argv[1]);
        result = system(run_command);
        
        printf("-------------------\n");
        if (result == 0) {
            printf("Program executed successfully!\n");
        } else {
            printf("Program execution failed (code %d)\n", result);
        }
    } else {
        printf("Compilation failed (code %d)\n", result);
    }

    return result;
}
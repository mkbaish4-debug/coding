#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <process.h>

int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("Usage: compiler.exe sourcefile.c\n");
        printf("Example: compiler.exe program.c\n");
        return 1;
    }

    char source_file[256];
    char output_file[256];
    char command[512];

    // Copy source file name
    strncpy(source_file, argv[1], sizeof(source_file) - 1);
    source_file[sizeof(source_file) - 1] = '\0';

    // Create output filename (replace .c with .exe)
    strncpy(output_file, source_file, sizeof(output_file) - 1);
    output_file[sizeof(output_file) - 1] = '\0';
    char *dot = strrchr(output_file, '.');
    if (dot) {
        strcpy(dot, ".exe");
    } else {
        strcat(output_file, ".exe");
    }

    // Build the gcc command with all necessary flags
    snprintf(command, sizeof(command),
        "gcc \"-Wl,--subsystem,console\" -o %s %s",
        output_file, source_file);

    // Print what we're doing
    printf("Compiling %s to %s...\n", source_file, output_file);
    printf("Command: %s\n", command);

    // Execute the compilation
    int result = system(command);
    
    if (result == 0) {
        printf("\nCompilation successful!\n");
        printf("Running the program:\n");
        printf("-------------------\n");
        
        // Run the compiled program
        result = system(output_file);
        printf("-------------------\n");
        
        if (result == 0) {
            printf("Program ran successfully!\n");
        } else {
            printf("Program execution failed with code %d\n", result);
        }
    } else {
        printf("Compilation failed with code %d\n", result);
    }

    return result;
}
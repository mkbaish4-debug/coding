#include <stdio.h>
#include <stdbool.h>
#include <string.h>





typedef struct {
    char name[50];
    int age;
    float gpa;
    bool isfulltime;
}Student;


void description(Student student);

int main() {
    Student student1 = {"Mayank", 18, 7.00, true};
    Student student2;
    strcpy (student2.name, "Bhanu");
    student2.age = 17;
    student2.gpa = 8.00;
    student2.isfulltime = false;
    description(student1);
    description(student2);
    
    

    return 0;
}

void description(Student student) {
    printf("%s\n", student.name);
    printf("%d\n", student.age);
    printf("%.2f\n", student.gpa);
    printf("%s\n\n", (student.isfulltime) ? "Yes" : "No");
}
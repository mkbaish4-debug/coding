#include <stdio.h>
#include <math.h>
int main() {
    double radius;
    double area;
    double surface_area;
    double volume;
    printf("Enter the radius: ");
    scanf("%lf", &radius);
    area = M_PI  * pow(radius, 2);
    surface_area = 4 * M_PI   * pow(radius, 2);
    volume = (4.0/3.0) * M_PI  * pow(radius, 3);

    printf("area = %lf\n", area);
    printf("surface area = %lf\n", surface_area);
    printf("volume = %lf\n", volume);
    return 0;

}
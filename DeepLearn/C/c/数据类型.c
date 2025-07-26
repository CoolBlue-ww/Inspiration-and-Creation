#include <stdio.h>
#include <limits.h>
#include <float.h>


void def1(void) {
    printf("%lu\n", sizeof(int));
}

void def2(void) {
    printf("%lu\n", sizeof(float));
}

void def3(void) {
    printf("%lu\n", sizeof(double));
}

void def4(void) {
    printf("%lu\n", sizeof(long double));
}


void def5(void) {
    printf("%E\n", FLT_MIN);
    printf("%E\n", FLT_MAX);
    printf("%d\n", FLT_DIG);
}

void def6(void) {
    printf("%E\n", DBL_MIN);
    printf("%E\n", DBL_MAX);
    printf("%d\n", DBL_DIG);
}


int main() {
    def1();
    def2();
    def3();
    def4();
    printf("----------------------------\n");
    def5();
    def6();
    return 0;
}
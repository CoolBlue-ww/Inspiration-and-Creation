#include <stdio.h>

void print_C(void) {
    for (int i = 0; i < 6; i++) {
        if (i == 0 || i == 5) {
            printf("************\n");
        }else {
            printf("*\n");
        }
    }
}


int main(void) {
    print_C();
    return 0;
}
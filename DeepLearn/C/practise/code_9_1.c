#include <stdio.h>

int main(void) {
    int i, j;
    for (i = 0; i < 8; i++) {
        if (i == 0 || i == 2 || i == 4 || i == 6) {
            for (j = 0; j < 8; j++) {
                if (j == 1 || j == 3 || j == 5 || j == 7) {
                    printf("%c%c", 219, 219);
                }else {
                    printf("  ");
                }
            }
            printf("\n");
        }else {
            for (j = 0; j < 8; j++) {
                if (j == 0 || j == 2 || j ==4 || j == 6) {
                    printf("%c%c", 219, 219);
                }else {
                    printf("  ");
                }
            }
            printf("\n");
        }
    }
    return 0;
}
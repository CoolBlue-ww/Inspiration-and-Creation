#include <stdio.h>


void print_chessboard(void) {
    int i, j;
    for (i = 0; i < 8; i++) {
        for (j = 0; j < 8; j++) {
            if ((i + j) % 2 == 0) {
                printf("%c%c", 219,219);
            }else {
                printf("  ");
            }
        }
        printf("\n");
    }
}


int main(void) {
    print_chessboard();
    return 0;
}
#include <stdio.h>

// 9*9乘法表

void print_table(void) {
    int i, j;
    for (i = 1; i <= 9; i++) {
        for (j=j = 1; j <= i; j++) {
            printf("%d * %d = %d\t", i, j, i * j);
        }
        printf("\n");    
    }
}

int main(void) {
    print_table();
    return 0;
}
#include <stdio.h>


void print_num(void) {
    for (int num = 100; num <= 999; num++) {
        int x = num / 100;
        int y = num % 100 / 10;
        int z = num % 100 % 10;
        if (x * x * x + y * y * y + z * z * z == x * 100 + y * 10 + z) {
            printf("%d 是水仙花数\n", num);
        }
    }
}

int main(void) {
    print_num();
    return 0;
}
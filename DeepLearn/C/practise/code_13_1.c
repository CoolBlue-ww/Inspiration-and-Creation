#include <stdio.h>


// 打印水仙花数

void print_num(void) {
    int x, y, z;
    for (x = 1; x <= 9; x++) {
        for (y = 0; y <= 9; y++) {
            for (z = 0; z <= 9; z++) {
                if (x * x * x + y * y * y + z * z * z == x * 100 + y * 10 + z) {
                    printf("%d%d%d 是水仙花数\n", x, y, z);
                }
            }
        }
    }
}



int main(void) {
    print_num();
    return 0;
}
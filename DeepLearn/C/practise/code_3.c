#include <stdio.h>
int main(void) {
    for (int i = 1; i <= 168 / 2; i++) {
        if (168 % i == 0) {
            int j = 168 / i;
            if (j > i && (j + i) % 2 == 0 && (j - i) % 2 == 0) {
                int n = (j + i) / 2;
                int m = (j - i) / 2;
                int number = n * n - 268;
                printf("一个整数加上100是完全平方数，再加上168还是完全平方数，那么这个整数是：%d\n", number);
                
            }
        }
    }
    return 0;
}
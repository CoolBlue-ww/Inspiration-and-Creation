// 判断找出101到200之间的素数
#include <stdio.h>

void is_prime(void) {
    int i = 101, j = 200;
    int count = 0;
    for (i; i <= j; i++) {
        int mean = (int)(i / 2) + 1;
        int sign;
        for (int sub = 2; sub < mean; sub++) {
            if (i % sub == 0) {
                sign += 1;
                break;
            }else {
                sign = 0;
            }
        }
        if (sign == 0 ) {
            printf("数字 %d 是素数\n", i);
            count++;
        }else {
            continue;
        }
    }
    printf("在101到200之间共有 %d 个素数\n", count);
}

int main(void) {
    is_prime();
    return 0;
}
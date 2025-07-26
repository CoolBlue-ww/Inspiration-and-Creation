#include <stdio.h>

int main(void) {
    const char *C[] = {
        "*******",
        "*",
        "*",
        "*",
        "*",
        "*******",
    };
    printf("使用*打印C\n");
    for (int i = 0; i < sizeof(C) / sizeof(C[0]); i++) {
        printf("%s\n", C[i]);
    }
    return 0;
}
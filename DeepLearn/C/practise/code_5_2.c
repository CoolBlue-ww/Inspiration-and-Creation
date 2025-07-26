#include <stdio.h>

int main(void) {
    int a, b, c, T;
    printf("请输入三个整数：\n");
    scanf("%d %d %d", &a, &b, &c);
    if (a > b) {
        T = a; a = b; b = T;
    }
    if (a > c) {
        T = a; a = c; c = T;
    }
    if (b > c) {
        T = b; b = c, c = T;
    }
    printf("把这三个整数从小到大排列为：%d < %d < %d\n", a, b, c);
    return 0;
}
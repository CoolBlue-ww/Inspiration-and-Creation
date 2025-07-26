#include <stdio.h>


int add(int a, int b);


int add(int a, int b) {
    return a + b;
}

float main() {
    int x, y;
    printf("请输入两个整数：\n");
    fflush(stdout);
    scanf("%d %d", &x, &y);
    const float PI = 3.1415926;
    printf("这个圆的直径是：%d\n", add(x, y));
    float r = add(x, y) / 2.0f;
    printf("这个圆的面积是：%f\n", PI * r * r);
    return 0;
}
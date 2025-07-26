#include <stdio.h>
extern int hi()
{
    printf("你好, C!\n");

    return 0;
}

void main() {
    hi();
}
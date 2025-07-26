//
// Created by ckr-win on 25-7-22.
//
#include <stdio.h>
#include "c_practise_15.h"

// 题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。

int main(void) {
    int fraction;
    printf("请输入你的成绩：\n");
    scanf("%d", &fraction);
    if (fraction >= 90) {
        printf("A\n");
    }
    if (60 <= fraction && fraction <= 89) {
        printf("B\n");
    }
    if (fraction < 60) {
        printf("C\n");
    }
    return 0;
}

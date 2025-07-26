#include <stdio.h>

// 输入三个整数把他们从小到大排列输出。

void input_three_integers(int *a, int *b, int *c) {
    printf("请输入三个整数：\n");
    scanf("%d %d %d", a, b, c);
}


int main(void) {
    int a, b, c;
    input_three_integers(&a, &b, &c);
    int nums[3] = {a, b, c};
    for (int i = 0; i < 3; i++) {
        if (i == 2) {
            break;
        }
        if (nums[i] > nums[i + 1]) {
            int temp = nums[i];
            nums[i] = nums[i + 1];
            nums[i + 1] = temp;
        }
    }
    printf("把这三个整数从新小到大排列为：[%d, %d, %d]\n", nums[0], nums[1], nums[2]);
    return 0;
}
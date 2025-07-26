#include <stdio.h>


extern int array(void) {
    // 定义一个初始化数组和循环次数
    int num = 1000000000;
    int array[3][3] = {
        {0, 0, 0},
        {0, 0, 0},
        {0, 0, 0}
    };
    for (int i = 1; i <= num; i++) {
        if (i <= num / 2) {
            array[0][0] += 4;
            array[0][1] += 4;
            array[0][2] += 4;
            array[1][0] += 4;
            array[1][1] += 4;
            array[1][2] += 4;
            array[2][0] += 4;
            array[2][1] += 4;
            array[2][2] += 4;

        } else if (i > (num / 2) && i <= (4 * num / 5)){
            array[0][0] *= 1;
            array[0][1] *= 2;
            array[0][2] *= 4;
            array[1][0] *= 4;
            array[1][1] *= 2;
            array[1][2] *= 1;
            array[2][0] *= 2;
            array[2][1] *= 4;
            array[2][2] *= 1;
        }else {
            array[0][0] -= 1;
            array[0][1] -= 1;
            array[0][2] -= 1;
            array[1][0] -= 1;
            array[1][1] -= 1;
            array[1][2] -= 1;
            array[2][0] -= 1;
            array[2][1] -= 1;
            array[2][2] -= 1;
        }
    } 
    return 0;
}

int main(void) {
    array();
    return 0;
}
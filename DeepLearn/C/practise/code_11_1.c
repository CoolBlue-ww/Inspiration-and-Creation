#include <stdio.h>

int fb(int *month) {
    // 初始化前两个月的兔子对数
    if (*month == 1 || *month == 2) {
        return 1;
    }
    if (*month >= 3) {
        // 根据fibonacci数列计算兔子的对数
        int fb1 = 1, fb2 = 1, fb3;
        for (int count = 3; count <= *month; count++) {
            fb3 = fb1 + fb2;
            printf("第%d个月的兔子对数为： %d\n", count, fb3);
            fb1 = fb2;
            fb2 = fb3; 
        }
        return fb3;
    }
}


int main(void) {
    int month, total;
    printf("请输入月份：");
    scanf("%d", &month);
    total = fb(&month);
    printf("\n\n-------------------------------\n");
    printf("当%d月后,也就是最后一个月时，兔子总三对数为：%d\n", month, total);
    return 0;
}
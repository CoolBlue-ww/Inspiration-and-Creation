# include <stdio.h>


int main(void) {
    int year, month, day;
    printf("请输入年月日：\n");
    scanf("%d %d %d", &year, &month, &day);
    int month_days[12] = {
        31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
    };
    int total_days = 0;
    for (int count = 0; count < month - 1; count++) {
        if (year % 4 == 0 && year % 100 != 0 || year % 400 == 0) {
            month_days[1] = 29; 
            total_days += month_days[count];
        }else {
            total_days += month_days[count];
        }
    }
    total_days += day;
    printf("%d年%d月%d日是这一年的第“%d”天。\n", year, month, day, total_days);
}
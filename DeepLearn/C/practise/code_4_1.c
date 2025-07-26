#include <stdio.h>

// 判断某年某月某日是这一年的第几天。

void input_date(int *year, int *month, int *day) {
    printf("请输入年月日：\n");
    scanf("%d %d %d", year, month, day);
}


int judge(int year) {
    if (year % 4 == 0 && year % 100 != 0 || year % 400 == 0) {
        return 0;
    }else {
        return 1;
    }
}

int to_days(int JUDGE, int month, int day) {
    int month_to_days[12] = {
        31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
    };
    int last_month = month - 1;
    int days = 0;
    for (int count = 0; count < last_month; count++) {
        if (JUDGE == 0 && month_to_days[count] == 28) {
            month_to_days[count] = 29;
            days += month_to_days[count];
        } else {
            days += month_to_days[count];
        }
    }
    return days + day;
}


int main(void) {
    int year, month, day;
    input_date(&year, &month, &day);
    printf("%d %d %d\n", year, month, day);
    int JUDGE = judge(year);
    int days = to_days(JUDGE, month, day);
    printf("%d年%d月%d日是这一年的第“%d”天。\n", year, month, day, days);
    return 0;
}
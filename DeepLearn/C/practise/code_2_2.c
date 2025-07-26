#include <stdio.h>

float InputProfit() {
    printf("请输入当月的总利润（万元）：\n");
    float profit;
    scanf("%f", &profit);
    return profit;
}


float ComputeBonus(float profit) {
    // 定义利润区间和奖金比例
    int bonus_range[6][2] = {
        {0, 10},
        {10, 20},
        {20, 40},
        {40, 60},
        {60, 100},
        {100, 0}
    };
    float bonus_rate[6] = {
        0.1,
        0.075,
        0.05,
        0.03,
        0.015,
        0.01
    };
    // 个根据利润计算奖金
    float bonus = 0;
    float bonus_i = 0;
    float bonus_j = 0;
    int count;
    for (count = 0; count < 6; count++) {
        int re = bonus_range[count][0];
        int ng = bonus_range[count][1];
        if (profit == 0) {
            bonus = 0;
            return bonus;
        }else if (profit < 0) {
            return profit;
        }else {
            if (profit > re && profit <= ng && ng > re) {
                for (int index = 0; index < count; index++) {
                    int left = bonus_range[index][0];
                    int right = bonus_range[index][1];
                    int length = right - left;
                    bonus += length * bonus_rate[index];
                }
                bonus_i += bonus + (profit - re) * bonus_rate[count];
            }else if (profit > re && profit > ng && ng < re) {
                for (int index = 0; index < count; index++) {
                    int left = bonus_range[index][0], right = bonus_range[index][1], length = right - left;
                    bonus += length * bonus_rate[index];
                }
                bonus_j += bonus + (profit - re) * bonus_rate[count];
            }else {
                continue;
            }
        }
    }
    if (bonus_i != 0) {
        return bonus_i;
    }else {
        return bonus_j;
    }
}

void main() {
    float profit = InputProfit();
    float bonus = ComputeBonus(profit);
    if (bonus > 0) {
        printf("根据本月总利润： %.2f万元，本月的奖金为： %.2f万元。\n", profit, bonus);
    }else if (bonus == 0) {
        printf("本月无利润，因此没有奖金。\n");
    }else {
        printf("都开始负债了，还想要奖金？？？\n");
    }
}



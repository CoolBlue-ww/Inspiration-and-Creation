#include <stdio.h>

float Profit() {
    printf("请输入当月的利润(万元)：\n");
    float profit;
    scanf("%f", &profit);
    return profit;
}


float Bonus(float profit) {
    // 0-10 10-20 20-40 40-60 60-100 100<
    // 从初始化奖金总数
    float bonus = 0;
    if (profit >= 0 && profit <= 10) {
        bonus += 0.1 * profit;
    }
    if (profit > 10 && profit <= 20) {
        bonus += 0.1 * 10 + (profit - 10) * 0.075;
    }
    if (profit > 20 && profit <= 40) {
        bonus += 0.1 * 10 + 0.075 * 10 + 0.05 * (profit - 20);
    }
    if (profit > 40 && profit <= 60) {
        bonus += 0.1 * 10 + 0.075 * 10 + 0.05 * 20 + 0.03 * (profit - 40);
    }
    if (profit > 60 && profit <= 100) {
        bonus += 0.1 * 10 + 0.075 * 10 + 0.05 * 20 + 0.03 * 20 + 0.015 * (profit - 60);
    }
    if (profit > 100) {
        bonus += 0.1 * 10 + 0.075 * 10 + 0.05 * 20 + 0.03 * 20 + 0.015 * 40 + 0.01 * (profit - 100);
    }  
    printf("当月总利润为：%.2f （万元）时， 奖金总数为： %.2f（万元）\n", profit, bonus);  
}


void main() {
    float profit = Profit();
    Bonus(profit);
}
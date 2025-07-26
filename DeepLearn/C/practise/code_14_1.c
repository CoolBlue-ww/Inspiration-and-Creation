#include <stdio.h>
#include <math.h>


void prime_factorization(int *number) {
    if (*number < 0) {
        printf("请输入一个正整数\n");
        return;
    }
    int number_sqrt = sqrt(*number);
    
}


int main(void) {
    int number;
    printf("请输入一个正整数: ");
    scanf("%d", &number);
    prime_factorization(&number);
    return 0;
}
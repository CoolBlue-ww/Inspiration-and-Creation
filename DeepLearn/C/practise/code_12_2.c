#include <stdio.h>


void is_prime(int *start, int *end) {
    int count = 0;
    for (*start; *start <= *end; (*start)++) {
        int i;
        for (i = 2; i < ((int)(*start / 2) + 1); i++) {
            if (*start % i == 0) {
                break;
            }
        }
        if (i >= ((int)(*start / 2) + 1)) {
            printf("%d ", *start);
            count++;
            if (count % 5 == 0) {
                printf("\n");
            }
        }
    }
    printf("\n");
}

int main(void) {
    int start = 101, end = 200;
    printf("素数在%d到%d之间的有：\n", start, end);
    is_prime(&start, &end);
    return 0;
}

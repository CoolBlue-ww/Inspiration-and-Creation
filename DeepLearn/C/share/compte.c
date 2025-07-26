#include <stdio.h>

extern int compte(void) {
    int number = 1000000000;
    int total = 0;
    for (int i = 1; i <= number; i++) {
        total += i;
    }
    return total;
}


 int main() {
    int result = compte();
    printf("The result is %d\n", result);
    return 0;
}
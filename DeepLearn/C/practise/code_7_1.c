#include <stdio.h>


int main(void) {
    char a[] = "\u2591\n", b[] = "\u2588\n";
    printf("%s %s %s\n", a, b, a);
    printf("%s %s %s", b, a, b);
    return 0;
}
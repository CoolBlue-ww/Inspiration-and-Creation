#include <stdio.h>


void print_smFace_with_stair(int *m, int *n) {
    char sm_face = '*';
    char stair = 'n';
    for (int i = 1; i <= *m; i++) {
        printf("%c", sm_face);
        if (i == *m) {
            printf("%c\n", sm_face);
        }
    }
    for (int j = 1; j <= *n; j++) {
        for (int k = 0; k <= j; k++) {
            printf("%c", stair);
            if (k == j) {
                printf("%c\n", stair);
            }
        }
    }
}



int main(void) {
    int m, n;
    printf("请输入笑脸个数和楼梯高度：");
    scanf("%d %d", &m, &n);
    print_smFace_with_stair(&m, &n);
    return 0;
}
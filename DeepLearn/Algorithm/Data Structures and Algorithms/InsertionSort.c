//
// Created by ckr-win on 25-7-30.
//

#include <stdio.h>

void insertion_sort_1(int arr[], int arr_size) {
    for (int i = 1; i < arr_size; i++) {
        for (int j = i; j > 0; j--) {
            if (arr[j] < arr[j - 1]) {
                int temp = arr[j];
                arr[j] = arr[j - 1];
                arr[j - 1] = temp;
            }else {
                break;
            }
        }
    }
    for (int k = 0; k < arr_size; k++) {
        printf("%d ", arr[k]);
    }
}


void insertion_sort_2(int arr[], int arr_size) {
    for (int i = 1; i < arr_size; i++) {
        int current = arr[i];
        int j = i -1;
        while (j >= 0 && arr[j] > current) {
            arr[j + 1] = arr[j];
            j -= 1;
        }
        arr[j + 1] = current;
    }
    for (int k = 0; k < arr_size; k++) {
        printf("%d ", arr[k]);
    }
}

int main(void) {
    int arr[] = {6, 5, 4, 3, 2, 1};
    int arr_size = sizeof(arr) / sizeof(arr[0]);
    insertion_sort_2(arr, arr_size);
}



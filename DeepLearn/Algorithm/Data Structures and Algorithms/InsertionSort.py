def insertion_sort_1(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
            else:
                break
    return arr


def insertion_sort_2(arr):
    for i in range(1, len(arr)):
        current_value = arr[i]
        j = i - 1
        while j >= 0 and current_value< arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current_value
    return arr

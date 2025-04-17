array = [1, 9, 4, 0, 3, 7, 3, 5, 2, 7, 0, 2, 4, 2]


def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[: len(arr) // 2]
        right_arr = arr[len(arr) // 2 :]

        merge_sort(left_arr)
        merge_sort(right_arr)

        i, j, k = 0, 0, 0

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
    return arr


print(merge_sort(array))

# output = [0, 0, 1, 2, 2, 2, 3, 3, 4, 4, 5, 7, 7, 9]

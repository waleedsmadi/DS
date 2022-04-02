def bubble_sort(arr):

    for i in range(len(arr)):

        for k in range(len(arr) - i - 1):
            if arr[k] > arr[k + 1]:
                arr[k], arr[k+1] = arr[k+1], arr[k]
    return arr
# merge sort depends on splitting the array
# and sorting the left and right side
# then it merges it together
# takes in the best, average and worst case O(n log n)

def merge_sort(array):
    """ sorting an array ASC by merge sorting """

    if len(array) > 1:
        mid_arr = len(array) // 2
        left_arr = array[:mid_arr]
        right_arr = array[mid_arr:]

        merge_sort(left_arr)
        merge_sort(right_arr)

        l = r = x = 0

        while l < len(left_arr) and r < len(right_arr):
            if left_arr[l] < right_arr[r]:
                array[x] = left_arr[l]
                l += 1
            else:
                array[x] = right_arr[r]
                r += 1
            x += 1

        while l < len(left_arr):
            array[x] = left_arr[l]
            l += 1
            x += 1

        while r < len(right_arr):
            array[x] = right_arr[r]
            r += 1
            x += 1


arr = [10, 5, 6, 4, 7, 8, 9, 3, 2, 1]
merge_sort(arr)
print(arr)

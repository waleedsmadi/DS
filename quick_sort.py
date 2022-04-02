# quick sort depends on putting the end
# the start element in the right way to sorting
# takes in the best and average case O(n log n)
# and in the best case O(n ^ 2)


def partition(start, end, array):
    """ to put the pivot in the right way """
    pivot = array[end]
    index = (start - 1)

    for i in range(start, end):
        if array[i] < pivot:
            index += 1
            array[index], array[i] = array[i], array[index]

    array[index+1], array[end] = array[end], array[index+1]
    return index + 1


def quick_sort(start, end, array):
    """ send the array to partition after splitting """
    if len(array) <= 1:
        return array
    if start < end:

        p = partition(start, end, array)
        quick_sort(start, p-1, array)
        quick_sort(p+1, end, array)


arr = [10, 5, 6, 7, 3, 2, 1, 8, 4, 9]
quick_sort(0, len(arr)-1, arr)
print(arr)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

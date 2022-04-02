# heap sort depends on complete tree
# to sorting, takes an array and splits it
# to subtrees and takes the biggest child
# and put it as a root
# takes in the best, average and worst case O(n log n)


def heapify(i, length, array):
    """ heapify the array """

    largest = i  # root
    l = i * 2 + 1  # left child
    r = i * 2 + 2  # right child

    # make sure of left child if exists, and if root is less than it
    if l < length and array[i] < array[l]:
        largest = l

    # make sure of right child if exists, and if root is less than it
    if r < length and array[largest] < array[r]:
        largest = r

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(largest, length, array)


def heap_sort(array):
    """ sorting an array ASC by heap sort """

    length = len(array)

    # get the last root of the tree
    for i in range(length // 2 - 1, -1, -1):
        heapify(i, length, array)
    # start sorting
    for i in range(length-1, 0, -1):
        array[0], array[i] = array[i], array[0]
        heapify(0, i, array)


arr = [10, 9, 5, 6, 7, 8, 3, 2, 4, 1]
heap_sort(arr)
print(arr)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

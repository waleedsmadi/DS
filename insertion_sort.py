# insertion method depends on the previous index
# takes in the average and worst case O(n^2)
# and in the best case O(n)


def insertion(array):

    """ Sorting an array ASC by insertion function """

    for i in range(1, len(array)):
        value = array[i]
        prev_index = (i - 1)

        while prev_index >= 0 and value < array[prev_index]:
            array[prev_index + 1] = array[prev_index]
            prev_index -= 1
        array[prev_index + 1] = value


arr = [10, 6, 7, 8, 4, 3, 2, 1, 5, 9]
insertion(arr)
print(arr)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def selection(array):

    for i in range(len(array)):
        min_index = i

        for k in range(i+1, len(array)):
            if array[k] < array[min_index]:
                min_index = k
        array[i], array[min_index] = array[min_index], array[i]


arr = [10, 7, 3, 6, 4, 5, 2, 3, 1]
selection(arr)
print(arr)


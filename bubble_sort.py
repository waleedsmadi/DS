# Simple code for bubble_sort algorithm
# takes in the average and worst case O(n^2)
# and in the best case O(n)

""" writen by python """


def bubble_sort(arr):
    """ to sorting ASC by bubble sort """
    for i in range(len(arr)):

        for k in range(len(arr) - i - 1):
            if arr[k] > arr[k + 1]:
                arr[k], arr[k+1] = arr[k+1], arr[k]
    return arr
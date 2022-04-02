# Hash Table is a data structure which stores data in an associative manner.
# In a hash table, data is stored in an array format, where each data value
# has its own unique index value. Access of data becomes very fast if we know
# the index of the desired data.
#
# Thus, it becomes a data structure in which insertion and search
# operations are very fast irrespective of the size of the data.
# Hash Table uses an array as a storage medium and uses hash technique
# to generate an index where an element is to be inserted or is to be located from.
#
# Hashing:
# Hashing is a technique to convert a range of key values into a range of
# indexes of an array. We're going to use modulo operator to get a range of key values.
#
# Linear Probing: In linear probing, we linearly probe for next slot.
# For example, the typical gap between two probes is 1 as seen in the example below.
# Let hash(x) be the slot index computed using a hash function and S be the table size

class HashTable:
    def __init__(self, size):
        self._size = size
        self._array = [None] * self._size
        self._counter = 0

    def _hash(self, element):
        """ hashing the index """

        index = element % self._size

        if self._array[index] is None:
            return index
        while self._array[index] is not None:
            index = (index - 1) % self._size
        return index

    def is_full(self):
        """ check if the array is full """

        return self._counter == self._size

    def is_empty(self):
        """ check if the array is empty """

        return self._counter == 0

    def insert(self, element):
        """ to insert the element """

        if self.is_full():
            return
        index = self._hash(element)
        self._array[index] = element
        self._counter += 1

    def search(self, element):
        """ searching about an element """

        if self.is_empty():
            return

        index = element % self._size
        if self._array[index] == element:
            return f"the element {element} exists in index {index}"
        while self._array[index] is not None and self._array[index] != element:
            index = (index - 1) % self._size

        if self._array[index] == element:
            return f"the element {element} exists in index {index}"
        return f"element {element} does not exist"

    def display(self):
        """ display the array """

        for x in range(len(self._array)):
            print(x, self._array[x], sep=" ----> ")


h = HashTable(10)
h.insert(2)
h.insert(2)
h.insert(9)
h.insert(6)
print(h.search(9))
h.display()

# OutPut:
# the element 9 exists in index 9
# 0 ----> None
# 1 ----> 2
# 2 ----> 2
# 3 ----> None
# 4 ----> None
# 5 ----> None
# 6 ----> 6
# 7 ----> None
# 8 ----> None
# 9 ----> 9

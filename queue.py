# A Queue is a linear structure which follows a particular order
# in which the operations are performed. The order is First In First Out (FIFO).
# A good example of a queue is any queue of consumers for a resource
# where the consumer that came first is served first.
# The difference between stacks and queues is in removing.
# In a stack we remove the item the most recently added;
# in a queue, we remove the item the least recently added.


class Node:
    """ Node class to initialize value and next pointer """
    def __init__(self, value=None):
        self.value = value
        self.next = None


class QueueClass:
    """ Queue class and initialize head and last pointers """
    def __init__(self):
        self.head = self.last = None



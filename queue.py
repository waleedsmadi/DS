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

    def queue(self, element):
        """ to add an element to the queue """
        new_element = Node(element)

        # for first insertion case
        if not self.head:
            self.head = self.last = new_element
            return

        # move the last pointer to the last element
        self.last.next = new_element
        self.last = new_element

    def is_empty(self):
        """ to check if is empty """
        return self.head is None

    def de_queue(self):
        """ to remove the first element (First In First Out) """
        if self.is_empty():
            return
        if self.head == self.last:
            self.head = self.last = None
            return
        self.head = self.head.next

    def display(self):
        """ display the queue """

        elem = []
        curr_node = self.head
        while curr_node is not None:
            elem.append(curr_node.value)
            curr_node = curr_node.next
        print(elem)


q = QueueClass()
q.queue(1)
q.queue(2)
q.queue(3)
q.queue(4)
q.queue(5)
q.de_queue()
q.display()
# [2, 3, 4, 5]

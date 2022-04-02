# A linked list is a sequence of data structures,
# which are connected together via links.
#
# Linked List is a sequence of links which contains items.
# Each link contains a connection to another link.
# Linked list is the second most-used data structure after array.
#
# (functions)
# add(element)
# remove(element)
# pop()
# peek()
# display()

class Node:
    """ Node class to link the array with each other """
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    """ Linked list class """

    def __init__(self):
        self.head = Node()

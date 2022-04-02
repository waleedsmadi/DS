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

    def pop(self):
        # check if is empty

        curr_node = self.head
        prev = None
        while curr_node.next is not None:
            prev = curr_node
            curr_node = curr_node.next
        last_element = curr_node.value
        prev.next = None
        return last_element

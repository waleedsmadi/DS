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

    def add(self, element):
        """ add function """

        # the new node
        new_node = Node(element)

        # if condition for the first element
        if self.head.next is None:
            self.head = new_node
            return

        # go to the end of list to add the new element
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next

        # add the new element
        curr_node.next = new_node



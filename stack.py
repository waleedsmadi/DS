# Stack is a linear data structure which follows a particular
# order in which the operations are performed. The order may be
# LIFO(Last In First Out) or FILO(First In Last Out).
#
# functions
# push()
# is_empty()
# pop()
# peek()
# display()


class Node:
    """ Node class to initialize value and next pointer """
    def __init__(self, value=None):
        self.value = value
        self.next = None


class Stack:
    """ Stack class """
    def __init__(self):
        self.top = None

    def push(self, element):
        """ push function"""

        # create the new element
        new_element = Node(element)

        if self.top is None:
            self.top = new_element
            return
        new_element.next = self.top
        self.top = new_element


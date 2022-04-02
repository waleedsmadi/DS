# Binary Search Tree is a node-based binary tree data structure which has the following properties:
#
# 1- The left subtree of a node contains only nodes with keys lesser than the node’s key.
# 2- The right subtree of a node contains only nodes with keys greater than the node’s key.
# 3- The left and right subtree each must also be a binary search tree.

class Node:
    """ Node to initialize the value, left and right """
    def __init__(self, value=None):
        self.value = value
        self.left = self.right = None


class BinarySearchTree:
    """ BinarySearchTree class """

    def insert(self, root, element):

        # if current node is empty return node with the element
        if not root:
            return Node(element)

        # put the element on the left side
        if element < root.value:
            root.left = self.insert(root.left, element)

        # put the element on the right side
        elif element > root.value:
            root.right = self.insert(root.right, element)

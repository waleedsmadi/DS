# AVL tree is a self-balancing Binary Search Tree (BST)
# where the difference between heights of left and right
# subtrees cannot be more than one for all nodes.

class Node:
    """ Node to initialize value, left, right and height """
    def __init__(self, value=None):
        self.value = value
        self.left = self.right = None
        self.height = 1


class AVLTree:
    """ AVLTree class """

    @staticmethod
    def get_height(root):
        """ get height function """
        if not root:
            return 0
        return root.height

    def get_min(self, root):
        """ gin minimum value of the tree """
        if not root.left:
            return root
        return self.get_height(root.left)

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

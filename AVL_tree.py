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

    def l_rotation(self, x):
        """ left rotation function """

        y = x.right
        t = y.left
        y.left = x
        x.right = t

        # update the height
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def r_rotation(self, x):
        """ right rotation function """

        y = x.left
        t = y.right
        y.right = x
        x.left = t

        # update the height
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def insert(self, root, element):
        """ to insert elements to the tree """

        # searching about the right place to add the element
        if not root:
            return Node(element)
        elif element < root.value:
            root.left = self.insert(root.left, element)
        elif element > root.value:
            root.right = self.insert(root.right, element)

        # update the height
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance_factor = self.get_balance(root)

        if balance_factor < -1:  # means it's a left rotation
            if element > root.right.value:  # means it's left-left rotation
                return self.l_rotation(root)

            else:  # means it's left-right rotation
                root.right = self.r_rotation(root.right)
                return self.l_rotation(root)

        if balance_factor > 1:  # means it's a right rotation
            if element < root.left.value:  # means it's right-right rotation
                return self.r_rotation(root)

            else:  # means it's right-left rotation
                root.left = self.l_rotation(root.left)
                return self.r_rotation(root)

        return root

    def remove(self, root, element):
        """ to remove an element from the tree """

        # searching about the element
        if not root:
            return root
        elif element < root.value:
            root.left = self.remove(root.left, element)

        elif element > root.value:
            root.right = self.remove(root.right, element)

        # found the element
        else:
            if not root.left:  # right child case
                return root.right
            elif not root.right:  # left child case
                return root.left

            else:  # two children case
                val = self.get_min(root.right).value
                root.value = val
                root.right = self.remove(root.right, val)

        # update the height
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance_factor = self.get_balance(root)

        if balance_factor < -1:  # means it's left rotation
            if self.get_balance(root.right) <= 0:  # means it's left-left rotation
                return self.l_rotation(root)

            else:  # means it's left-right rotation
                root.right = self.r_rotation(root.right)
                return self.l_rotation(root)

        if balance_factor > 1:  # means it's right rotation
            if self.get_balance(root.left) >= 0:  # means it's right-right rotation
                return self.r_rotation(root)

            else:  # means it's right-left rotation
                root.left = self.l_rotation(root.left)
                return self.r_rotation(root)

        return root

    def pre_order(self, root):
        """ display the tree in pre-order way """
        if root:
            print("{0} ".format(root.value), end="")
            self.pre_order(root.left)
            self.pre_order(root.right)

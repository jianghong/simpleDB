BLACK = 0
RED = 1

class Node:
    def __init__(self, key=None, parent=None, left=None,
                 right=None, color=BLACK):
        self.color = color
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right

# Sentinel Nil node; This node is black and the other values don't matter
NIL_NODE = Node() 


class RBTree:
    def __init__(self, root=Node()):
        self.root = root
        self.root.parent = NIL_NODE
        self.root.left = NIL_NODE
        self.root.right = NIL_NODE

    def insert(self, new_node):
        """
        Insert new_node into RBTree.
        Assumes new_node.key exists.
        """
        operating_node = NIL_NODE
        walker_node = self.root
        while walker_node != NIL_NODE:
            operating_node = walker_node
            if new_node.key < walker_node.key:
                walker_node = walker_node.left
            else:
                walker_node = walker_node.right

        new_node.parent = operating_node
        if operating_node == NIL_NODE:
            self.root = new_node
        elif new_node.key < operating_node.key:
            operating_node.left = new_node
        else:
            operating_node.right = new_node
        new_node.left = NIL_NODE
        new_node.right = NIL_NODE
        new_node.color = RED
        self._fixup_after_insert(new_node)

    def _fixup_after_insert(self, inserted_node):
        """
        Fix up RBTree by recoloring and rotating as needed to maintain 
        properties of a Red-black tree.
        """
        pass

    def _left_rotate(self, x):
        """
        Rotate the RBTree to the left.
        x is the reference node being rotated. y is x's right child node.
        Assumes x.right is not NIL_NODE.
        """
        y = x.right
        x.right = y.left 
        if y.left != NIL_NODE:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == NIL_NODE:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, x):
        """
        Rotate the RBTree to the right.
        x is the reference node being rotated. y is x's left child node.
        Assumes x.left is not NIL_NODE.
        """
        y = x.left
        x.left = y.right
        if y.right != NIL_NODE:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == NIL_NODE:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.right = x
        x.parent = y
   
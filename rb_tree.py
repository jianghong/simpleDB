BLACK = 0
RED = 1

# Nil node by default is black and the other values don't matter
NIL_NODE = Node() 

class Node:
    def __init__(self, color=BLACK, key=None, parent=None, left=None,
                 right=None):
        self.color = color
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right


class RBTree:
    def __init__(self, root=Node()):
        self.root = root

BLACK = 0
RED = 1

class Node:
    def __init__(self, color=BLACK, key=None, parent=None, left=None,
                 right=None):
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

    def left_rotate(self, x):
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

    def right_rotate(self, x):
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

if __name__ == '__main__':
    # trivial test
    tt  = RBTree()
    assert tt.root.parent == NIL_NODE

    # test passing in a node
    tt = RBTree(Node(RED, 'ex', None, None, None))
    assert tt.root.color == RED
    assert tt.root.key == 'ex'

    # test left rotation
    tt = RBTree(Node(BLACK, 0))
    node_a = Node(RED, 1)
    node_a.left = NIL_NODE
    node_a.right = NIL_NODE
    tt.root.right = node_a
    tt.left_rotate(tt.root)
    assert tt.root == node_a

    # test right rotation
    tt = RBTree(Node(BLACK, 0))
    node_a = Node(RED, 0)
    node_a.left = NIL_NODE
    node_a.right = NIL_NODE
    tt.root.left = node_a
    tt.right_rotate(tt.root)
    assert tt.root == node_a    
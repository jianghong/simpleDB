import pdb

BLACK = 0
RED = 1

def print_tree(node):
    """
    Print out tree for debugging.
    """
    if node is NIL_NODE:
        return

    print "Node key: {0}, parent key: {1}, color: {2}, left: {3}, right: {4}" \
          " value: {5}".format(
        node.key, node.parent.key, node.color, node.left.key, node.right.key,
        node.value)

    print_tree(node.left)
    print_tree(node.right)


class Node:
    def __init__(self, key=None, value=None, color=BLACK, parent=None, left=None,
                 right=None):
        self.color = color
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right
        self.value = value

# Sentinel Nil node; This node is black and the other values don't matter
NIL_NODE = Node() 


class RBTree:
    def __init__(self, root=NIL_NODE):
        self.root = root
        self.root.parent = NIL_NODE
        self.root.left = NIL_NODE
        self.root.right = NIL_NODE

    def _tree_min(self):
        """
        Return the node with min key.
        """
        walker_node = self.root
        while walker_node.left != NIL_NODE:
            walker_node = walker_node.left

        return walker_node

    def insert(self, new_node):
        """
        Insert new_node into RBTree.
        Assumes new_node.key exists.
        """
        operating_node = NIL_NODE
        walker_node = self.root
        while walker_node != NIL_NODE:
            operating_node = walker_node
            # on key collision override old node value with new_node value
            if new_node.key == walker_node.key:
                walker_node.value = new_node.value
                return
            elif new_node.key < walker_node.key:
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
        walker_node = inserted_node
        while walker_node.parent.color == RED:
            parent_node = walker_node.parent
            grandparent_node = parent_node.parent
            if parent_node == grandparent_node.left:
                uncle_node = grandparent_node.right
                if uncle_node.color == RED:
                    # walker_node's parent and uncle are both red
                    parent_node.color = BLACK
                    uncle_node.color = BLACK
                    grandparent_node.color = RED
                    walker_node = grandparent_node # walk walker_node
                else:
                    # walker_node's parent is RED, uncle is BLACK
                    if walker_node == parent_node.right:
                        walker_node = parent_node # walk walker_node
                        self._left_rotate(walker_node)
                    walker_node.parent.color = BLACK
                    walker_node.parent.parent.color = RED
                    self._right_rotate(walker_node.parent.parent)
            else:
                uncle_node = grandparent_node.left
                if uncle_node.color == RED:
                    # walker_node's parent and uncle are both red
                    parent_node.color = BLACK
                    uncle_node.color = BLACK
                    grandparent_node.color = RED
                    walker_node = grandparent_node # walk walker_node
                else:
                    # walker_node's parent is RED, uncle is BLACK
                    if walker_node == parent_node.left:
                        walker_node = parent_node # walk walker_node
                        self._right_rotate(walker_node)
                    walker_node.parent.color = BLACK
                    walker_node.parent.parent.color = RED
                    self._left_rotate(walker_node.parent.parent)                                

        self.root.color = BLACK

    def delete(self, node):
        """
        Remove node from RBTree.
        """
        pass

    def _transplant(self, subtree1, subtree2):
        """
        Replace subtree1 with subtree2 as child of subtree1's parent.
        RBTree version.
        """
        if subtree1.parent == NIL_NODE:
            self.root = subtree2
        elif subtree1 == subtree1.parent.left:
            subtree1.parent.left = subtree2
        else:
            subtree1.parent.right = subtree2
        subtree2.parent = subtree1.parent

    def _fixup_after_delete(self, deleted_node):
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
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def query(self, key):
        """
        Search and return the node with matching key.
        """
        def _query_helper(node, key):
            if node == NIL_NODE or key == node.key:
                return node
            elif key < node.key:
                return _query_helper(node.left, key)
            else:
                return _query_helper(node.right, key)

        return _query_helper(self.root, key)


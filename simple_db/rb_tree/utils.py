from rb_tree import *


def verify_properties_1_3_4(node):
    """
    1. Verify that every node in RBTree is red or black.
    3. Verify that every leaf node (NIL_NODE) is black.
    4. Verify that if a node is red, then both its children are black.
    """

    if node is NIL_NODE:
        # check property 3
        assert node.color == BLACK
        return

    # check property 1
    assert node.color == RED or node.color == BLACK

    # check property 4
    if node.color == RED:
        assert node.parent.color == BLACK

    verify_properties_1_3_4(node.left)
    verify_properties_1_3_4(node.right)


def verify_property_2(root):
    """
    Verify that the root node in RBTree is black.
    """

    assert root.color == BLACK


def verify_property_5(root):
    """
    Verify that all paths from any given node to its leaf nodes contain the 
    same number of black nodes.
    """
    def _verify_property_5_helper(node, black_count, path_black_count):
        if node.color == BLACK:
            black_count += 1

        if node == NIL_NODE:
            if path_black_count == -1:
                # finished first path, set this as comparitive
                path_black_count = black_count
            else:
                assert path_black_count == black_count
            return

        _verify_property_5_helper(node.left, black_count, path_black_count)
        _verify_property_5_helper(node.right, black_count, path_black_count)

    _verify_property_5_helper(root, 0, -1)


def verify_RB_tree_properties(RBTree, debug=False):
    """
    Utility function to verify tree holds Red-black tree properties.
    For readability I break down verification of each property into different
    functions.
    """
    verify_properties_1_3_4(RBTree.root)
    verify_property_2(RBTree.root)
    verify_property_5(RBTree.root)

    if debug:
        print_tree(RBTree.root)
        print "======================"


def insert_test_nodes_1(tt):
    tt.insert(Node(11))
    tt.insert(Node(2))
    tt.insert(Node(7))
    tt.insert(Node(14))
    tt.insert(Node(1))
    tt.insert(Node(15))
    tt.insert(Node(5))
    tt.insert(Node(8))
    tt.insert(Node(4))


def insert_test_nodes_2(tt):
    tt.insert(Node(1))
    tt.insert(Node(2))
    tt.insert(Node(3))
    tt.insert(Node(4))
    tt.insert(Node(5))
    tt.insert(Node(6))
    tt.insert(Node(7))
    tt.insert(Node(8))
    tt.insert(Node(9))

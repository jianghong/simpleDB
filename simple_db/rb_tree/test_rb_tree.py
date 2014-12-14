import unittest
from utils import *
from rb_tree import *


class RBTreeTests(unittest.TestCase):

    def setUp(self):
        self.tt = RBTree()

    def test_init(self):
        self.assertEqual(self.tt.root.parent, NIL_NODE)

    def test_init_RBTree_with_node(self):
        self.tt = RBTree(Node('ex', 1, RED))
        self.assertEqual(self.tt.root.color, RED)
        self.assertEqual(self.tt.root.key, 'ex')
        self.assertEqual(self.tt.root.value, 1)

    def test_simple_insert(self):
        node_j = Node('j')
        node_h = Node('h')
        node_k = Node('k')
        node_a = Node('a')
        node_z = Node('z')

        self.tt.insert(node_j)
        self.assertEqual(self.tt.root, node_j)
        self.tt.insert(node_h)
        self.assertEqual(self.tt.root.left, node_h)
        self.tt.insert(node_k)
        self.assertEqual(self.tt.root.right, node_k)
        self.tt.insert(node_a)
        self.assertEqual(self.tt.root.left.left, node_a)
        self.tt.insert(node_z)
        self.assertEqual(self.tt.root.right.right, node_z)

    def test_insert_and_verify(self):
        insert_test_nodes_1(self.tt)
        verify_RB_tree_properties(self.tt)

        self.tt = RBTree()
        insert_test_nodes_2(self.tt)
        verify_RB_tree_properties(self.tt)

    def test_left_rotate(self):
        self.tt = RBTree(Node(0))
        node_a = Node(1)
        self.tt.insert(node_a)
        self.tt._left_rotate(self.tt.root)
        self.assertEqual(self.tt.root, node_a)

    def test_right_rotate(self):
        self.tt = RBTree(Node(1))
        node_a = Node(0)
        self.tt.insert(node_a)
        self.tt._right_rotate(self.tt.root)
        self.assertEqual(self.tt.root, node_a)

    def test_query(self):
        self.tt = RBTree(Node(1, 'k'))
        self.assertEqual(self.tt.query(1).value, 'k')

        self.tt.insert(Node(1))
        self.tt.insert(Node(2))
        self.tt.insert(Node(3))
        self.tt.insert(Node(4))
        self.tt.insert(Node(5, 'b'))
        self.tt.insert(Node(6))
        self.tt.insert(Node(7))
        self.tt.insert(Node(8))
        self.tt.insert(Node(9))
        self.assertEqual(self.tt.query(5).value, 'b')
        self.assertEqual(self.tt.query('not exist').value, None)
        self.assertEqual(self.tt.query('not exist'), NIL_NODE)

    def test_key_collision(self):
        self.tt = RBTree(Node('a', 1))
        self.assertEqual(self.tt.query('a').value, 1)

        self.tt.insert(Node('a', 5))
        self.assertEqual(self.tt.query('a').value, 5)

        self.assertEqual(self.tt.root.value, 5)
        self.assertEqual(self.tt.root.left, NIL_NODE)
        self.assertEqual(self.tt.root.right, NIL_NODE)

    def test_transplant(self):
        self.tt.insert(Node(2))
        self.tt.insert(Node(3))
        self.tt._transplant(self.tt.query(2), self.tt.query(3))
        self.assertEqual(self.tt.root.key, 3)
        self.assertEqual(self.tt.query(2), NIL_NODE)

        self.tt = RBTree()
        self.tt.insert(Node(2))
        self.tt.insert(Node(3))
        self.tt.insert(Node(1))
        self.tt._transplant(self.tt.query(1), self.tt.query(3))
        self.assertEqual(self.tt.root.left.key, 3)
        self.assertEqual(self.tt.query(1), NIL_NODE)

        self.tt = RBTree()
        self.tt.insert(Node(2))
        self.tt.insert(Node(3))
        self.tt.insert(Node(1))
        self.tt._transplant(self.tt.query(3), self.tt.query(1))
        self.assertEqual(self.tt.root.left.key, 1)
        self.assertEqual(self.tt.query(3), NIL_NODE)

    def test_tree_min(self):
        insert_test_nodes_1(self.tt)
        self.assertEqual(self.tt._tree_min(self.tt.root).key, 1)

    def test_simple_delete(self):
        insert_test_nodes_1(self.tt)
        self.tt.delete(self.tt.query(5))
        self.assertEqual(self.tt.query(5), NIL_NODE)
        self.tt.delete(self.tt.query(14))
        self.assertEqual(self.tt.query(14), NIL_NODE)

    def test_delete_and_verify(self):
        insert_test_nodes_1(self.tt)
        self.tt.delete(self.tt.query(5))
        self.assertEqual(self.tt.query(5), NIL_NODE)
        verify_RB_tree_properties(self.tt)
        self.tt.delete(self.tt.query(14))
        self.assertEqual(self.tt.query(14), NIL_NODE)
        verify_RB_tree_properties(self.tt)

        self.tt = RBTree()
        insert_test_nodes_2(self.tt)
        self.tt.delete(self.tt.query(4))
        self.assertEqual(self.tt.query(4), NIL_NODE)
        verify_RB_tree_properties(self.tt)
        self.tt.delete(self.tt.query(8))
        self.assertEqual(self.tt.query(8), NIL_NODE)
        verify_RB_tree_properties(self.tt)

if __name__ == '__main__':
    unittest.main()

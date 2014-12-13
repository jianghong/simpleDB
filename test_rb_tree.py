from rb_tree import *

if __name__ == '__main__':
    # trivial test
    tt  = RBTree()
    assert tt.root.parent == NIL_NODE

    # test passing in a node
    tt = RBTree(Node('ex', None, None, None, RED))
    assert tt.root.color == RED
    assert tt.root.key == 'ex'

    # test insert
    tt = RBTree(Node('j'))
    node_h = Node('h')
    tt.insert(node_h)
    assert tt.root.left == node_h
    node_k = Node('k')
    tt.insert(node_k)
    assert tt.root.right == node_k
    node_a = Node('a')
    tt.insert(node_a)
    assert tt.root.left.left == node_a
    node_z = Node('z')
    tt.insert(node_z)
    assert tt.root.right.right == node_z

    # test left rotation
    tt = RBTree(Node(0))
    node_a = Node(1)
    tt.insert(node_a)
    tt._left_rotate(tt.root)
    assert tt.root == node_a

    # test right rotation
    tt = RBTree(Node(1))
    node_a = Node(0)
    tt.insert(node_a)
    tt._right_rotate(tt.root)
    assert tt.root == node_a 
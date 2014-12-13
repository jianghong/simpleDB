from rb_tree.rb_tree import *

"""
SimpleDB is a simple database similar to redis. The underlying data structure
is a Red-black tree.

Supported operations:
    Data Commands
    =============
    - SET [name] [value]: Set the variable [name] to the value [value].

    - GET [name]: Print out the value of the variable [name]. 
                  NULL if that variable is not set.

    - UNSET [name]

    - NUMEQUALTO [value]

    - END: Exit the program.

    Transaction Commands
    =====================
    - BEGIN
    - ROLLBACK
    - COMMIT
"""
class SimpleDB:
    def __init__(self):
        self.data_structure = RBTree()

    def set(self, key, value):
        """
        Set key to value in data_structure.
        """
        new_node = Node(key, value)
        self.data_structure.insert(new_node)

    def get(self, key):
        """
        Return value of matching key from data_structure.
        """
        return self.data_structure.query(key)


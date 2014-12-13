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

    - UNSET [name]: Unset the variable [name],
                    making it just like that variable was never set.

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

    def unset(self, key):
        """
        Unset matching key in data_structure if it exists.
        """
        to_delete = self.get(key)
        if to_delete != NIL_NODE:
            self.data_structure.delete(to_delete)


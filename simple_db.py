from rb_tree import RBTree

"""
SimpleDB is a simple database similar to redis. The underlying data structure
is a Red-black tree.

Supported operations:
    Data Commands
    =============
    - SET [name] [value]
    - GET [name]
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
        pass

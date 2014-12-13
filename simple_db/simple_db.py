"""
SimpleDB is a simple database similar to redis. The underlying data structure
is a python dictionary

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
        self.data_structure = {}

    def set(self, key, value):
        """
        Set key to value in data_structure.
        """
        self.data_structure[key] = value

    def get(self, key):
        """
        Return value of matching key from data_structure.
        """
        return self.data_structure.get(key, None)

    def unset(self, key):
        """
        Unset matching key in data_structure if it exists.
        """
        self.data_structure.pop(key, None)


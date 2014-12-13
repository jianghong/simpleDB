from collections import defaultdict
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

    - NUMEQUALTO [value]: Print out the number of variables that are currently
                          set to [value]. 
                          If no variables equal that [value], prints 0.

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
        self.value_count = defaultdict(int)

    def _decr_value_count(self, key):
        """
        Decrement value count for value at key.
        """
        old_value = self.get(key)
        if old_value:
            self.value_count[old_value] = max(0, self.value_count[old_value] - 1)

    def _incr_value_count(self, value):
        """
        Increment value count.
        """
        self.value_count[value] += 1

    def set(self, key, value):
        """
        Set key to value in data_structure.
        """
        # on every set decrease value count stored at key if exists
        # this is in case of a reset of an existing key
        self._decr_value_count(key)
        self._incr_value_count(value)
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
        self._decr_value_count(key)
        self.data_structure.pop(key, None)

    def numequalto(self, value):
        """
        Return the number of times value appears in DB.
        """
        return self.value_count[value]

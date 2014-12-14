from collections import defaultdict
from data_structures.rb_tree import *
from data_structures.hash_table import *

SimpleDB_docstring = """
SimpleDB is a simple database similar to redis.

Supported operations:
    Data Commands
    =============
    - SET [name] [value]: Set the variable [name] to the value [value].
      Example: > SET x 10

    - GET [name]: Print out the value of the variable [name]. 
                  NULL if that variable is not set.
      Example: > GET x
                10

    - UNSET [name]: Unset the variable [name],
                    making it just like that variable was never set.
      Example: > UNSET x

    - NUMEQUALTO [value]: Print out the number of variables that are currently
                          set to [value]. 
                          If no variables equal that [value], prints 0.
      Example: > SET x 10
               > NUMEQUALTO 10
                1

    - END: Exit the program.

    Transaction Commands
    =====================
    - BEGIN: Open a new transaction block. 
             Transaction blocks can be nested;
             a BEGIN can be issued inside of an existing block.
      
    - ROLLBACK: Undo all of the commands issued in the most 
                recent transaction block, and close the block. 

    - COMMIT: Close all open transaction blocks, 
              permanently applying the changes made in them.

    Example: > BEGIN
             > SET a 10
             > GET a
              10
             > BEGIN
             > SET a 20
             > GET a
              20
             > ROLLBACK
             > GET a
              10
             > ROLLBACK
             > GET a
              NULL


"""


class SimpleDB:

    def __init__(self, rb_tree=False):
        if rb_tree:
            self.data_structure = RBTree()
        else:
            self.data_structure = HashTable()

        self.rb_tree = rb_tree
        self.value_count = defaultdict(int)
        self.transaction_stack = []
        self.open_transactions = False

    def _decr_value_count(self, key):
        """
        Decrement value count for value at key.
        """
        old_value = self.get(key)
        if old_value:
            self.value_count[old_value] = max(
                0, self.value_count[old_value] - 1)

    def _incr_value_count(self, value):
        """
        Increment value count.
        """
        self.value_count[value] += 1

    def _store_previous_state(self, key):
        """
        Store previous state of key in most recent transaction in
        transaction_stack.
        """
        previous_state_store = self.transaction_stack[-1]
        old_key_state = previous_state_store.get(key, None)
        if not old_key_state:
            previous_state_store[key] = self.get(key)

    def set(self, key, value):
        """
        Set key to value in data_structure.
        """

        if self.open_transactions:
            self._store_previous_state(key)

        # on every set decrease value count stored at key if exists
        # this is in case of a reset of an existing key
        self._decr_value_count(key)
        self._incr_value_count(value)
        self.data_structure.insert(key, value)

    def get(self, key):
        """
        Return value of matching key from data_structure.
        """
        if self.rb_tree:
            return self.data_structure.query(key).value
        else:
            return self.data_structure.query(key)

    def unset(self, key):
        """
        Unset matching key in data_structure if it exists.
        """
        key_check = self.get(key)
        if not key_check:
            return

        if self.open_transactions:
            self._store_previous_state(key)

        self._decr_value_count(key)

        to_delete = self.data_structure.query(key)
        if to_delete is not None:
            self.data_structure.delete(key)

    def numequalto(self, value):
        """
        Return the number of times value appears in DB.
        """
        return self.value_count[value]

    def begin(self):
        """
        Begin a new transaction.
        """
        self.transaction_stack.append({})
        self.open_transactions = True

    def rollback(self):
        """
        Rollback transformation commands in current transaction and close 
        transaction.
        """
        if self.transaction_stack:
            previous_state = self.transaction_stack.pop()
            # temporarily set this to False so states don't get stored
            self.open_transactions = False
            for key, value in previous_state.iteritems():
                if value:
                    self.set(key, value)
                else:
                    self.unset(key)

            self.open_transactions = bool(self.transaction_stack)
        else:
            print 'NO TRANSACTION'

    def commit(self):
        """
        Commit all open transactions and close them.
        Due to implementation, changes are saved at this point and just
        need to close transactions.
        """
        if self.transaction_stack:
            self.transaction_stack = []
        else:
            print 'NO TRANSACTION'

        self.open_transactions = False

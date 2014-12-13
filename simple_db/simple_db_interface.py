import sys
from simple_db import SimpleDB

"""
SimpleDBInterface is the interface that the user will use to interact with 
SimpleDB. Details on implementation are in simple_db.py

Supported operations:
    Data Commands
    =============
    - SET [name] [value]
    - GET [name]
    - UNSET [name]
    - NUMEQUALTO [value]
    - END

    Transaction Commands
    =====================
    - BEGIN
    - ROLLBACK
    - COMMIT
"""
class SimpleDBInterface:
    def __init__(self):
        self.db = SimpleDB()
        self._prompt_for_cmd()
        self.line = sys.stdin.readline()
        self.start()

    def _prompt_for_cmd(self):
        """Convenience function to print a prompt for the user."""
        print '> ',

    def _handle_cmd(self, cmd, args):
        """
        Handle the command and args received from stdin. Main entry point into 
        SimpleDB.
        """

        # chain of ifs instead of dict style for simplicity
        if cmd == 'get':
            self._handle_get(args)
        elif cmd == 'set':
            self._handle_set(args)
        elif cmd == 'unset':
            pass
        elif cmd == 'numequalto':
            pass
        elif cmd == 'begin':
            pass
        elif cmd == 'rollback':
            pass
        elif cmd == 'commit':
            pass
        elif cmd == 'end':
            self._handle_end()
        else:
            print 'UNRECOGNIZED COMMAND'

    def _handle_set(self, args):
        if self._bad_args(args, 2):
            print 'USAGE: SET [name] [value]. 2 parameters only.'
        else:
            key = args[0]
            value = args[1]
            self.db.set(key, value)
            print ''

    def _handle_get(self, args):
        if self._bad_args(args, 1):
            print 'USAGE: GET [name]. 1 parameter only.'
        else:
            key = args[0]
            value = self.db.get(key).value 
            print value if value else 'NULL'

    def _handle_end(self):
        print 'ENDING SIMPLEDB'
        sys.exit()

    def _bad_args(self, args, num_required):
        if len(args) != num_required:
            print 'ERROR: Incorect number of arguments.'
            return True

    def _sanitize(self, target):
        """Clean up target by lowercasing target and stripping whitespace."""
        return target.lower().strip()


    def start(self):
        """Start SimpleDBInterface and receive commands from stdin."""
        while self.line:
            split_line = self._sanitize(self.line).split(' ')
            self._handle_cmd(split_line[0], split_line[1:])
            self._prompt_for_cmd()
            self.line = sys.stdin.readline()

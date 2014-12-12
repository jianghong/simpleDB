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
            pass
        elif cmd == 'set':
            pass
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
            print 'ENDING SIMPLEDB'
            sys.exit()
        else:
            print 'UNRECOGNIZED COMMAND'

    def _sanitize(self, target):
        """Clean up target by lowercasing cmd and stripping whitespace."""
        return target.lower().strip()


    def start(self):
        """Start SimpleDBInterface and receive commands from stdin."""
        while self.line:
            split_line = self._sanitize(self.line).split(' ')
            self._handle_cmd(split_line[0], split_line[1:])
            self._prompt_for_cmd()
            self.line = sys.stdin.readline()

import sys
from simple_db import SimpleDB

"""
SimpleDBInterface is the interface that the user will use to interact with 
SimpleDB. Details on implementation are in simple_db.py

Supported operations:
    Data Commands
    =============
    - GET
    - SET
    - UNSET
    - NUMEQUALTO
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
        self._cmd = sys.stdin.readline()
        self.start()

    def _prompt_for_cmd(self):
        """Convenience function to print a prompt for the user."""
        print '> ',

    def _handle_cmd(self):
        """
        Handle the command received from stdin. Main entry point into 
        SimpleDB.
        """
        self._sanitize_cmd()

        if self._cmd == 'end':
            print 'ENDING SIMPLEDB'
            sys.exit()
        else:
            print 'UNRECOGNIZED COMMAND'

    def _sanitize_cmd(self):
        """Clean up cmd by lowercasing cmd and stripping whitespace."""
        self._cmd = self._cmd.lower().strip()


    def start(self):
        """Start SimpleDBInterface and receive commands from stdin."""
        while self._cmd:
            self._handle_cmd()
            self._prompt_for_cmd()
            self._cmd = sys.stdin.readline()

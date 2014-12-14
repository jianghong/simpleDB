import sys
from simple_db import SimpleDB, SimpleDB_docstring

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

    def __init__(self, use_rb_tree=None):
        if use_rb_tree == 'use_rb_tree':
            self.db = SimpleDB(rb_tree=True)
            print 'Using red-black tree.'
        else:
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

        cmd = self._sanitize(cmd)

        # chain of ifs instead of dict style for simplicity
        if cmd == 'get':
            self._handle_get(args)
        elif cmd == 'set':
            self._handle_set(args)
        elif cmd == 'unset':
            self._handle_unset(args)
        elif cmd == 'numequalto':
            self._handle_numequalto(args)
        elif cmd == 'begin':
            self._handle_begin(args)
        elif cmd == 'rollback':
            self._handle_rollback(args)
        elif cmd == 'commit':
            self._handle_commit(args)
        elif cmd == 'end':
            self._handle_end(args)
        elif cmd == 'help':
            self._handle_help(args)
        else:
            print 'UNRECOGNIZED COMMAND'

    def _handle_get(self, args):
        if self._bad_args(args, 1):
            print 'USAGE: GET [name]. 1 parameter only.'
        else:
            key = args[0]
            value = self.db.get(key)
            print value if value else 'NULL'

    def _handle_set(self, args):
        if self._bad_args(args, 2):
            print 'USAGE: SET [name] [value]. 2 parameters only.'
        else:
            key = args[0]
            value = args[1]
            self.db.set(key, value)
            print ''

    def _handle_unset(self, args):
        if self._bad_args(args, 1):
            print 'USAGE: UNSET [name]. 1 parameter only.'
        else:
            key = args[0]
            self.db.unset(key)
            print ''

    def _handle_numequalto(self, args):
        if self._bad_args(args, 1):
            print 'USAGE: NUMEQUALTO [value]. 1 parameter only.'
        else:
            value = args[0]
            print self.db.numequalto(value)

    def _handle_begin(self, args):
        if self._bad_args(args, 0):
            print 'USAGE: BEGIN. No parameters required.'
        else:
            self.db.begin()
            print ''

    def _handle_rollback(self, args):
        if self._bad_args(args, 0):
            print 'USAGE: ROLLBACK. No parameters required.'
        else:
            self.db.rollback()
            print ''

    def _handle_commit(self, args):
        if self._bad_args(args, 0):
            print 'USAGE: COMMIT. No parameters required.'
        else:
            self.db.commit()

    def _handle_end(self, args):
        if self._bad_args(args, 0):
            print 'USAGE: END. No parameters required.'
        else:
            sys.exit()

    def _handle_help(self, args):
        if self._bad_args(args, 0):
            print 'USAGE: HELP. No parameters required.'
        else:
            print SimpleDB_docstring

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
            split_line = self.line.strip().split(' ')
            self._handle_cmd(split_line[0], split_line[1:])
            self._prompt_for_cmd()
            self.line = sys.stdin.readline()

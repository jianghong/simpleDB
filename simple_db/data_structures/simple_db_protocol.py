"""
Protocol that data structures have to adhere to to be used by SimpleDB.
"""


class SimpleDBProtocol:

    def __init__(self):
        pass

    def insert(self):
        """
        Required to support set
        """
        pass

    def delete(self):
        """
        Required to support unset.
        """
        pass

    def query(self):
        """
        Required to support get.
        """
        pass

from simple_db_protocol import SimpleDBProtocol


class HashTable(SimpleDBProtocol):

    def __init__(self):
        self.hashtable = {}

    def insert(self, key, value):
        """
        Required to support set
        """
        self.hashtable[key] = value

    def delete(self, key):
        """
        Required to support unset.
        """
        self.hashtable.pop(key, None)

    def query(self, key):
        """
        Required to support get.
        """
        return self.hashtable.get(key, None)

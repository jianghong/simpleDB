import unittest
import time
import random
from simple_db import SimpleDB


class PerformanceTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.db = SimpleDB()
        cls.n = 100000
        for i in xrange(cls.n):
            cls.db.set(i, i)

    def test_set(self):
        """
        Test set performance.
        """
        t0 = time.time()
        self.db.set('+1', 'yay')
        print "Time to set a key in a db of size {0}: {1}".format(self.n, time.time() - t0)

    def test_get(self):
        """
        Test set performance.
        """
        t0 = time.time()
        k = random.randint(0, self.n)
        self.db.get(k)
        print "Time to get a random key in a db of size {0}: {1}".format(self.n, time.time() - t0)

    def test_unset(self):
        """
        Test unset performance.
        """
        t0 = time.time()
        k = random.randint(0, self.n)
        self.db.unset(k)
        print "Time to unset a random key in a db of size {0}: {1}".format(self.n, time.time() - t0)

if __name__ == '__main__':
    unittest.main()

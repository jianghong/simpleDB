import timeit
from simple_db.simple_db import SimpleDB

def test_set():
    """
    Test insert performance.
    """
    db = SimpleDB()
    for i in xrange(8):
        db.set(i, i)

if __name__ == '__main__':
    print(timeit.timeit("test_set()", setup="from __main__ import test_set"))
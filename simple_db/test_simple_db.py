import unittest
from simple_db import SimpleDB

class SimpleDBTests(unittest.TestCase):

    def setUp(self):
        self.db = SimpleDB()


    def test_basic_data_cmds_1(self):
        self.db.set('ex', 10)
        self.assertEqual(self.db.get('ex'), 10)

        self.db.unset('ex')
        self.assertEqual(self.db.get('ex'), None)

    def test_basic_data_cmds_2(self):
        self.db.set('a', 10)
        self.db.set('b', 10)
        self.assertEqual(self.db.numequalto(10), 2)
        self.db.set('b', 30)
        self.assertEqual(self.db.numequalto(10), 1)

    def test_transaction_cmds_1(self):
        self.db.begin()
        self.db.set('a', 10)
        self.assertEqual(self.db.get('a'), 10)
        self.db.begin()
        self.db.set('a', 20) 
        self.assertEqual(self.db.get('a'), 20)
        self.db.rollback()
        self.assertEqual(self.db.get('a'), 10)
        self.db.rollback()
        self.assertEqual(self.db.get('a'), None)

    def test_transaction_cmds_2(self):
        self.db.begin()
        self.db.set('a', 30) 
        self.db.begin()
        self.db.set('a', 40)
        self.db.commit()
        self.assertEqual(self.db.get('a'), 40)
        self.db.rollback()
        self.assertEqual(self.db.get('a'), 40)

    def test_transaction_cmds_3(self):
        self.db.set('a', 50)
        self.db.begin()
        self.assertEqual(self.db.get('a'), 50)
        self.db.set('a', 60)
        self.db.begin()
        self.db.unset('a')
        self.assertEqual(self.db.get('a'), None)
        self.db.rollback()
        self.assertEqual(self.db.get('a'), 60)
        self.db.commit()
        self.assertEqual(self.db.get('a'), 60)

    def test_transaction_cmds_4(self):
        self.db.set('a', 10)
        self.db.begin()
        self.assertEqual(self.db.numequalto(10), 1)
        self.db.begin()
        self.db.unset('a')
        self.assertEqual(self.db.numequalto(10), 0)
        self.db.rollback()
        self.assertEqual(self.db.numequalto(10), 1)
        self.db.commit()
        self.assertEqual(self.db.numequalto(10), 1)
   
if __name__ == '__main__':
    unittest.main()
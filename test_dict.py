import unittest

class TestDictEqualityForKeys(unittest.TestCase):
    a = {'foo': 'bar'}
    b = {u'foo': 'bar'}
    
    def test_using_equals(self):
        self.assertTrue(self.a == self.b)

    def test_using_assertEqual(self):
        self.assertEqual(self.a, self.b)

class TestDictEqualityForValues(unittest.TestCase):
    a = {'foo': u'bar'}
    b = {'foo': 'bar'}
    
    def test_using_equals(self):
        self.assertTrue(self.a == self.b)

    def test_using_assertEqual(self):
        self.assertEqual(self.a, self.b)

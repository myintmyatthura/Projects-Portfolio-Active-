"""
    Unit test for ASet, implemented via inheritance from TestSet.
"""
from test_set import *
from aset import *


class TestASet(TestSet):

    @classmethod
    def setUpClass(cls):
        cls.SetType = ASet

    def test_is_full(self):
        capacity = 10
        s = self.SetType(capacity)
        for i in range(capacity):
            self.assertFalse(s.is_full())
            s.add(i)
        self.assertTrue(s.is_full())

    def test_add_exception(self):
        capacity = 10
        s = self.SetType(capacity)

        try:
            for i in range(capacity):
                s.add(i)
        except Exception as e:
            self.fail("Exception \"{}\" should not have been raised.".format(e))

        with self.assertRaises(Exception):
            s.add(capacity)


if __name__ == '__main__':
    testtorun = TestASet()
    suite = unittest.TestLoader().loadTestsFromModule(testtorun)
    unittest.TextTestRunner().run(suite)

"""
Tests basic functionality of the hash table methods, such as statistics.
"""

from hash_table import LinearProbeTable
import unittest

__author__ = "Jackson Goerner"

FIX_TABLESIZE = 19

def silly_hash(key):
    return (ord(key[0]) % FIX_TABLESIZE)

class TestHashTable(unittest.TestCase):
    """ Testing Hash Table functionality. """
    
    def test_initialisation(self):
        table = LinearProbeTable(10, tablesize_override=FIX_TABLESIZE)
        table.hash = silly_hash
        for name in "Eva, Amy, Tim, Ron, Jan, Kim, Dot, Ann, Jim, Jon".split(", "):
            table[name] = name + "-value"
        conflict, probe_total, probe_max, rehash = table.statistics()
        self.assertEqual(conflict, 4)     # Tim, Ann, Jim, Jon
        self.assertEqual(probe_total, 8)  # Tim: 1, Ann: 2, Jim: 2, Jon: 3
        self.assertEqual(probe_max, 3)    # Jon: 3
        self.assertEqual(rehash, 0)       # No rehash
        
        self.assertEqual(table["Tim"], "Tim-value")
        
        self.assertRaises(KeyError, lambda: table["Joe"])

    def test_rehash(self):
        table = LinearProbeTable(10, tablesize_override=FIX_TABLESIZE)
        table.hash = silly_hash
        for name in "Eva, Amy, Tim, Ron, Jan, Kim, Dot, Ann, Jim, Jon".split(", "):
            table[name] = name + "-value"
        # Rehash should be checked before the item is actually inserted - So the 10th/19th insert doesn't trigger.
        self.assertEqual(len(table.table), FIX_TABLESIZE, "Table rehashing too early.")
        table["Joe"] = "Joe-value"
        # But the 11th/19th does.
        self.assertGreater(len(table.table), FIX_TABLESIZE, "Table not being rehashed.")
        
        conflict, probe_total, probe_max, rehash = table.statistics()
        self.assertGreaterEqual(conflict, 4)     # Tim, Ann, Jim, Jon + Whatever rehash caused
        self.assertGreaterEqual(probe_total, 8)  # Tim: 1, Ann: 2, Jim: 2, Jon: 3  + Whatever rehash caused
        self.assertGreaterEqual(probe_max, 3)    # Jon: 3  + Whatever rehash caused
        self.assertEqual(rehash, 1)              # 1 rehash

if __name__ == '__main__':

    # running all the tests
    unittest.main()

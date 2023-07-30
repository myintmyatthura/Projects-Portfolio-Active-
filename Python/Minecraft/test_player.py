from random_gen import RandomGen
from player import Player
import unittest


class TestPlayer(unittest.TestCase):
    """ Testing additional AVL functionality. """

    def setUp(self):
        pass

    def test_init(self):
        # checking a valid player being created
        try:
            _ = Player("Enderman", 10)
        except Exception:
            raise AssertionError("Unable to instantiate player with correct inputs")


if __name__ == '__main__':
    # seeding the pseudo-random generator
    RandomGen.set_seed(16)

    # running all the tests
    unittest.main()

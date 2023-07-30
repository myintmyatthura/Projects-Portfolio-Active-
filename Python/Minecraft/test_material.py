from random_gen import RandomGen
from material import Material
import unittest


class TestMaterial(unittest.TestCase):
    """ Testing additional AVL functionality. """

    def setUp(self):
        pass

    def test_init(self):
        # checking a valid player being created
        try:
            _ = Material("Carrot on a Stick", 32.5)
        except Exception:
            raise AssertionError("Unable to instantiate material with correct inputs")


if __name__ == '__main__':
    # seeding the pseudo-random generator
    RandomGen.set_seed(16)

    # running all the tests
    unittest.main()

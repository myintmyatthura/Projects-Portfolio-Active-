from random_gen import RandomGen
from trader import RandomTrader, RangeTrader, HardTrader
from material import Material
import unittest


class TestTraders(unittest.TestCase):
    """ Testing additional AVL functionality. """

    def setUp(self):
        pass

    def test_material_methods(self):
        t = RandomTrader.random_trader()
        a, b, c = [
            Material("Arrow", 1),
            Material("Axe", 2),
            Material("Bow", 3),
        ]
        t.set_all_materials([a, b])
        self.assertFalse(t.is_currently_selling())
        # Make a deal. The material in the deal should be either a or b.
        t.generate_deal()
        self.assertTrue(t.is_currently_selling())
        self.assertIn(t.current_deal()[0], [a, b])
        t.add_material(c)
        # Now the trader has access to a, b and c.
        t.generate_deal()
        self.assertTrue(t.is_currently_selling())
        self.assertIn(t.current_deal()[0], [a, b, c])
        t.stop_deal()
        self.assertFalse(t.is_currently_selling())
        t.set_all_materials([a])
        # This resets the traders inventory to just a.
        t.generate_deal()
        self.assertTrue(t.is_currently_selling())
        self.assertIn(t.current_deal()[0], [a])
        t.add_material(c)
        # And now we have access to a and c.
        t.generate_deal()
        self.assertTrue(t.is_currently_selling())
        self.assertIn(t.current_deal()[0], [a, c])

    def test_init(self):
        # checking a valid random trader being created
        try:
            _ = RandomTrader("Bertie Combs")
        except Exception:
            raise AssertionError("Unable to instantiate RandomTrader with correct inputs")

        # Checking if a valid range trader is being created

        try:
            _ = RangeTrader("Lyle Randall")
        except Exception:
            raise AssertionError("Unable to instantiate RangeTrader with correct inputs")

        # Checking if a valid hard trader is being created

        try:
            _ = HardTrader("Dana Rowland")
        except Exception:
            raise AssertionError("Unable to instantiate HardTrader with correct inputs")

    def test_random_str(self):
        # Set random seed
        RandomGen.set_seed(16)

        # Create a random trader and add some materials
        rando = RandomTrader("Mr Barnes")
        rando.add_material(Material("Amethyst", 1))
        rando.add_material(Material("Emerald", 2))
        rando.add_material(Material("Ruby", 3))
        rando.add_material(Material("Diamond", 4))
        rando.add_material(Material("Arrow", 5))
        rando.add_material(Material("Clock", 6))
        rando.add_material(Material("Pickaxe", 7))
        rando.add_material(Material("Gunpowder", 8))

        # Check what is being currently sold; should raise an error
        with self.assertRaises(ValueError):
            _ = rando.current_deal()

        # Now, generate a deal
        rando.generate_deal()

        # check that the deal matches
        # If you get 2.01 here, try swapping the generation of material choice and sell price.
        self.assertEqual(str(rando), "<RandomTrader: Mr Barnes buying [Pickaxe: 7🍗/💎] for 7.57💰>", "Deal check failed")

    def test_range_str(self):
        RandomGen.set_seed(16)

        # Create a random trader and add some materials
        rando = RangeTrader("Mr Barnes")
        rando.add_material(Material("Amethyst", 1))
        rando.add_material(Material("Emerald", 2))
        rando.add_material(Material("Ruby", 3))
        rando.add_material(Material("Diamond", 4))
        rando.add_material(Material("Arrow", 5))
        rando.add_material(Material("Clock", 6))
        rando.add_material(Material("Pickaxe", 7))
        rando.add_material(Material("Gunpowder", 8))

        # Check what is being currently sold; should raise an error
        with self.assertRaises(ValueError):
            _ = rando.current_deal()

        # Now, generate a deal
        rando.generate_deal()

        # check that the deal matches
        self.assertEqual(str(rando), "<RangeTrader: Mr Barnes buying [Pickaxe: 7🍗/💎] for 4.87💰>", "Deal check failed")

    def test_range_materials_between(self):
        RandomGen.set_seed(16)

        # Create a random trader and add some materials
        rando = RangeTrader("Mr Barnes")
        rando.add_material(Material("Amethyst", 1))
        rando.add_material(Material("Emerald", 2))
        rando.add_material(Material("Ruby", 3))
        rando.add_material(Material("Diamond", 4))
        rando.add_material(Material("Arrow", 5))
        rando.add_material(Material("Clock", 6))
        rando.add_material(Material("Pickaxe", 7))
        rando.add_material(Material("Gunpowder", 8))

        # Check materials between method validity
        expected_list = [Material("Emerald", 2), Material("Ruby", 3), Material("Diamond", 4)]
        expected_str = [str(x) for x in expected_list]
        your_list = rando.materials_between(1, 3)
        your_str = [str(x) for x in your_list]
        self.assertEqual(your_str, expected_str, "Strings of materials between do not match")

    def test_hard_str(self):
        RandomGen.set_seed(16)

        # Create a random trader and add some materials
        rando = HardTrader("Mr Barnes")
        rando.add_material(Material("Amethyst", 1))
        rando.add_material(Material("Emerald", 2))
        rando.add_material(Material("Ruby", 3))
        rando.add_material(Material("Diamond", 4))
        rando.add_material(Material("Arrow", 5))
        rando.add_material(Material("Clock", 6))
        rando.add_material(Material("Pickaxe", 7))
        rando.add_material(Material("Gunpowder", 8))

        # Check what is being currently sold; should raise an error
        with self.assertRaises(ValueError):
            _ = rando.current_deal()

        # Now, generate a deal
        rando.generate_deal()

        # check that the deal matches
        self.assertEqual(str(rando), "<HardTrader: Mr Barnes buying [Gunpowder: 8🍗/💎] for 2.01💰>", "Deal check failed")


if __name__ == '__main__':
    # seeding the pseudo-random generator
    RandomGen.set_seed(16)

    # running all the tests
    unittest.main()

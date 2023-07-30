from food import Food
from game import MultiplayerGame, SoloGame
from player import PLAYER_NAMES, Player
from random_gen import RandomGen
from cave import Cave
from trader import HardTrader, RandomTrader, RangeTrader
from material import Material
import unittest


class TestGame(unittest.TestCase):
    """ Testing Game functionality. """

    def test_example(self):
        RandomGen.set_seed(16)
        
        gold = Material("Gold Nugget", 27.24)
        netherite = Material("Netherite Ingot", 20.95)
        fishing_rod = Material("Fishing Rod", 26.93)
        ender_pearl = Material("Ender Pearl", 13.91)
        prismarine = Material("Prismarine Crystal", 11.48)

        materials = [
            gold,
            netherite,
            fishing_rod,
            ender_pearl,
            prismarine,
        ]

        caves = [
            Cave("Boulderfall Cave", prismarine, 10),
            Cave("Castle Karstaag Ruins", netherite, 4),
            Cave("Glacial Cave", gold, 3),
            Cave("Orotheim", fishing_rod, 6),
            Cave("Red Eagle Redoubt", fishing_rod, 3),
        ]

        waldo = RandomTrader("Waldo Morgan")
        waldo.add_material(fishing_rod)     # Now selling for 7.57
        orson = RandomTrader("Orson Hoover")
        orson.add_material(gold)            # Now selling for 4.87
        lea = RandomTrader("Lea Carpenter")
        lea.add_material(prismarine)        # Now selling for 5.65
        ruby = RandomTrader("Ruby Goodman")
        ruby.add_material(netherite)        # Now selling for 8.54
        mable = RandomTrader("Mable Hodge")
        mable.add_material(gold)            # Now selling for 6.7
        
        traders = [
            waldo,
            orson,
            lea,
            ruby,
            mable,
        ]
        
        for trader in traders:
            trader.generate_deal()

        g = SoloGame()
        g.initialise_with_data(materials, caves, traders, ["Jackson"], [50])

        # Avoid simulate_day - This regenerates trader deals and foods.
        foods = [
            Food("Cabbage Seeds", 106, 30),
            Food("Fried Rice", 129, 24),
            Food("Cooked Chicken Cuts", 424, 19),
        ]

        g.player.set_foods(foods)
        food, balance, caves = g.player.select_food_and_caves()
        
        self.assertGreaterEqual(balance, 185.01974749350165 - pow(10, -4))
        # Actual tests will also check your output is possible.

    def test_generation(self):
        RandomGen.set_seed(1234)
        g = SoloGame()
        g.initialise_game()
        # Spend some time in minecraft
        # Note that this will crash if you generate a HardTrader with less than 3 materials.
        for _ in range(3):
            g.simulate_day()
            g.finish_day()
    
    def test_unique(self):
        RandomGen.set_seed(1239087123)
        g = SoloGame()
        g.initialise_game()
        # I'm going to assume you have a `name` attribute on the Materials.
        self.assertEqual(len(set(map(lambda m: m.name, g.get_materials()))), len(g.get_materials()))
        # Same deal with caves
        self.assertEqual(len(set(map(lambda c: c.name, g.get_caves()))), len(g.get_caves()))
        # and Traders
        self.assertEqual(len(set(map(lambda t: t.name, g.get_traders()))), len(g.get_traders()))
    
    def test_multiplayer(self):
        RandomGen.set_seed(1234)
        materials = [
            Material.random_material()
            for _ in range(400)
        ]
        mat_set = set()
        mining_set = set()
        materials = list(filter(lambda x: (x.name not in mat_set and x.mining_rate not in mining_set) and (mat_set.add(x.name) or mining_set.add(x.mining_rate)) is None, materials))
        caves = [
            Cave.random_cave(materials)
            for _ in range(400)
        ]
        cave_set = set()
        caves = list(filter(lambda x: x.name not in cave_set and cave_set.add(x.name) is None, caves))        
        traders = [
            RandomGen.random_choice([RangeTrader, RandomTrader]).random_trader()
            for _ in range(50)
        ]
        trade_set = set()
        traders = list(filter(lambda x: x.name not in trade_set and trade_set.add(x.name) is None, traders))
        for trader in traders:
            trader.set_all_materials(materials)
        players = [
            RandomGen.random_choice(PLAYER_NAMES)
            for _ in range(20)
        ]
        balances = [
            RandomGen.randint(20, 100)
            for _ in range(20)
        ]
        RandomGen.set_seed(12345)
        g = MultiplayerGame()
        g.initialise_with_data(
            materials,
            caves,
            traders,
            players,
            balances,
        )
        
        # Live a year in minecraft
        for _ in range(365):
            g.simulate_day()
            g.finish_day()

if __name__ == '__main__':
    # seeding the pseudo-random generator
    RandomGen.set_seed(16)

    # running all the tests
    unittest.main()

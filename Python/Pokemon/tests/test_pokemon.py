from __future__ import annotations
from pokemon import Charmander, Venusaur, Squirtle, Gengar 
from tests.base_test import BaseTest
import unittest

class TestPokemon(BaseTest):

    def test_venusaur_stats(self):
        v = Venusaur()
        self.assertEqual(v.get_hp(), 21) 
        self.assertEqual(v.get_level(), 2)
        self.assertEqual(v.get_attack_damage(), 5)
        self.assertEqual(v.get_speed(), 4)
        self.assertEqual(v.get_defence(), 10)
        v.level_up()
        v.level_up()
        v.level_up()
        self.assertEqual(v.get_hp(), 22)
        self.assertEqual(v.get_level(), 5)
        self.assertEqual(v.get_attack_damage(), 5)
        self.assertEqual(v.get_speed(), 5)
        self.assertEqual(v.get_defence(), 10)
        v.lose_hp(5)

        self.assertEqual(str(v), "LV. 5 Venusaur: 17 HP")

    def test_charmander_stats(self):
        """
            test for Charmander stats after leveling up and losing hp which influence its stats
        """
        c = Charmander() # get Charmander
        # check its base stats
        self.assertEqual(c.get_poke_name(), "Charmander")
        self.assertEqual(c.get_hp(), 9)
        self.assertEqual(c.get_level(), 1)
        self.assertEqual(c.get_attack_damage(), 7)
        self.assertEqual(c.get_speed(), 8)
        self.assertEqual(c.get_defence(), 4)
        c.level_up() # Charmander levels up
        # check its stats after level up
        self.assertEqual(c.get_hp(), 10)
        self.assertEqual(c.get_level(), 2)
        self.assertEqual(c.get_attack_damage(), 8)
        self.assertEqual(c.get_speed(), 9)
        self.assertEqual(c.get_defence(), 4)
        c.defend(8) # have 8 as effective attack damage
        self.assertEqual(c.get_hp(), 2) # check Charmander hp after losing hp equal to damage dealt

        self.assertEqual(str(c), "LV. 2 Charmander: 2 HP") # check Charmander level and hp 

    def test_squirtle_stats(self):
        """
            Test for Squirtle stats after leveling up and losing hp which influence its stats
        """
        s = Squirtle() # get Squirtle
        # check its base stats
        self.assertEqual(s.get_poke_name(), "Squirtle")
        self.assertEqual(s.get_hp(), 11)
        self.assertEqual(s.get_level(), 1)
        self.assertEqual(s.get_attack_damage(), 4)
        self.assertEqual(s.get_speed(), 7)
        self.assertEqual(s.get_defence(), 7)
        s.level_up() # now Squirtle levels up
        s.level_up() # again
        # check its stats after 2 level up
        self.assertEqual(s.get_hp(), 15)
        self.assertEqual(s.get_level(), 3)
        self.assertEqual(s.get_attack_damage(), 5)
        self.assertEqual(s.get_speed(), 7)
        self.assertEqual(s.get_defence(), 9)
        s.defend(4) # 4 as effective attack damage
        self.assertEqual(s.get_hp(), 13) # check Squirtle hp after losing hp equal to half of damage
        s.lose_hp(3) # Squirtle loses hp

        self.assertEqual(str(s), "LV. 3 Squirtle: 10 HP") # check Squirtle level and hp 

    def test_gengar_stats(self):
        """
            Test for Gengar stats after leveling up and losing hp which influence its stats
        """
        g = Gengar() # get Gengar
        # check its base stats
        self.assertEqual(g.get_poke_name(), "Gengar")
        self.assertEqual(g.get_hp(), 13)
        self.assertEqual(g.get_level(), 3)
        self.assertEqual(g.get_attack_damage(), 18)
        self.assertEqual(g.get_speed(), 12)
        self.assertEqual(g.get_defence(), 3)
        g.level_up() # Gengar levels up
        g.level_up() # again
        g.level_up() # and again
        # check its stats after 3 level up
        self.assertEqual(g.get_hp(), 15)
        self.assertEqual(g.get_level(), 6)
        self.assertEqual(g.get_attack_damage(), 18)
        self.assertEqual(g.get_speed(), 12)
        self.assertEqual(g.get_defence(), 3)
        g.defend(7) # 7 as effectivve attack damage
        self.assertEqual(g.get_hp(), 8) # check Gengar hp after losing hp equal to attack damage
        g.lose_hp(6) # Gengar loses hp

        self.assertEqual(str(g), "LV. 6 Gengar: 2 HP") # check if Gengar level and hp match

if __name__ == '__main__':
    unittest.main()    


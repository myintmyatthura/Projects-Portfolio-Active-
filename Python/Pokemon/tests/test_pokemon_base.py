from __future__ import annotations
from random_gen import RandomGen
from pokemon_base import PokemonBase
from pokemon import Eevee, Gastly, Haunter, Charmander, Bulbasaur, Blastoise, Charizard, Venusaur, Gengar, Squirtle
from tests.base_test import BaseTest
import unittest

class TestPokemonBase(BaseTest):
# class TestPokemonBase(BaseTest): #unittest.TestCase):

    def test_cannot_init(self):
        """Tests that we cannot initialise PokemonBase, and that it raises the correct error."""
        self.assertRaises(TypeError, lambda: PokemonBase(30, "FIRE"))

    def test_level(self):
        e = Eevee()
        self.assertEqual(e.get_level(), 1)
        e.level_up()
        self.assertEqual(e.get_level(), 2)
    
    def test_hp(self):
        e = Eevee()
        self.assertEqual(e.get_hp(), 10)
        e.lose_hp(4)
        self.assertEqual(e.get_hp(), 6)
        e.heal()
        self.assertEqual(e.get_hp(), 10)
        
    def test_status(self):
        RandomGen.set_seed(0)
        e1 = Eevee()
        e2 = Eevee()
        e1.attack(e2)
        # e2 now is confused.
        e2.attack(e1)
        # e2 takes damage in confusion.
        self.assertEqual(e1.get_hp(), 10)

    def test_evolution(self):
        g = Gastly()
        self.assertEqual(g.can_evolve(), True)
        self.assertEqual(g.should_evolve(), True)
        new_g = g.get_evolved_version()
        self.assertIsInstance(new_g, Haunter)

    def test_3_pokemon_level(self):
        """
            Test to check 3 pokemon level after level_up() 
        """

        # test 1
        c = Charmander() # get Charmander
        self.assertEqual(c.get_level(), 1) # check its level
        c.level_up() # Charmander level up
        self.assertEqual(c.get_level(), 2) # check Charmander level after leveling up

        # test 2
        v = Venusaur() # get Venusaur
        self.assertEqual(v.get_level(), 2) # check its level
        v.level_up() # Venusaur level up
        self.assertEqual(v.get_level(), 3) # check Venusaur level after leveling up

        # test 3
        g = Gengar()
        self.assertEqual(g.get_level(), 3) # check its level
        g.level_up() # Gengar level up
        self.assertEqual(g.get_level(), 4) # check Gengar level after leveling up

    def test_3_pokemon_hp(self):
        """
            Test to check for 3 pokemon hp after losing, healing or leveling up
        """

        # test 1
        c = Charmander() # get Charmander
        self.assertEqual(c.get_hp(), 9) # check its hp
        c.lose_hp(5) # Charmander loses 5 hp
        self.assertEqual(c.get_hp(), 4) # check its hp after losing hp
        c.heal() # Charmander healed
        self.assertEqual(c.get_hp(), 9) # check if Charmander hp returns to max hp

        # test 2
        c = Charizard() # get Charizard
        self.assertEqual(c.get_hp(), 15) # check its hp
        c.lose_hp(9) # Charizard loses 9 hp
        self.assertEqual(c.get_hp(), 6) # check its hp after losing hp
        c.heal() # Charizard healed
        self.assertEqual(c.get_hp(), 15) # check if Charizard hp returns to max hp

        # test 3
        b = Bulbasaur() # get Bulbasaur
        self.assertEqual(b.get_hp(), 13) # check its hp
        b.lose_hp(3) # Bulbasaur loses 3 hp
        self.assertEqual(b.get_hp(), 10) # check its hp after losing hp
        b.heal() # Bulbasaur healed
        self.assertEqual(b.get_hp(), 13) # check if Bulbasaur hp returns to max hp
        b.level_up() # Bulbasaur levels up and evolve, since it is not fainted and reached evolving level to Venusaur
        self.assertEqual(b.get_hp(), 14) # now Venusaur, its hp should be at base hp for Venusaur

    def test_3_pokemon_status(self):
        """
            Test to check 3 pokemon status after attacking
        """

        # test 1
        RandomGen.set_seed(0)
        c1 = Charmander()
        c2 = Charmander()
        c1.attack(c2)
        # c2 loses 7 hp and obtain burn effect , c2 hp = 9 - 7 = 2
        c2.attack(c1)
        # c1 takes half of effective attack damage due to c2 burn effect, c1 hp = 9 - (3//2) = 8
        self.assertEqual(c1.get_hp(), 8) # check c1 hp 
        self.assertEqual(c1.is_fainted(), False) # check if c1 is fainted

        # test 2
        RandomGen.set_seed(0)
        b1 = Bulbasaur()
        s1 = Squirtle()
        b1.attack(s1)
        # s1 loses 5 hp and obtain poison effect, s1 hp = 11 - (10//2) = 6
        s1.attack(b1)
        # b1 takes half of effective damage due to defense calculation of b1, b1 hp = 13 - (2//2) = 12
        # due to poison effect in attacking, s1 loses 3 hp, c1 hp = 6 - 3 = 3
        self.assertEqual(s1.get_hp(), 3) # check s1 hp
        self.assertEqual(s1.is_fainted(), False) # check if s1 is fainted

        # test 3
        RandomGen.set_seed(0)
        c1 = Charizard()
        v1 = Venusaur()
        c1.attack(v1)
        # c1 loses 32 hp and obtain fire effect, s1 hp = 21 - 32 = -11
        self.assertEqual(v1.get_hp(), -11) # check s1 hp
        # at this point Venusaur is fainted because its hp is less than or equal to 0
        self.assertEqual(v1.is_fainted(), True) # check if v1 is fainted

    def test_3_evolution(self):
        """
            Test for 3 pokemon capability to evolve based on certain criteria
        """

        # test 1
        s = Squirtle()
        s.level_up()
        s.level_up()
        self.assertEqual(s.can_evolve(), True) # False as it has not reached level needed to evolve
        self.assertEqual(s.should_evolve(), True) # False as can_evolve is False
        new_s = s.get_evolved_version()
        self.assertIsInstance(new_s, Blastoise)
        
        # test 2
        c = Charmander()
        c.level_up()
        c.level_up()
        self.assertEqual(c.can_evolve(), True) # True as it has reached level needed to evolve
        self.assertEqual(c.should_evolve(), True) # True as can_evolve is True and it is not fainted
        new_c = c.get_evolved_version()
        self.assertIsInstance(new_c, Charizard) # check if evolved Charmander is Charizard

        # test 3
        b = Bulbasaur()
        b.level_up()
        b.level_up()
        self.assertEqual(b.can_evolve(), True) # True as it has reached level needed to evolve
        self.assertEqual(b.should_evolve(), True) # True as can_evolve is True and it is not fainted
        new_b = b.get_evolved_version()
        self.assertIsInstance(new_b, Venusaur) # check if evolved Bulbasaur is Venusaur

    def test_inflict_status_effect(self):
        """
            Test for function of inflict_status_effect in PokemonBase which is integrated in the attack method
            This test will just show state of a pokemon after inflicted with status from another pokemon
            without attack, as it is just a demonstration
        """

        # test 1
        c1 = Charmander() # get Charmander
        c2 = Charmander() # get Charmander
        c1.inflict_status_effect(c2) # c2 gets status based on c1 type (Fire)
        self.assertEqual(c2.state, "Burn") # check status

        # test 2
        s = Squirtle() # get Squirtle
        b = Bulbasaur() # get Bulbasaur
        s.inflict_status_effect(b) # s gets status based on s type (Water)
        self.assertEqual(b.state, "Paralysis") # check status

        # test 3
        e = Eevee() # get Eevee
        v = Venusaur() # get Venusaur
        e.inflict_status_effect(v) # e gets status based on e type (Normal)
        self.assertEqual(v.state, "Confusion") # check status
        self.assertEqual(e.state, None) # e should not have status as it is not the one being inflicted

if __name__=='__main__':
    unittest.main()


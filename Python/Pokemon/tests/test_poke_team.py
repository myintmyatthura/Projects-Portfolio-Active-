from __future__ import annotations
import unittest
from poke_team import Action, Criterion, PokeTeam
from pokemon_base import PokemonBase
from random_gen import RandomGen
from pokemon import Bulbasaur, Charizard, Charmander, Gastly, Squirtle, Eevee
from tests.base_test import BaseTest

class TestPokeTeam(BaseTest):

    def test_random(self):
        RandomGen.set_seed(123456789)
        t = PokeTeam.random_team("Cynthia", 0)
        pokemon = []
        while not t.is_empty():
            pokemon.append(t.retrieve_pokemon())
        expected_classes = [Squirtle, Gastly, Eevee, Eevee, Eevee, Eevee]
        self.assertEqual(len(pokemon), len(expected_classes))
        for p, e in zip(pokemon, expected_classes):
            self.assertIsInstance(p, e)

    def test_regen_team(self):
        RandomGen.set_seed(123456789)
        t = PokeTeam.random_team("Cynthia", 2, team_size=4, criterion=Criterion.HP)
        # This should end, since all pokemon are fainted, slowly.
        while not t.is_empty():
            p = t.retrieve_pokemon()
            p.lose_hp(1)
            t.return_pokemon(p)
        t.regenerate_team()
        pokemon = []
        while not t.is_empty():
            pokemon.append(t.retrieve_pokemon())
        expected_classes = [Bulbasaur, Eevee, Charmander, Gastly]
        self.assertEqual(len(pokemon), len(expected_classes))
        for p, e in zip(pokemon, expected_classes):
            self.assertIsInstance(p, e)

    def test_battle_option_attack(self):
        t = PokeTeam("Wallace", [1, 0, 0, 0, 0], 1, PokeTeam.AI.ALWAYS_ATTACK)
        p = t.retrieve_pokemon()
        e = Eevee()
        self.assertEqual(t.choose_battle_option(p, e), Action.ATTACK)

    def test_special_mode_1(self):
        t = PokeTeam("Lance", [1, 1, 1, 1, 1], 1, PokeTeam.AI.SWAP_ON_SUPER_EFFECTIVE)
        # C B S G E
        t.special()
        # S G E B C
        pokemon = []
        while not t.is_empty():
            pokemon.append(t.retrieve_pokemon())
        expected_classes = [Squirtle, Gastly, Eevee, Bulbasaur, Charmander]
        self.assertEqual(len(pokemon), len(expected_classes))
        for p, e in zip(pokemon, expected_classes):
            self.assertIsInstance(p, e)

    def test_string(self):
        t = PokeTeam("Dawn", [1, 1, 1, 1, 1], 2, PokeTeam.AI.RANDOM, Criterion.DEF)
        self.assertEqual(str(t), "Dawn (2): [LV. 1 Gastly: 6 HP, LV. 1 Squirtle: 11 HP, LV. 1 Bulbasaur: 13 HP, LV. 1 Eevee: 10 HP, LV. 1 Charmander: 9 HP]")

    def test_3_random(self):
        """
            Test to check the correctness of random team formation
        """
        RandomGen.set_seed(2020)
        t = PokeTeam.random_team("Vision", 0, team_size = 4) # form random team
        pokemon = []
        while not t.is_empty():
            pokemon.append(t.retrieve_pokemon()) # put the pokemon into a list
        expected_classes = [Bulbasaur, Squirtle, Squirtle, Gastly] 
        self.assertEqual(len(pokemon), len(expected_classes)) # check length of list
        for p, e in zip(pokemon, expected_classes): # comparing two pokemon of same index from two lists 
            self.assertIsInstance(p, e)
        
        RandomGen.set_seed(2021)
        t = PokeTeam.random_team("Toyko", 2, team_size = 6, criterion=Criterion.HP) # form random team with criterion
        pokemon = []
        while not t.is_empty():
            pokemon.append(t.retrieve_pokemon()) # put pokemon into the list
        expected_classes = [Squirtle, Squirtle, Charmander, Charmander, Gastly, Gastly]
        self.assertEqual(len(pokemon), len(expected_classes)) # check length
        for p, e in zip(pokemon, expected_classes): # comparing two pokemon of same index from two lists
            self.assertIsInstance(p, e)

        RandomGen.set_seed(2359)
        t = PokeTeam.random_team("Clock", 1) # form random team with just team name and battle mode 1
        pokemon = []
        while not t.is_empty():
            pokemon.append(t.retrieve_pokemon()) # put pokemon into the list
        expected_classes = [Bulbasaur, Bulbasaur, Squirtle, Squirtle, Gastly, Gastly]
        self.assertEqual(len(pokemon), len(expected_classes)) # check length
        for p, e in zip(pokemon, expected_classes): # comparing two pokemon of same index from two lists
            self.assertIsInstance(p, e)

    def test_3_regen_team(self):
        RandomGen.set_seed(11) # set a random set for random team formation
        t = PokeTeam.random_team("Eleven", 2, team_size=3, criterion=Criterion.HP) # form random team with criterion
        # This should end as all pokemon are fainted by losing hp
        while not t.is_empty():
            p = t.retrieve_pokemon()
            p.lose_hp(2) # the amount is trivial as fainted won't be returned
            t.return_pokemon(p)
        t.regenerate_team() # regenerate a fresh team with same parameters
        pokemon = []
        while not t.is_empty():
            pokemon.append(t.retrieve_pokemon()) # put pokemon into list
        expected_classes = [Squirtle, Eevee, Gastly]
        self.assertEqual(len(pokemon), len(expected_classes)) # check length of lists
        for p, e in zip(pokemon, expected_classes): # comparing two pokemon of same index from two lists
            self.assertIsInstance(p, e)

        t = PokeTeam("Taylor", [2, 2, 0, 0, 0], 0, PokeTeam.AI.SWAP_ON_SUPER_EFFECTIVE)
        # This should end, since all pokemon are fainted by losing hp
        while not t.is_empty():
            p = t.retrieve_pokemon()
            p.lose_hp(13) # the amount is trivial as fainted won't be returned
            t.return_pokemon(p)
        t.regenerate_team() # regenerate a fresh team with same parameters
        pokemon = []
        while not t.is_empty():
            pokemon.append(t.retrieve_pokemon()) # put pokemon into list
        expected_classes = [Charmander, Charmander, Bulbasaur, Bulbasaur]
        self.assertEqual(len(pokemon), len(expected_classes)) # check length of lists
        for p, e in zip(pokemon, expected_classes): # comparing two pokemon of same index from two lists
            self.assertIsInstance(p, e)

        t = PokeTeam("Jake", [3, 0, 1, 0, 0], 1, PokeTeam.AI.ALWAYS_ATTACK)
        # This should end, since all pokemon are fainted by losing hp
        while not t.is_empty():
            p = t.retrieve_pokemon()
            p.lose_hp(4) # the amount is trivial as fainted won't be returned
            t.return_pokemon(p)
        t.regenerate_team() # regenerate a fresh team with same parameters
        pokemon = []
        while not t.is_empty():
            pokemon.append(t.retrieve_pokemon()) # put pokemon into list
        expected_classes = [Charmander, Charmander, Charmander, Squirtle]
        self.assertEqual(len(pokemon), len(expected_classes)) # check length of lists
        for p, e in zip(pokemon, expected_classes): # comparing two pokemon of same index from two lists
            self.assertIsInstance(p, e)

        #pass
    def test_3_battle_option_attack(self):
        """
            Test battle option based on AI modes from class AI
        """
        # test 1
        t = PokeTeam("Ingrid", [1, 0, 0, 0, 0], 1, PokeTeam.AI.SWAP_ON_SUPER_EFFECTIVE)
        p = t.retrieve_pokemon() # retrieve Charmander
        b = Bulbasaur() # get Bulbasaur
        # either swap or attack based on attack type / defend type multiplier
        self.assertEqual(t.choose_battle_option(p, b), Action.ATTACK) # check battle option

        # test 2
        t = PokeTeam("Sloan", [0, 1, 0, 0, 0], 1, PokeTeam.AI.SWAP_ON_SUPER_EFFECTIVE)
        p = t.retrieve_pokemon() # retrieve Bulbasaur
        e = Charmander() # get Charmander
        # either swap or attack based on attack type / defend type multiplier
        self.assertEqual(t.choose_battle_option(p, e), Action.SWAP) # check battle option

        # test 3
        t = PokeTeam("Wright", [1, 0, 1, 0, 1], 2, PokeTeam.AI.ALWAYS_ATTACK, criterion=Criterion.DEF)
        p = t.retrieve_pokemon() # after sorting, first to retrieve is Squirtle
        e = Gastly() # get Gastly
        self.assertEqual(t.choose_battle_option(p, e), Action.ATTACK) # check battle option 

    def test_3_special_mode(self):
        """
            Test for special action performed on a pokemon team based on battle mode 
        """
        # test 1
        t = PokeTeam("Oui", [1, 0, 1, 1, 1], 0, PokeTeam.AI.ALWAYS_ATTACK) # form team with battle mode 0
        # C S G E
        t.special()
        # E S G C
        pokemon = []
        while not t.is_empty():
            pokemon.append(t.retrieve_pokemon()) # put pokemon in list
        expected_classes = [Eevee, Squirtle, Gastly, Charmander]
        self.assertEqual(len(pokemon), len(expected_classes)) # check length of lists
        for p, e in zip(pokemon, expected_classes): # comparing two pokemon of same index from two lists
            self.assertIsInstance(p, e)

        # test 2
        t = PokeTeam("Ou", [2, 1, 0, 1, 2], 1, PokeTeam.AI.SWAP_ON_SUPER_EFFECTIVE) # form team with battle mode 1
        # C C B G E E
        t.special()
        # G E E B C C
        pokemon = []
        while not t.is_empty():
            pokemon.append(t.retrieve_pokemon()) # put pokemon in list
        expected_classes = [Gastly, Eevee, Eevee, Bulbasaur, Charmander, Charmander]
        self.assertEqual(len(pokemon), len(expected_classes)) # compare length of lists
        for p, e in zip(pokemon, expected_classes): # comparing two pokemon of same index from two lists
            self.assertIsInstance(p, e)

        # test 3 
        RandomGen.set_seed(711)
        # form random team with battle mode 2
        t = PokeTeam.random_team("Non", 2, team_size = 4, ai_mode = PokeTeam.AI.RANDOM, criterion=Criterion.SPD)
        # C C S G
        t.special()
        # G S C C
        pokemon = []
        while not t.is_empty():
            pokemon.append(t.retrieve_pokemon()) # put pokemon in list
        expected_classes = [Gastly, Squirtle, Charmander, Charmander]
        self.assertEqual(len(pokemon), len(expected_classes)) # check length of lists
        for p, e in zip(pokemon, expected_classes): # comparing two pokemon of same index from two lists
            self.assertIsInstance(p, e)
        #pass

    def test_3_retrieve_and_return(self):
        """
            Test for retrieving and returning pokemon based on battle mode
        """

        # test 1
        t = PokeTeam("Cyrus", [1, 1, 1, 1, 1], 0, PokeTeam.AI.SWAP_ON_SUPER_EFFECTIVE)
        # C B S G E
        p = t.retrieve_pokemon() # retrieve the first pokemon of team
        self.assertIsInstance(p, Charmander) # check the retrieved pokemon
        t.return_pokemon(p) # return p
        # once returned, p (Charmander) should be in front of the list
        self.assertEqual(str(t), "Cyrus (0): [LV. 1 Charmander: 9 HP, LV. 1 Bulbasaur: 13 HP, LV. 1 Squirtle: 11 HP, LV. 1 Gastly: 6 HP, LV. 1 Eevee: 10 HP]")

        # test 2
        t = PokeTeam("Miley", [0, 1, 0, 1, 1], 1, PokeTeam.AI.SWAP_ON_SUPER_EFFECTIVE)
        # B G E
        p = t.retrieve_pokemon() # retrieve the first pokemon of team
        self.assertIsInstance(p, Bulbasaur) # check the retrieved pokemon
        t.return_pokemon(p) # return p
        # once returned, p (Bulbasaur) should be at the end of the list
        self.assertEqual(str(t), "Miley (1): [LV. 1 Gastly: 6 HP, LV. 1 Eevee: 10 HP, LV. 1 Bulbasaur: 13 HP]")

        # test 3
        t = PokeTeam("Ryan", [0, 2, 1, 0, 1], 2, PokeTeam.AI.SWAP_ON_SUPER_EFFECTIVE, criterion=Criterion.HP)
        # B B S E
        p = t.retrieve_pokemon() # retrieve the first pokemon of team
        self.assertIsInstance(p, Bulbasaur) # check the retrieved pokemon
        p.lose_hp(4) # p loses hp
        t.return_pokemon(p) # return p
        # once returned, p (Bulbasaur) should be at its initial position even with lower hp than the second Bulbasaur
        self.assertEqual(str(t), "Ryan (2): [LV. 1 Bulbasaur: 13 HP, LV. 1 Squirtle: 11 HP, LV. 1 Eevee: 10 HP, LV. 1 Bulbasaur: 9 HP]")
    
    def test_3_string(self):
        """
            Test to check if Poke Team formed is in correct format in order (Pokedex Order or Criterion)
        """
        # test 1
        t = PokeTeam("Noon", [1, 1, 1, 1, 1], 2, PokeTeam.AI.SWAP_ON_SUPER_EFFECTIVE, Criterion.SPD)
        self.assertEqual(str(t), "Noon (2): [LV. 1 Charmander: 9 HP, LV. 1 Eevee: 10 HP, LV. 1 Bulbasaur: 13 HP, LV. 1 Squirtle: 11 HP, LV. 1 Gastly: 6 HP]")

        # test 2
        t = PokeTeam("Evening", [3, 3, 0, 0, 0], 0, PokeTeam.AI.ALWAYS_ATTACK)
        self.assertEqual(str(t), "Evening (0): [LV. 1 Charmander: 9 HP, LV. 1 Charmander: 9 HP, LV. 1 Charmander: 9 HP, LV. 1 Bulbasaur: 13 HP, LV. 1 Bulbasaur: 13 HP, LV. 1 Bulbasaur: 13 HP]")

        # test 3
        t = PokeTeam("Night", [0, 2, 0, 1, 1], 1, PokeTeam.AI.USER_INPUT)
        self.assertEqual(str(t), "Night (1): [LV. 1 Bulbasaur: 13 HP, LV. 1 Bulbasaur: 13 HP, LV. 1 Gastly: 6 HP, LV. 1 Eevee: 10 HP]")

    def test_3_is_empty(self):
        """
        A test constructed for the is_empty instance method to check if the Pokemon Team is empty given certain criteria.
        """
        # test 1
        # given that the team is not empty, check if the returned boolean statement is correct.
        t = PokeTeam("Homelander", [1,1,1,1,1], 0, PokeTeam.AI.ALWAYS_ATTACK)
        self.assertEqual(t.is_empty(), False)

        # test 2
        # given that a given team only has one pokemon, check if the returned boolean statement is correct after retrieving the pokemon.
        t = PokeTeam.random_team("A-Train", 2, 1, criterion=Criterion.SPD)
        self.assertTrue(len(t.team), 1)
        t.retrieve_pokemon()
        self.assertEqual(t.is_empty(), True)

        # test 3
        # given that a random team is generated (where if no team size is specified, it is a random length between 3 and 6), check if the returned boolean statement is correct.
        t = PokeTeam.random_team("The Deep", 1)
        self.assertEqual(t.is_empty(), False)

if __name__ == "__main__":
    unittest.main()



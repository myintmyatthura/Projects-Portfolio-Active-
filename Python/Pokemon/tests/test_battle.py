from __future__ import annotations
from random_gen import RandomGen
from battle import Battle
from poke_team import Criterion, PokeTeam
from pokemon import Charizard, Charmander, Eevee, Gastly, Squirtle, Venusaur, Bulbasaur, Blastoise
from tests.base_test import BaseTest
import unittest

class TestBattle(BaseTest):

    def test_basic_battle(self):
        RandomGen.set_seed(1337)
        team1 = PokeTeam("Ash", [1, 1, 1, 0, 0], 0, PokeTeam.AI.ALWAYS_ATTACK)
        team2 = PokeTeam("Gary", [0, 0, 0, 0, 3], 0, PokeTeam.AI.ALWAYS_ATTACK)
        b = Battle(verbosity=0)
        res = b.battle(team1, team2)
        self.assertEqual(res, 1)
        self.assertTrue(team2.is_empty())
        remaining = []
        while not team1.is_empty():
            remaining.append(team1.retrieve_pokemon())
        self.assertEqual(len(remaining), 2)
        self.assertEqual(remaining[0].get_hp(), 1)
        self.assertIsInstance(remaining[0], Venusaur)
        self.assertEqual(remaining[1].get_hp(), 11)
        self.assertIsInstance(remaining[1], Squirtle)

    def test_complicated_battle(self):
        RandomGen.set_seed(192837465)
        team1 = PokeTeam("Brock", [1, 1, 1, 1, 1], 2, PokeTeam.AI.SWAP_ON_SUPER_EFFECTIVE, criterion=Criterion.HP)
        team2 = PokeTeam("Misty", [0, 0, 0, 3, 3], 2, PokeTeam.AI.SWAP_ON_SUPER_EFFECTIVE, criterion=Criterion.SPD)
        b = Battle(verbosity=0)
        res = b.battle(team1, team2)
        self.assertEqual(res, 1)
        remaining = []
        while not team1.is_empty():
            remaining.append(team1.retrieve_pokemon())
        self.assertEqual(len(remaining), 2)
        self.assertEqual(remaining[0].get_hp(), 11)
        self.assertIsInstance(remaining[0], Charizard)
        self.assertEqual(remaining[1].get_hp(), 6)
        self.assertIsInstance(remaining[1], Gastly)

    def test_3_battle(self):
        """
            Test battles between teams
        """
        RandomGen.set_seed(17) # this seed is crucial in determing if there is inflicting status and confusion attack
        team1 = PokeTeam("Ace", [1, 0, 1, 1, 0], 0, PokeTeam.AI.SWAP_ON_SUPER_EFFECTIVE)
        team2 = PokeTeam("Gary", [0, 1, 2, 0, 0], 0, PokeTeam.AI.ALWAYS_ATTACK)
        b = Battle(verbosity=0)
        res = b.battle(team1, team2) # start battle
        self.assertEqual(res, 2) # check battle outcome
        self.assertTrue(team1.is_empty()) # since team 2 won, team 1 must be empty
        remaining = []
        while not team2.is_empty():
            remaining.append(team2.retrieve_pokemon()) # putting pokemon into remaining list
        self.assertEqual(len(remaining), 2) # check length of remaining list
        self.assertEqual(remaining[0].get_hp(), 11) # check the last pokemon hp
        self.assertIsInstance(remaining[0], Blastoise) # check which pokemon
        self.assertEqual(remaining[1].get_hp(), 11) # check hp of second pokemon
        self.assertIsInstance(remaining[1], Squirtle) # second pokemon

        RandomGen.set_seed(90) # this seed is crucial in determing if there is inflicting status and confusion attack
        team1 = PokeTeam("Manny", [1, 0, 0, 1, 1], 1, PokeTeam.AI.RANDOM)
        team2 = PokeTeam("Bart", [0, 1, 1, 1, 0], 1, PokeTeam.AI.SWAP_ON_SUPER_EFFECTIVE)
        b = Battle(verbosity=0)
        res = b.battle(team1, team2) # start battle
        self.assertEqual(res, 2) # check battle outcome
        self.assertTrue(team1.is_empty()) # team 1 should be empty if team 2 won
        remaining = []
        while not team2.is_empty():
            remaining.append(team2.retrieve_pokemon()) # putting remaining pokemon into remaining list
        self.assertEqual(len(remaining), 3) # check length of remamining list
        self.assertEqual(remaining[0].get_hp(), 6) # check hp of first pokemon
        self.assertIsInstance(remaining[0], Gastly) # check first pokemon
        self.assertEqual(remaining[1].get_hp(), 13) # check hp of second pokemon
        self.assertIsInstance(remaining[1], Bulbasaur) # second pokemon
        self.assertEqual(remaining[2].get_hp(), 13) # check hp of third pokemon
        self.assertIsInstance(remaining[2], Blastoise) # check third pokemon

        RandomGen.set_seed(88) # this seed is crucial in determing if there is inflicting status and confusion attack
        team1 = PokeTeam("Sad", [2, 0, 0, 2, 0], 2, PokeTeam.AI.ALWAYS_ATTACK, criterion=Criterion.SPD)
        team2 = PokeTeam("Happy", [0, 1, 3, 0, 0], 2, PokeTeam.AI.SWAP_ON_SUPER_EFFECTIVE, criterion=Criterion.DEF)
        b = Battle(verbosity=0)
        res = b.battle(team1, team2) # start battle
        self.assertEqual(res, 2) # check battle outcome
        self.assertTrue(team1.is_empty()) # team 1 should be empty as team 2 won
        remaining = []
        while not team2.is_empty():
            remaining.append(team2.retrieve_pokemon()) # put remaining pokemon into remaining list
        self.assertEqual(len(remaining), 2) # check length of remaining list
        self.assertEqual(remaining[0].get_hp(), 7) # check hp of first pokemon
        self.assertIsInstance(remaining[0], Squirtle) # check first pokemon
        self.assertEqual(remaining[1].get_hp(), 13) # check hp of second pokemon
        self.assertIsInstance(remaining[1], Bulbasaur) # check second pokemon

if __name__ == "__main__":
    unittest.main()

from __future__ import annotations
from pokemon_base import PokemonBase
"""
"""
__author__ = "Scaffold by Jackson Goerner, Code by Myint Myat Thura, Lau Ka-Kiat, Wong Heng Yew, Tay Chean Hao"

from random_gen import RandomGen
from poke_team import Action, PokeTeam, Criterion
from print_screen import print_game_screen

class Battle:
    """
        CLASS DESCRIPTION:
        Battle Class used when pokemons battle each other.
    """
    
    def __init__(self, verbosity=0) -> None:
        """
            PRECONDITIONS:
            [NONE]            
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            PARAMETERS:
            objects instantiated:
            -   verbosity[integer]: optional switch to possibly enable printing/logging while battling(not sure
                how fun testing really will be with this added =.=)
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            FUNCTION DESCRIPTION:
            __init__ magic method to initialise the object related to Battle.
            -   attributes assigned:
                _________________________________________________________________
                |battle_outcome |verbosity  |team_1    |team_2   |t1    |t2     | 
                |_______________|___________|__________|_________|______|_______|
                |None           |verbosity  |None      |None     |None  |None   |
                |_______________|___________|__________|_________|______|_______|
                -   where battle_outcome = None, verbosity = verbosity, team_1 = None, team_2 = None,
                    t1 = None, t2 = None
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [NONE]: its an __init__ function
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all, only assigns values to variables.
        """
        self.battle_outcome = None
        self.verbosity = verbosity
        self.team_1 = None
        self.team_2 = None
        self.t1 = None
        self.t2 = None

    def battle(self, team1: PokeTeam, team2: PokeTeam) -> int:
        """
            PRECONDITIONS:
            team1 has to be an object from PokeTeam or its subclasses
            team2 has to be an object from PokeTeam or its subclasses            
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            PARAMETERS:
            objects instantiated:
            -   team1[PokeTeam]: one of the 2 teams that will be battling each other.
            -   team2[PokeTeam]: one of the 2 teams that will be battling each other.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            FUNCTION DESCRIPTION:
            Runs the battle between the 2 teams of pokemon.
            A battle_outcome will be returned once the battle is over, which will only happen if either team
            wins the battle or both sides have lost all their pokemons.
            battle_outcome can only be 0, 1 or 2, with each integer implying a different result.
                _____________________________________________
                |battle_outcome |result                     | 
                |_______________|___________________________|
                |0              |draw as both teams'        |
                |               |pokemons have all fainted  |
                |_______________|___________________________|
                |1              |team 1 wins                | 
                |_______________|___________________________|
                |2              |team 2 wins                |
                |_______________|___________________________|
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            battle_outcome[integer]: an integer that signifies the results of the battle.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST CASE:
            O(n), where n is the number of turns needed for the battle to be finished.
            
            COMPLEITY FOR WORST CASE:
            O(n+k^2), where n is the number of turns needed for the battle to be finished, and k is the number 
            of pokemons in a team.
            This only happens if both team's battle_mode is 2.
        """
        self.team_1 = team1
        self.team_2 = team2
        # both teams retrieve a pokemon
        self.t1 = self.team_1.retrieve_pokemon()
        self.t2 = self.team_2.retrieve_pokemon()

        while self.battle_outcome == None:

        # check the options
            team1_choice = self.team_1.choose_battle_option(self.t1, self.t2)
            team2_choice = self.team_2.choose_battle_option(self.t2, self.t1)

            if self.verbosity != 0:
                self.screen_output(team1_choice, team2_choice)

        #swap
            if team1_choice == Action.SWAP:
                self.team_1.return_pokemon(self.t1)
                self.t1 = self.team_1.retrieve_pokemon() 
            if team2_choice == Action.SWAP:
                self.team_2.return_pokemon(self.t2)
                self.t2 = self.team_2.retrieve_pokemon()

        #special
            if team1_choice == Action.SPECIAL:
                self.team_1.return_pokemon(self.t1)
                self.team_1.special()
                self.t1 = self.team_1.retrieve_pokemon()
            if team2_choice == Action.SPECIAL:
                self.team_2.return_pokemon(self.t2)
                self.team_2.special()
                self.t2 = self.team_2.retrieve_pokemon()

        #heal
        # if no more remaining heals and use heal, lose
            if team1_choice == Action.HEAL:
                if self.team_1.heals_avail == 0:
                    self.battle_outcome = 2
                else:
                    self.t1.heal()
                    self.team_1.heals_avail -= 1

            if team2_choice == Action.HEAL:
                if self.team_2.heals_avail == 0:
                    self.battle_outcome == 1

                else:
                    self.t2.heal()
                    self.team_2.heals_avail -= 1

        #attack
        #if both attack, get speed. if defending not fainted, attack too
            if team1_choice == Action.ATTACK and team2_choice == Action.ATTACK:
                if self.t1.get_speed() > self.t2.get_speed():
                    self.t1.attack(self.t2)
                    if not self.t2.is_fainted():
                        self.t2.attack(self.t1)

                elif self.t1.get_speed() < self.t2.get_speed():
                    self.t2.attack(self.t1)
                    if not self.t1.is_fainted():
                        self.t1.attack(self.t2)
        #if same speed, both attack, but team1 first.                        
                else:
                    self.t1.attack(self.t2)
                    self.t2.attack(self.t1)

            elif team1_choice == Action.ATTACK:
                self.t1.attack(self.t2)

            elif team2_choice == Action.ATTACK:
                self.t2.attack(self.t1)

                #if both not dead, lose 1 hp
            if (self.t1 != None and not self.t1.is_fainted()) and (self.t2 != None and not self.t2.is_fainted()):
                self.t1.lose_hp(1)
                self.t2.lose_hp(1)

                # if one faint other didn't, other level up
            if (self.t1 != None and self.t1.is_fainted()) and self.t2 != None:
                self.t2.level_up()

            elif (self.t2 != None and self.t2.is_fainted()) and self.t1 != None:
                self.t1.level_up()

            if self.t1 != None and self.t1.should_evolve():
                self.t1 = self.t1.get_evolved_version()
            
            if self.t2 != None and self.t2.should_evolve():
                self.t2 = self.t2.get_evolved_version()
                
        #if fainted, return and retrieve new one
            if self.t1 != None and self.t1.is_fainted():
                self.team_1.return_pokemon(self.t1)
                self.t1 = self.team_1.retrieve_pokemon() 

            if self.t2 != None and self.t2.is_fainted():
                self.team_2.return_pokemon(self.t2)
                self.t2 = self.team_2.retrieve_pokemon()

        #if team empty, other team wins. if both empty, draw.
            if (self.team_1.on_the_field == None and self.team_2.on_the_field == None) and (len(self.team_1.team) == 0 and len(self.team_2.team) == 0):
                self.battle_outcome = 0
                
            elif self.team_1.on_the_field == None and len(self.team_1.team) == 0:
                self.team_2.return_pokemon(self.t2)
                self.battle_outcome = 2
                
            elif self.team_2.on_the_field == None and len(self.team_2.team) == 0:
                self.team_1.return_pokemon(self.t1)
                self.battle_outcome = 1

        return self.battle_outcome

    def screen_output(self, team1_choice: Action, team2_choice: Action) -> str:
        """
            PRECONDITIONS:
            [NONE]          
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            PARAMETERS:
            objects instantiated:
            -   team1_choice[Action]: action chosen by team 1
            -   team2_choice[Action]: action chosen by team 2
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            FUNCTION DESCRIPTION:
            Displays the 2 team's choices, the team itself, the state, number of pokemons remaining, and the 
            current pokemon battling respectively.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [string]: returns a string containing the 2 team's choices, the team itself, the state, number of
                      pokemons ramaining, and the current pokemon battling respectively.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST CASE AND WORST CASE:
            O(1), just a print statement.
        """
        if self.verbosity > 3:
            raise ValueError("Printing for verboisity above 3 does not exist.")

        if self.verbosity == 1:
            print(team1_choice.name, self.t1, self.t1.state, len(self.team_1.team), self.team_1)
            print(team2_choice.name, self.t2, self.t2.state, len(self.team_2.team), self.team_2)
            # pass

        elif self.verbosity == 2:
            print(self.t1, self.t1.state, len(self.team_1.team), self.team_1.team)
            pass

        elif self.verbosity == 3:
            # print_game_screen(self.t1.get_poke_name(), self.t2.get_poke_name(), self.t1.get_hp(), self.t1.max_hp, self.t2.get_hp(), self.t2.max_hp, self.t1.get_level(), self.t2.get_level(), self.t1.state, self.t2.state, len(self.team_1.team), len(self.team_2.team))
            pass
            
if __name__ == "__main__":
    b = Battle(verbosity=3)
    RandomGen.set_seed(16)
    t1 = PokeTeam.random_team("Cynthia", 0, criterion=Criterion.SPD)
    t1.ai_type = PokeTeam.AI.USER_INPUT
    t2 = PokeTeam.random_team("Barry", 1)
    print(b.battle(t1, t2))
    

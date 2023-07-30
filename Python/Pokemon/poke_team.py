from __future__ import annotations

"""
"""
__author__ = "Scaffold by Jackson Goerner, Code by Myint Myat Thura, Lau Ka-Kiat, Wong Heng Yew, Tay Chean Hao"

from enum import Enum, auto
from pokemon_base import PokemonBase
from pokemon import Charmander, Charizard, Squirtle, Blastoise, Bulbasaur, Venusaur, Gastly, Haunter, Gengar, Eevee
from referential_array import ArrayR
from array_sorted_list import ArraySortedList, ListItem
from random_gen import RandomGen
from queue_adt import CircularQueue
from stack_adt import ArrayStack

class Action(Enum):
    """
        CLASS DESCRIPTION:
        It contains 4 actions with each of them automatically enumerate its state as an enum member
        The enumeration starts from 1 for ATTACK and ends at 4 for SPECIAL
    """
    ATTACK = auto()
    SWAP = auto()
    HEAL = auto()
    SPECIAL = auto()
    
class Criterion(Enum):
    """
        CLASS DESCRIPTION:
        It contains 4 statistics with each of them automatically enumerate its state as an enum member
        The enumeration starts from 1 for SPD and ends at 4 for DEF
    """
    SPD = auto()
    HP = auto()
    LV = auto()
    DEF = auto()

class PokeTeam:
    """
        CLASS DESCRIPTION:
        Used to form PokeTeam objects with parameters team_name, team_numbers, battle_mode, ai_type,
        criterion and criterion_value.
        Also declares constant lists which are POKEDEX_ORDER and INITIAL_POKEMON
    """
    POKEDEX_ORDER = [Charmander, Charizard, Bulbasaur, Venusaur, Squirtle, Blastoise, Gastly, Haunter, Gengar, Eevee]
    INITIAL_POKEMON = [Charmander, Bulbasaur, Squirtle, Gastly, Eevee]

    class AI(Enum):
        """
            CLASS DESCRIPTION
            It contains 4 AI type with each of them automatically enumerate its state as an enum member
            The enumeration starts from 1 for ALWAYS_ATTACK and ends at 4 for USER_INPUT
        """
        ALWAYS_ATTACK = auto()
        SWAP_ON_SUPER_EFFECTIVE = auto()
        RANDOM = auto()
        USER_INPUT = auto()

    def __init__(self, team_name: str, team_numbers: list[int], battle_mode: int, ai_type: PokeTeam.AI, criterion=None, criterion_value=None) -> None:
        """
            PRECONDITIONS:
            -   team_name parameter must be a string
            -   team_numbers must be a list that contains integer elements
                -   number of elements within team_numbers list must be either 5 or 6
                -   sum of all integers within team_numbers list must not exceed 6
            -   battle_mode must be an integer, either 0, 1 or 2
            -   ai_type must be based on AI(Enum), where the integer 1-4 stands for an AI type, namely
                ALWAYS_ATTACK, SWAP_ON_SUPER_EFFECTIVE, RANDOM, and USER_INPUT
            -   criterion, if given, must be within Criterion(Enum)
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            PARAMETERS:
            -   objects instantiated:
                -   team_name[string]: name of the PokeTeam object created.
                -   team_numbers[list[integer]]: list of the pokemons within the PokeTeam object, with each
                    integer standing for a different pokemon.
                -   battle_mode[int]: integer that decides how the pokemons should be ordered in a battle.
                -   ai_type[PokeTeam.AI]: one of the four elements within AI(Enum) which decides how the AI makes
                    decisions in battle.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            FUNCTION DESCRIPTION:
            __init__ magic method to initialise the attributes of an object from PokeTeam Class.
            -   object has attributes team_name, team_numbers, battle_mode, ai_type, criterion, 
                criterion_value, crit, heals_avail, team_size, team, on_the_field, special_used
                -   crit, heals_avail, team_size, on_the_field and special_used have defaulted values:
                    _____________________________________________________________________
                    |crit   |heals_avail    |team_size  |on_the_field   |special_used   |
                    |_______|_______________|___________|_______________|_______________|
                    |None   |3              |0          |None           |0              |
                    |_______|_______________|___________|_______________|_______________|
                    -   where crit = None, heals_avail = 3, team_size = 0, on_the_field = None, 
                        special_used = 0
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [NONE]: its an __init__ function
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST CASE:
            O(n), where n is the number of elements in team_numbers 
            COMPLEXITY FOR WORST CASE:
            O(n), where n is the number of elements in team_numbers + all 4 members of AI(Enum) and 
            Criterion(Enum) 
        """
        if len(team_numbers) < 5 or len(team_numbers) > 6 or sum(team_numbers) > 6:
            raise ValueError("This list is invalid; requires 5 items that sum doesn't exceeed 6")
        if battle_mode < 0 or battle_mode > 2:
            raise ValueError(f"Battle_mode with value {battle_mode} is not available.")
        if ai_type not in PokeTeam.AI:
            raise ValueError("The AI type chosen is not correct or not available")
        if criterion != None and criterion not in Criterion:
            raise ValueError("An invalid criterion was given.")
        
        self.team_name = team_name
        self.team_numbers = team_numbers
        self.battle_mode = battle_mode
        self.ai_type = ai_type
        self.criterion = criterion
        self.criterion_value = criterion_value
        self.crit = None
        self.heals_avail = 3
        self.team_size = 0
        self.team = self.team_creator()
        self.on_the_field = None
        self.special_used = 0
    
    def team_creator(self) -> ArraySortedList:
        """
            PRECONDITIONS:
            [NONE]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            PARAMETERS:
            Object instantiated from PokeTeam
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            Creates the team of pokemons from the values initialised in the __init__ function.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            team[ArraySortedList]: an ArraySortedList of the team of pokemons
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(n^2): -   single nested for loop in both cases where battle_mode != 2 and battle_mode == 2
                    -   n is the number of elements in team_numbers
        """
        if self.battle_mode == 2:
            for i in range(len(self.team_numbers)):
                self.team_size += self.team_numbers[i]
            
            self.team = ArraySortedList(self.team_size)

            self.crit = self.crit_selector()

            for i in range(len(self.team_numbers)):
                for _ in range(self.team_numbers[i]):
                    self.team.add(ListItem(self.INITIAL_POKEMON[i](), eval(f"self.INITIAL_POKEMON[i]()." + self.crit)))

                
            descending_team = ArraySortedList(len(self.team))
            for i in range(len(self.team)-1,-1,-1):
                item = self.team[i]
                descending_team.add(ListItem(item.value, len(self.team)-1-i))
            self.team = descending_team

            if self.criterion == Criterion.LV:
                self.pokedex_ordering(self.team)

            return self.team

        else:
            for i in range(len(self.team_numbers)):
                self.team_size += self.team_numbers[i]
            
            self.team = ArraySortedList(self.team_size)

            for i in range(len(self.team_numbers)):
                for _ in range(self.team_numbers[i]):
                    self.team.add(ListItem(self.INITIAL_POKEMON[i](), len(self.team)))
            
            return self.team

    def crit_selector(self) -> str:
        """
            PRECONDITIONS:
            [NONE]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            PARAMETERS:
            Object instantiated from PokeTeam
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            Returns a string of the command needed to get the value criterion refers to.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [string]: string of command
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST CASE:
            O(1), consists of only if_statements
        """
        if self.criterion == Criterion.SPD:
            return "get_speed()"
        elif self.criterion == Criterion.HP:
            return "get_hp()"
        elif self.criterion == Criterion.LV:
            return "get_level()"
        elif self.criterion == Criterion.DEF:
            return "get_defence()"

    @classmethod
    def random_team(cls, team_name: str, battle_mode: int, team_size=None, ai_mode=None, **kwargs):
        """
            PRECONDITIONS:
            -   team_name parameter must be a string
            -   battle_mode parameter must be an integer
                -   must be either integer 0, 1 or 2
            -   team_size can be left blank
                -   in that case, a random integer between 3 and 6 will be declared as team_size
            -   ai_mode must be within AI(Enum)
                _________________________________________________________________
                |1              |2                          |3      |4          |
                |_______________|___________________________|_______|___________|
                |ALWAYS_ATTACK  |SWAP_ON_SUPER_EFFECTIVE    |RANDOM |USER_INPUT |
                |_______________|___________________________|_______|___________|
                -   Either ALWAYS_ATTACK, SWAP_ON_SUPER_EFFECTIVE, RANDOM or USER_INPUT
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            PARAMETERS:
            The PokeTeam Class instance instantiated:
            team_name[string]: stands as the name of the PokeTeam
            battle_mode[int]: integer that decides how the pokemons within the team will be ordered during a
                              battle
            team_size[None]: integer that determines the size of the team
                             -  if nothing is entered, a random integer between 3 and 6 is given as the 
                                team_size
            ai_mode[None]: one of the elements within AI(Enum) that determines the actions taken in a battle
                           -    if no ai_mode was given, the ai_mode will automatically be RANDOM
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            Initialises a random team of pokemons that either has a team_size inputted or randomly generated
            between 3 and 6.
            The list of team_number will be sorted in ascending order.
            In a battle, the team of pokemons will use one of the four AI modes found within AI(Enum) to 
            decide on their course of action throughout the battle.
            
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            The PokeTeam Class instance instantiated:
            team_name[string]: name of the pokemon team
            team_numbers_list[list[integer]]: list of integers that are the difference between individual
                                              elements in team_numbers.
            battle_mode[integer]: an integer that designates the order in which the team of pokemons will be 
                                  organised.
            ai_action_value: value equal to the enum members in AI(Enum) that determines the actions taken
                             in battle
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE: 
            O(n^2), from bubble_sort()
        """

        def bubble_sort(lst: ArrayR) -> None:
            """
                PRECONDITIONS:
                lst has to be an object from ArrayR or its subclasses
                ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
                PARAMETERS:
                lst[ArrayR]: a list of the pokemon in a team
                ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
                FUNCTION DESCRIPTION:
                Rearranges the list of pokemons given in an ascending order.
                ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
                RETURN:
                [NONE]
                ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
                COMPLEXITY FOR BEST AND WORST CASE:
                O(n^2), where n is the length of lst - 1
            """
            n = len(lst)
            for mark in range(n-1, 0, -1):
                swapped = False
                for i in range(mark):
                    if lst[i] > lst[i+1]:
                        swap(lst, i, i+1)
                        swapped = True
                if not swapped:
                    break

        def swap(lst: ArrayR, i: int, j: int) -> None:
            """
                PRECONDITIONS:
                lst has to be an object from ArrayR or its subclasses
                i has to be an integer
                j has to be an integer
                ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
                PARAMETERS:
                lst[ArrayR]: a list of the pokemon in a team
                i[integer]: index used to refer to the previous element
                j[integer]: index used to refer to the next element
                ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
                FUNCTION DESCRIPTION:
                Swaps around 2 elements within a list.
                ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
                RETURN:
                [NONE]
                ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
                COMPLEXITY FOR BEST AND WORST CASE:
                O(1), no iterations, just 3 lines of assignments
            """
            hold = lst[i]
            lst[i] = lst[j]
            lst[j] = hold
        
        if team_size == None:
            team_size = RandomGen.randint(3,6)
        
        randomised_team = ArrayR(6)
        team_numbers = ArrayR(5)
        randomised_team[0] = 0
        randomised_team[1] = team_size
        for i in range(2, 6):
            randomised_team[i] = RandomGen.randint(0, team_size)

        bubble_sort(randomised_team)

        for i in range(len(randomised_team)-1):
            team_numbers[i] = randomised_team[i+1] - randomised_team[i]

        if ai_mode == None:
            ai_mode = PokeTeam.AI.RANDOM  

        return cls(team_name, team_numbers, battle_mode, ai_mode, **kwargs)
                       
    def return_pokemon(self, poke: PokemonBase) -> None:
        """
            PRECONDITIONS:
            poke must be an object instantiated from PokemonBase or its subclasses.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            PARAMETERS:
            Object instantiated from PokeTeam:
            poke[PokemonBase]: an object instantiated from PokemonBase or its subclassses
                               -    in this case, it is the pokemon that should be returned
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            Used to return pokemon from the battlefield to the team.
            Different battle_mode would return the pokemon to different positions within the team.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [NONE]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST:
            O(1), if battle_mode == 0, just some if_statements will be went through
            COMPLEXITY FOR WORST CASE:
            O(n^2), if battle_mode is neither 0 nor 1, for loops are within where after going through a 
            container, it goes through another list.
        """
        if self.battle_mode == 0:
            if poke.is_fainted():
                pass
            
            else:
                self.team.add(ListItem(poke, 0))
            
        elif self.battle_mode == 1:
            if poke.is_fainted():
                pass

            else:
                self.team.add(ListItem(poke, self.team[-1].key+1))
                
        else:
            if poke.is_fainted():
                pass 

            else:
                self.team.add(ListItem(poke, self.on_the_field.key))
                arranged_team = ArraySortedList(len(self.team))
                while not self.team.is_empty():
                    item = self.team.delete_at_index(0)
                    arranged_team.add(ListItem(item.value, eval(f"item.value." + self.crit)))
                for i in range(len(arranged_team)):
                    arranged_team[i].key = i

                if self.special_used % 2 >= 1 and self.criterion == Criterion.LV:
                    indx = None
                    for i in range(len(arranged_team)-1):
                        if arranged_team[i].value.get_level() < arranged_team[i+1].value.get_level():
                            indx = i
                            break
                    
                    if indx != None:
                        lower_half = ArraySortedList(indx+1)
                        for i in range(indx+1):
                            lower_half.add(arranged_team.delete_at_index(0))
                        self.pokedex_ordering(lower_half)
                        flipped_lower = ArraySortedList(len(lower_half))
                        for i in range(len(lower_half)-1,-1,-1):
                            item = lower_half[i]
                            flipped_lower.add(ListItem(item.value, len(lower_half)-1-i))

                        upper_half = ArraySortedList(len(arranged_team)-indx-1)
                        for i in range(len(arranged_team)):
                            upper_half.add(arranged_team.delete_at_index(0))
                        self.pokedex_ordering(upper_half)

                        sorted_team = ArraySortedList(len(flipped_lower) + len(upper_half))
                        while not flipped_lower.is_empty():
                            sorted_team.add(ListItem(flipped_lower.delete_at_index(0).value, len(sorted_team)))

                        while not upper_half.is_empty():
                            sorted_team.add(ListItem(upper_half.delete_at_index(0).value, len(sorted_team)))
                        
                        self.team = sorted_team

                    else:
                        self.pokedex_ordering(arranged_team)
                        flipped_order = ArraySortedList(len(arranged_team))
                        for i in range(len(arranged_team)-1,-1,-1):
                            item = arranged_team[i]
                            flipped_order.add(ListItem(item.value, len(arranged_team)-1-i))
                        self.team = flipped_order

                elif self.special_used % 2 >= 1:      # if not 0 means it's ascending order                   
                    self.pokedex_ordering(arranged_team)
                    self.team = arranged_team
                        
                else:                                # descending order
                    descending_team = ArraySortedList(len(arranged_team))
                    for i in range(len(arranged_team)-1,-1,-1):
                        item = arranged_team[i]
                        descending_team.add(ListItem(item.value, len(arranged_team)-1-i))
                        
                    self.pokedex_ordering(descending_team)
                    self.team = descending_team
                    

    def retrieve_pokemon(self) -> PokemonBase | None:
        """
            PRECONDITIONS:
            Only retrieves pokemon if the PokeTeam object is not empty.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            PARAMETERS:
            Object instantiated from PokeTeam
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            Used to retrieve pokemon from the team to the battlefield.
            Different battle_mode would retrieve pokemon from different position.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            poke_out[PokemonBase]: a pokemon from the PokeTeam that's chosen to be retrieved
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all, just retrieves the pokemon after going through various if statements.
        """
        if self.team.is_empty():
            self.on_the_field = None
            return None
        self.on_the_field = self.team.delete_at_index(0)
        return self.on_the_field.value

    def special(self) -> None:
        """
            PRECONDITIONS:
            [NONE]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            PARAMETERS:
            Object instantiated from PokeTeam
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            Rearranges the PokeTeam object based on the battle_mode the object is in.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [NONE]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST CASE:
            O(1), in the case of battle_mode == 0, there is no iteration, only 1st and last pokemon swapping 
            around in the PokeTeam.
            COMPLEXITY FOR WORST CASE:
            O(n^2), for loop with team.delete_at_index() within, meaning that everytime the for loop loops, 
            team.delete_at_index() goes through the entire list again.
        """
        if self.battle_mode == 0:
            first = self.team.delete_at_index(0)                    # gets the pokemon in the first position
            last = self.team.delete_at_index(len(self.team)-1)      # gets the pokemon in the last position
            last.key = 0                                            # sets the last pokemon's key to 0, so that when it is added to the list it is added to the front
            self.team.add(last)
            first.key = self.team[len(self.team)-1].key + 1                              # sets the first pokemon's key to the end of the list
            self.team.add(first)

        elif self.battle_mode == 1:
            first_half = len(self.team) // 2
            team_first_half = ArrayStack(first_half)
            for _ in range(first_half):
                team_first_half.push(self.team.delete_at_index(0))
            for i in range(len(self.team)):
                self.team[i].key = i
            while not team_first_half.is_empty():
                self.team.add(ListItem(team_first_half.pop().value, len(self.team)))

        else:
            self.special_used += 1
            flipped_team = ArraySortedList(len(self.team))
            for i in range(len(self.team)-1,-1,-1):
                item = self.team[i]
                flipped_team.add(ListItem(item.value, len(self.team)-1-i))
            if self.criterion == Criterion.LV:
                self.team = flipped_team
            else:
                self.pokedex_ordering(flipped_team)
                self.team = flipped_team
            
    def regenerate_team(self) -> None:
        """
            PRECONDITIONS:
            [NONE]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            PARAMETERS:
            Object instantiated from PokeTeam
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            Completely regenerates the PokeTeam.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [NONE]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST CASE:
            O(n^2), same as team_creator()      
        """
        self.team = self.team_creator()

    def __str__(self):
        """
            PRECONDITIONS:
            [NONE]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            PARAMETERS:
            Object instantiated from PokeTeam
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            __str__ function prints out the entire team with the team_name, and each individual pokemon's
            level, name and hp.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            output[string]: a string with the team_name, battle_mode, and each individual pokemon's level, 
                            name and hp.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST CASE:
            O(1), in the case of an empty team, the code will not go through a while loop and just return
            the team_name, battle_mode and a square bracket.
            COMPLEXITY FOR WORST CASE:
            O(n), where n is the number of pokemons in the team.
        """
        # "Dawn (2): [LV. 1 Gastly: 6 HP, LV. 1 Squirtle: 11 HP, LV. 1 Bulbasaur: 13 HP, LV. 1 Eevee: 10 HP, LV. 1 Charmander: 9 HP]
        output = f"{self.team_name} ({self.battle_mode}): ["
        for i in range(len(self.team)):
            if i > 0:
                output += ", "
            pokemon = str(self.team[i].value)
            output += pokemon
        output += "]"
        return output

    def is_empty(self) -> bool:
        """
            PRECONDITIONS:
            [NONE]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            PARAMETERS:
            Object instantiated from PokeTeam
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            Checks whether team is empty.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            self.team.is_empty[boolean]: boolean statement for whether team is empty.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST CASE AND WORST CASE:
            O(1), just a boolean.
        """
        return self.team.is_empty()

    def choose_battle_option(self, my_pokemon: PokemonBase, their_pokemon: PokemonBase) -> Action:
        """
            PRECONDITIONS:
            [NONE]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            PARAMETERS:
            Object instantiated from PokeTeam:
            my_pokemon[PokemonBase]: the attacking pokemon
            their_pokemon[PokemonBase]: the defending pokemon
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            Based on the ai_type, chooses a battle_option from the options within Action(Enum).
                ________________________________
                |1      |2      |3      |4      |
                |_______|_______|_______|_______|
                |ATTACK |SWAP   |HEAL   |SPECIAL|
                |_______|_______|_______|_______|
                -   Either ATTACK, SWAP, HEAL or SPECIAL
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            battle_action[Action]: the chosen battle action from Action(Enum).
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST CASE:
            O(1), if self.AI.ALWAYS_ATTACK is chosen, Action.ATTACK will be returned.

            COMPLEXITY FOR WORST CASE:
            O(n), if self.AI.SWAP_ON_SUPER_EFFECTIVE is chosen, the for loop goes through every element in the
            PokemonBase.POKEMON_TYPE list.
        """
        if self.ai_type == PokeTeam.AI.ALWAYS_ATTACK:
            battle_action = Action.ATTACK
            
        elif self.ai_type == PokeTeam.AI.SWAP_ON_SUPER_EFFECTIVE:
            for i in range(len(PokemonBase.POKEMON_TYPE)):
                if their_pokemon.type == PokemonBase.POKEMON_TYPE[i]:
                    attacking_type_list = PokemonBase.POKEMON_MULTIPLIERS[i]
                    break

            for i in range(len(PokemonBase.POKEMON_TYPE)):
                if my_pokemon.type == PokemonBase.POKEMON_TYPE[i]:
                    def_type_index = i

            if attacking_type_list[def_type_index] >= 1.5:
                battle_action = Action.SWAP
            else:
                battle_action = Action.ATTACK
            
        elif self.ai_type == PokeTeam.AI.RANDOM:                
            random_action = RandomGen.randint(1,4)
            if self.heals_avail <= 0:
                while random_action == 3:
                    random_action = RandomGen.randint(1,4)
            battle_action = Action(random_action)
            
        else:
            user_choice = int(input("1. ATTACK, 2. SWAP, 3. HEAL, 4. SPECIAL\nPlease choose an action: "))
            battle_action = Action(user_choice)  

        return battle_action

    # added method
    def pokedex_ordering(self, a_team: ArraySortedList):     # similar to bubble sort
        """
            PRECONDITIONS:
            [NONE]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            PARAMETERS:
            Object instantiated from PokeTeam
            a_team[ArraySortedList]: a team of pokemons
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            Used to order pokemons based on the index determined in POKEDEX_ORDER
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [NONE]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(n^3), nested for loops where it repeats as many times as the length of a_team twice, and then 
            goes to get_initial_index() which has a complexity of O(n)
        """     
        for mark in range(len(a_team)-1, 0, -1):
            swapped = False
            for i in range(mark):
                poke_a = a_team[i].value
                poke_b = a_team[i+1].value
                if eval(f"poke_a." + self.crit) == eval(f"poke_b." + self.crit):
                    index_a = self.get_initial_index(poke_a)
                    index_b = self.get_initial_index(poke_b)
                
                    if index_a > index_b:
                        held = a_team[i].value #lst[i]   #swap places
                        
                        a_team[i].value = a_team[i+1].value
                        a_team[i+1].value = held
                        
    def get_initial_index(self, find_poke: PokemonBase) -> int:
        """
            PRECONDITIONS:
            [NONE]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            PARAMETERS:
            Object instantiated from PokeTeam
            find_poke[PokemonBase]: pokemon that which index needs to be found in the pokedex
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            FUNCTION DESCRIPTION:
            Finds the index of the pokemon's type in the pokedex
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            initial_index[integer]: index of the pokemon in the pokedex
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(n), goes through the list POKEDEX_ORDER
        """  
        for initial_index in range(len(self.POKEDEX_ORDER)):
            matched_poke = self.POKEDEX_ORDER[initial_index]()
            if type(find_poke) == type(matched_poke):
                return initial_index

    @classmethod
    def leaderboard_team(cls):
        pass

if __name__ == "__main__":
    a = PokeTeam.random_team("a", 0, 5)
    print(a)


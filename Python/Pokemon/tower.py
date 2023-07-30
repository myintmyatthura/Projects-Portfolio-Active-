from __future__ import annotations

__author__ = "Scaffold by Jackson Goerner, Code by Myint Myat Thura, Lau Ka-Kiat, Wong Heng Yew, Tay Chean Hao"
from typing import Set
from poke_team import Criterion, PokeTeam
from battle import Battle
from random_gen import RandomGen
from node import Node
from linked_list import LinkedList, LinkedListIterator
from bset import BSet

class BattleTower(Battle):
    """
        CLASS DESCRIPTION:
        BattleTower Class for creating a battle tower with multiple trainers within that can be challenged
        by the user.
        ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
        CLASS VARIABLES:
        Declares several attributes for every object related to BattleTower Class.
            _____________________________________________________________
            |defending_team |lives  |challenger_team    |enemy_team     |
            |_______________|_______|___________________|_______________|
            |None           |None   |None               |None           |
            |_______________|_______|___________________|_______________|
            where defending_team = None, lives = None, challenger_team = None, enemy_team = None    

    """
    defending_team = None
    lives = None
    challenger_team = None
    enemy_team = None

    def __init__(self, battle: Battle|None=None) -> None:
        """
            PRECONDITIONS:
            battle parameter must be an object instantiated from Battle or its subclasses
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            PARAMETERS:
            objects instantiated:
            -   battle[Battle]|None[None]: an instance of Battle class that will be used for all battles 
                                           occuring in the BattleTower
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            __init__ magic method to initialise the BattleTower, with several attributes:
                -   defending_team = None
                -   lives = None
                -   challenger_team = None
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [NONE]: its an __init__ function
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST CASE AND WORST CASE:
            O(1), only assigns values to variables.
        """
        Battle.__init__(self)
        self.defending_team = None
        self.lives = None
        self.challenger_team = None
        self.lives = 0

    def set_my_team(self, team: PokeTeam) -> None:
        """
            PRECONDITIONS:
            team parameter must be an object related to PokeTeam Class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            PARAMETERS:
            objects instantiated:
            -   team[PokeTeam]: the trainer's team that will be challenging the battle tower.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            Assigns the challenger_team variable with team from parameter.
            __...___...___...____...___...___...___...____...___...___...
            RETURN:
            [NONE]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST CASE AND WORST CASE:
            O(1), only assigns values to a variable.
        """

        self.challenger_team = team


    def generate_teams(self, n: int) -> None:
        """
            PRECONDITIONS:
            n parameter must be an integer.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            PARAMETERS:
            objects instantiated:
            -   n[integer]: number of defending teams to be generated.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            -   Generates n number of teams to defend the battle tower.
            -   Every defending_team that is generated will be inserted into enemy_team, a linked list.
            -   Lives for each of the defending_team will also be randomly generated between 2 and 10, and 
                stored in linked list called lives.
            __...___...___...____...___...___...___...____...___...___...___...___...___...___...___...___...
            RETURN:
            [NONE]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST CASE AND WORST CASE:
            O(n), where n is the number of defending teams in the battle tower.
        """

        # n will be the number of teams you want
        # linked list will be made with space for n number of teams
        # n will be the number of teams you want
        # linked list will be made with space for n number of teams
        if type(n) != int:
            raise TypeError(f"n is not an integer")

        self.enemy_team = LinkedList()
        self.lives = LinkedList()

        # depending on the number of teams, lives will be assigned to each team
        # this is implemented using a list and each life will be appended accordingly
        # if there were 4 teams,the lives list would appear as below
        # [1, 4, 6, 2]
        # [t1,t2,t3,t4]
        # depending on the number of teams, teams will be added to a linked list
        for i in range(n):
            battle_mode = RandomGen.randint(0,1) # set battle mode for random team
            self.defending_team = PokeTeam.random_team(i, battle_mode)
            self.enemy_team.insert(i, self.defending_team)
            self.lives.insert(i, RandomGen.randint(2,10))
            # [t1,t2,t3,t4]
    def __iter__(self):
        """
            PRECONDITIONS:
            [NONE]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            PARAMETERS:
            objects instantiated.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            -   calls the init function for BattleTowerIterator Class for the object instantiated.
            __...___...___...____...___...___...___...____...___...___...___...___...___...___...___...___...
            RETURN:
            self[BattleTowerIterator]: object of BattleTowerIterator
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST CASE AND WORST CASE:
            O(1), only initialises an object from BattleTowerIterator.
        """

        return BattleTowerIterator(self)

    
    
class BattleTowerIterator:
    """
        CLASS DESCRIPTION:
        BattleTowerIterator Class is used to create an object from BattleTower, which can then be integrated
        through.
    """
    def __init__(self, battle: Battle|None=None): # iterating battle tower
        """
            PRECONDITIONS:
            battle parameter must be an object instantiated from Battle or its subclasses
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            PARAMETERS:
            objects instantiated:
            -   battle[Battle]|None[None]: an instance of Battle class that will be used for all battles 
                                           occuring in the BattleTower
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            __init__ magic method to initialise an object from BattleTowerIterator with several attributes:
            -   table = battle
            -   index = 0
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [NONE]: its an __init__ function
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST CASE AND WORST CASE:
            O(1), only assigns values to variables.
        """
        self.iter_battle = battle # BattleTower actually with enemy team and lives and challenger_team
        self.index = 0
        self.tower_lost = None

    def __next__(self) -> str:
        """
            PRECONDITIONS:
            [NONE]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            PARAMETERS:
            objects instantiated
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            __next__ magic method to go to the next element within the linked list.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            ret[]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST CASE AND WORST CASE:
            O(1), only assigns values to variables.
        """
        if not self.has_next(): # if index has reached the endd of tower team
            self.reset() # index goes back to 0 , or the beginning of the tower team
        if self.tower_lost == True: # if our team has lost its battle in the tower
            raise StopIteration
        else:
            ret = self.next() # call the battle
            return ret

    def has_next(self) -> bool:
        """
            PRECONDITIONS:
            [NONE]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            PARAMETERS:
            objects instantiated
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            Checks whether self.index is less than the length of the list to check if the list can be further
            transversed.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            Returns a boolean.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST CASE AND WORST CASE:
            O(1), only assigns values to variables.
        """
        return self.index < len(self.table.enemy_team)

    def reset(self) -> None:
        """
            PRECONDITIONS:
            [NONE]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            PARAMETERS:
            objects instantiated
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            Resets the index to 0.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [NONE]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST CASE AND WORST CASE:
            O(1), only assigns values to variables.
        """
        self.index = 0

    def next(self,my_iterable:int) -> str:
        """
        PARAMETERS:
        my_iterable[int]: selects the enemy_team to battle in the battle tower.
        ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
        METHOD DESCRIPTION:
        -   Battles one of the teams based on my_iterable within the BattleTower with the challenger_team.
            -   When the player wins the battle, the corresponding life for the team in enemy_team will be
                deducted.
            -   When a defending team has lost their lives, remove them from the lives list and the enemies
                list.
            -   When the player loses the battle, the gauntlet run will end, and a StopIteration will be 
                raised.
        When all of the defending_teams in enemy_team has lost all of their lives, the tower ends, and 
        the player wins.
        ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
        RETURN:
        Will return battle results after every iteration as tuples.
        (res, me, other_team, lives)
        ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
        COMPLEXITY FOR BEST CASE AND WORST CASE:
        O(B), where B is the complexity of the battle.
        ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
    """ 
        if not self.has_next():
            raise ValueError("Peeking at end of iterable.")

        opposing_team = self.iter_battle.enemy_team[self.index] # gets a team off enemy team linked list
        the_chall_team = self.iter_battle.challenger_team # our team for challenge

        the_outcome = self.iter_battle.battle(the_chall_team, opposing_team) # battle

        opposing_team_lives = self.iter_battle.lives[self.index] # opposing team lives after battle
        tower_team_post_battle = self.iter_battle.enemy_team # tower team after battle
        self.iter_battle.enemy_team[self.index].regenerate_team() # regenerate the tower team
        challenged_team_post_battle = self.iter_battle.challenger_team # our team after battle
        # if challenger wins
        if the_outcome == 1:
            self.iter_battle.lives[self.index] -= 1 # decrement oppsing team lives by 1
            if self.iter_battle.lives[self.index] == 0: # if the opposing team has no more lives
                self.iter_battle.enemy_team.delete_at_index(self.index) # the opposing team is removed from the tower team
                self.iter_battle.lives.delete_at_index(self.index) # the lives of opposing team is removed

            opposing_team_lives = self.iter_battle.lives[self.index] # readjust lives of opposing team
            self.iter_battle.challenger_team.regenerate_team() # regenerate our team for next battle
            print("won")
            self.index += 1 # increment index to move to next opposing team
            self.iter_battle.battle_outcome = None # default the battle outcome back to None
        else:
            # if challenger loses, break because tower has ended
            print("tower has ended")
            self.tower_lost = True # a boolean value to stop iteration

        return f"({the_outcome}, {challenged_team_post_battle}, {tower_team_post_battle}, {opposing_team_lives})"
                
    
    def avoid_duplicates(self) -> None:
                """
        PARAMETERS:
        Object instantiated.
        ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
        METHOD DESCRIPTION:
        Removes trainers that have multiple pokemon of the same type by storing them in sets.
        -   as sets by nature don't allow duplicates.
        If length of the set is different from the length of the enemy_team linked list, the set will be cleared
        of all the elements and the respective team will be removed from enemyteam LinkedList. 
        ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
        RETURN:
        [NONE]
        ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
        COMPLEXITY FOR BEST CASE AND WORST CASE:
        O(N*P), where N is the number of trainers and P is the limit on the number of pokemon per team.
        ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
    """
        index = 0
        #temp_set = BSet(len(BattleTower.enemy_team))
        temp_set = BSet(len(self.iter_battle.enemy_team))
        for team in self.iter_battle.enemy_team:
            # for team in [t1,t2,t3,t4]
            for pokemon in team:
                # set = [t1]
                temp_set.add(pokemon)
            # if set length {t1} = list [t1]
            if len(temp_set) == len(self.iter_battle.enemy_team[index]): #BattleTower.self.enemy_team[index]
                # remove team from set
                # index += 1
                temp_set.clear()
            else:
                # remove team from set
                temp_set.clear()
                # remove team from list
                self.iter_battle.enemy_team.delete_at_index(index)
            index += 1
        

    def sort_by_lives(self):
        # 1054
        raise NotImplementedError()








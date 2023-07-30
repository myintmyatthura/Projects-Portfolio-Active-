from __future__ import annotations

__author__ = "Scaffold by Jackson Goerner, Code by Myint Myat Thura, Lau Ka-Kiat, Wong Heng Yew, Tay Chean Hao"

from typing import TypeVar, Generic
from abc import ABC, abstractmethod
from random_gen import RandomGen
T = TypeVar('T')


class PokemonBase(ABC, Generic[T]):
    """
        CLASS DESCRIPTION:
        PokemonBase Abstract class that has POKEMON_TYPE[list] and POKEMON_MULTIPLIERS[list] nested list 
        declared as class variables. This class is used to store the statistics of a pokemon that do not vary
    """
    POKEMON_TYPE = ["Fire","Grass","Water","Ghost","Normal"]
    POKEMON_MULTIPLIERS = [[1,2,0.5,1,1],[0.5,1,2,1,1],[2,0.5,1,1,1],[1.25,1.25,1.25,2,0],[1.25,1.25,1.25,0,1]]


    def __init__(self, hp: int, poke_type: str) -> None:
        """ 
            PRECONDITIONS: 
            -   hp parameter must be an integer
            -   poke_type parameter must be a string equal to one of the elements within POKEMON_TYPE
            -   function is an init function, therefore only used when initialising an object
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            PARAMETERS:
            objects instantiated:
            -   hp[integer]: health or hit points of the pokemon
            -   poke_type[string]: type of the pokemon, consisting of Fire, Grass, Water, Ghost, Normal
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            FUNCTION DESCRIPTION:
            -   __init__ magic method to initialise hp and pokemon type statistics of a pokemon
            -   hp and type of the pokemon will be passed into the init function,
            -   rest of the stats such as level, defence, attack_damage, speed will be defaulted
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [NONE]: its an __init__ function
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all, only assigns values to variables and check for precondtions
        """    
        if hp < 0:
            raise ValueError("positive please")
        if poke_type not in PokemonBase.POKEMON_TYPE:
            raise TypeError("poke_type input is not valid")
            
        self.type = poke_type # use in status effects
        self.level = None # base_level
        self.max_hp = hp # save hp of pokemon for future reference on healing
        self.hp = self.max_hp
        self.state = None # the status effect name
        self.has_evolution = None # this points to evolved pokemon
        self.evolves_at = None # this points to which level pokemon can evolve

    def is_fainted(self) -> bool:
        """
            PRECONDITIONS:
            
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            PARAMETERS:
            The instances of PokemonBase
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            -   checks whether self.hp is less than or equals to 0 and returns a boolean value
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [boolean]: True if self.hp<=0 , otherwise False
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all, only returns a boolean value
        """  
        return self.hp <= 0 
    
    def level_up(self) -> None: 
        """
            PARAMETERS:
            The instances of PokemonBase
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            -   levels up the pokemon by 1
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [NONE]: does not return anything
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all and level increases by 1
        """
        self.level += 1
    
    def heal(self) -> None:
        """
            PARAMETERS:
            The instances of PokemonBase
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            Method DESCRIPTION:
            -   increases the pokemon's current hp to the max hp
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [NONE]: does not return anything
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all, just reassigning hp to max hp
        """
        self.hp = self.max_hp
        
    def get_hp(self) -> int:
        """
            PARAMETERS:
            The instances of PokemonBase
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            Method DESCRIPTION:
            -   gets the pokemon's hp
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            self.hp[integer]: returns the pokemon's hp
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all as it only returns pokemon's hp
        """
        return self.hp
    
    def get_level(self) -> int:
        """
            PARAMETERS:
            The instances of PokemonBase
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            M DESCRIPTION:
            -   gets the pokemon's level
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            self.level[integer]: returns the pokemon's level
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all as it returns pokemon's level
        """
        return self.level

    @abstractmethod
    def get_speed(self) -> int: 
        """
        An abstract method to speed stat of a pokemon because speed is calculated differently for each pokemon 
        """
        pass

    @abstractmethod
    def get_attack_damage(self) -> int: 
        """
        An abstract method to get attack damage stat of a pokemon because attack damage is calculated differently for each pokemon
        """
        pass

    @abstractmethod
    def get_defence(self) -> int: 
        """
        An abstract method to get defence stat of a pokemon because defence is calculated differently for each pokemon 
        """
        pass

    def lose_hp(self, lost_hp: int) -> None:
        """
            PARAMETERS:
            The instances of PokemonBase class
            lost_hp[integer]: the amount of hp lost by the pokemon
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            -   decreases the current hp of the pokemon by the amount of hp lost[lost_hp]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [NONE]: does not return anything
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), mathematical calculation of hp decreasing due to lost_hp
        """
        self.hp -= lost_hp

    @abstractmethod
    def defend(self, damage: int) -> None:
        """
            An abstract method to calculate defence for the defending pokemon
            based on the damage imposed from the attacking pokemon and some conditions that influences
            the defence calculation 
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), only check for precondition for damage amount
        """
        if damage < 0: #precondition: damage must be >= 0
            raise ValueError("damage needs to be more than or equal to 0 ")


    def inflict_status_effect(self, other: PokemonBase) -> None:
        """
            PARAMETERS:
            The instances of PokemonBase class
            other[PokemonBase]: an instance of class PokemonBase, which is a pokemon
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            FUNCTION DESCRIPTION:
            -   checks the type of the attacking pokemon, and inflicts a status effect on the defending pokemon
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [NONE]: does not return anything
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), only if and elif conditions of checking pokemon type and assigning a state based on type
        """
        if self.type == "Fire":
            other.state = "Burn"
        elif self.type == "Grass":
            other.state = "Poison"
        elif self.type == "Water":
            other.state = "Paralysis"
        elif self.type == "Ghost":
            other.state = "Sleep"
        elif self.type == "Normal":
            other.state = "Confusion"

    def attack(self, other: PokemonBase):
        """
            PARAMETERS:
            The instances of PokemonBase class
            other[PokemonBase]: the opposing pokemon currently fighting
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            Attacks the opposing pokemon using the current selected pokemon.
            -   Checks for status effects afflicted on the attacking pokemon, where:
                -   if attacking pokemon has status effect [SLEEP], the function is passed
                -   if attacking pokemon has status effect [CONFUSED], there is a 50% chance it will attack itself.
            -   Checks whether attacking pokemon will be effective against the opposing pokemon
                -   certain pokemon types will deal increased or decreased damage to other specific pokemon types:
                    _____________________________________________________________
                    |AT type/DEF type   |Fire   |Grass  |Water  |Ghost  |Normal |
                    |___________________|_______|_______|_______|_______|_______|
                    |Fire               |1      |2      |0.5    |1      |1      |
                    |Grass              |0.5    |1      |2      |1      |1      |
                    |Water              |2      |0.5    |1      |1      |1      |
                    |Ghost              |1.25   |1.25   |1.25   |2      |0      |
                    |Normal             |1.25   |1.25   |1.25   |0      |1      |
                    |___________________|_______|_______|_______|_______|_______|
            -   Perform attack and lose hp due to any side effects
            -   Checks whether attacking pokemon would inflict status effects on attacked pokemon  
                -   0.2 chance of inflicting status effects based on attacking pokemon's pokemon_type
                    -   (BURN) pokemon loses one hp per turn, and effective attack is halved
                    -   (POISON) pokemon loses an additional 3 hp
                    -   (SLEEP) pokemon falls asleep, causing them to always fail to attack
                    -   (CONFUSION) pokemon has a 50% chance of attacking themselves instead of attacking the opponent.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [NONE]: does not return anything
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST CASE:
            O(n), string comparison if pokemon state equals to "Sleep", n being the length of the string
            COMPLEXITY FOR WORST CASE:
            O(n^2), n^2 being the biggest factor in this method which happens in the two for-loops 
            which iterates len(PokemonBase.POKEMON_TYPE) and comparing pokemon type as strings
        """    
        # Step 1: Status effects on attack damage / redirecting attacks
        # Step 2: Do the attack
        # Step 3: Losing hp to status effects
        # Step 4: Possibly applying status effects

        #Step 1:
        #if self.state == "Sleep": # if a pokemon is asleep, stop the attack
        #    pass
        
        if self.state == "Confusion": # redirecting attacks
            if RandomGen.random_chance(0.5) == True:
                other = self # make other as the attacking pokemon itself
        if self.state != "Sleep":
            attacking_type = self.type
            defending_type = other.type

            for i in range(len(PokemonBase.POKEMON_TYPE)):
                if attacking_type == PokemonBase.POKEMON_TYPE[i]:
                    attacking_type_list = PokemonBase.POKEMON_MULTIPLIERS[i] # retrieve the multipliers based on pokemon type
                    break

            for i in range(len(PokemonBase.POKEMON_TYPE)):
                if defending_type == PokemonBase.POKEMON_TYPE[i]:
                    def_type_index = i # obtain index to extract the multiplier value
                    break 

            # Step 2
            effective_attack = self.attack_damage * attacking_type_list[def_type_index] # calculate attack
        
            if self.state == "Burn":
                effective_attack = effective_attack // 2

            other.defend(effective_attack) # calculate defend

            # Step 3
            if self.state == "Burn":
                self.hp -= 1
            if self.state == "Poison":
                self.hp -= 3

            # Step 4
            if RandomGen.random_chance(0.2) == True:
                self.inflict_status_effect(other)

    @abstractmethod
    def get_poke_name(self) -> str:
        """
            An abstract method to get pokemon name because every pokemon has a unique name
        """
        pass

    @abstractmethod
    def __str__(self) -> str:
        """
            An abstract method to form a string detailing a pokemon stats.
            It is under abstract as each pokemon has different stats to return, mainly poke_name
            which is unique and the poke_name is not instantiated under PokemonBase abstract class
        """
        pass
        

    def should_evolve(self) -> bool:
        """
            PARAMETERS:
            The instances of PokemonBase class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            checks whether pokemon is awake and whether it can evolve
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [boolean]: True if both conditions are True, otherwise False 
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), assigning flag through comparing two fucntions of O(1) gives O(1)
        """
        return self.can_evolve() == True and self.is_fainted() == False

    def can_evolve(self) -> bool:
        """
            PARAMETERS:
            The instances of PokemonBase class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            FUNCTION DESCRIPTION:
            checks whether pokemon qualifies for an evolution, else it returns false
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [boolean]: True if can_evolve is True and not fainted, otherwise False
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), the comparisons and if conditions are O(1) 
            Even for best case of failing the the first condition, it is still O(1) for returning False 
        """
        return (self.has_evolution != None) and (self.level >= self.evolves_at) # return is conditions are met 

    def get_evolved_version(self) -> PokemonBase:
        """
            PARAMETERS:
            The instances of PokemonBase class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            -   checks whether pokemon should evolve, and if True evolves the pokemon while keeping the health
                difference in check, as well as carrying over their status effect if they were inflicted
            -   if pokemon shouldn't evolve, raise an Exception that the pokemon can't evolve/can't evolve yet
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            object[PokemonBase]  
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), comparison to a function of O(1), O(1) mathematical operations, 
            returning evolved PokemonBase and raising exception are all O(1) 
        """
        if self.should_evolve() == True:
            status = self.state
            diff = self.max_hp - self.hp # calculate health difference
            self = self.has_evolution # assign new evolved pokemon 
            self.hp = self.max_hp - diff # update hp of evolved pokemon 
            self.state = status
            return self
        else:
            raise Exception("This Pokemon can't evolve/can't evolve yet.")

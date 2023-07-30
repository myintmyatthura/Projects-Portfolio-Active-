from __future__ import annotations

__author__ = "Scaffold by Jackson Goerner, Code by Myint Myat Thura, Lau Ka-Kiat, Wong Heng Yew, Tay Chean Hao"

from pokemon_base import PokemonBase 
from random_gen import RandomGen

class Charizard(PokemonBase):
    """
        CLASS DESCRIPTION:
        Charizard(Parent PokemonBase) class with class variables pokemon_name, pokemon_type, base_level, base_hp,
        base_attack_damage, base_speed and base_defence declared and defaulted
    """
    pokemon_name = "Charizard"
    pokemon_type = "Fire"
    base_level = 3
    base_hp = 12
    base_attack_damage = 10
    base_speed = 9
    base_defence = 4
    
    def __init__(self) -> None:
        """
            PARAMETERS:
            The instances of Charizard subclass with inherited members from PokemonBase parent class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            FUNCTION DESCRIPTION:
            __init__ function to initialise instances of class Charizard with parent class PokemonBase while
            assigning Charizard class specific attributes to the object with increased stats compared to the
            previous evolution
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [NONE]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all as we are inheriting attributes and instances from parent class and doing
            assignment to instances with some containing mathematical calculation
        """
        PokemonBase.__init__(self, Charizard.base_hp, Charizard.pokemon_type)
        self.name = self.pokemon_name
        self.level = self.base_level # base_level
        self.max_hp = self.base_hp + (1 * self.level)
        self.hp = self.max_hp
        self.attack_damage = self.base_attack_damage + (2 * self.level)
        self.speed = self.base_speed + (1 * self.level)
        self.defence = self.base_defence

    def level_up(self) -> None:
        """
            PARAMETERS:
            The instances of Charizard subclass with inherited members from PokemonBase parent class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            This adds on the base method of level_up() derived from the parent class PokemonBase. 
            It has recalculation for stats needed for adjustment as incrementing Charizard level can influence its stats 
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [NONE]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all as we are inheriting attributes and instances from parent class and doing
            assignment to instances with some containing mathematical calculation
        """
        PokemonBase.level_up(self)
        stat_increase = 1 * self.level  # since all the stats for charmander increase by same amount, create var for ease
        prev_max_hp = self.max_hp
        prev_hp = self.hp
        diff = prev_max_hp - prev_hp
        self.max_hp = self.base_hp + stat_increase
        self.hp = self.max_hp - diff
        self.attack_damage = self.base_attack_damage + (2 * self.level)
        self.speed = self.base_speed + stat_increase

    def get_speed(self) -> int:
        """
            PARAMETERS:
            The instances of Charizard subclass with inherited members from PokemonBase parent class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            This overrides the abstract method derived from the parent class PokemonBase. 
            It returns speed of Charizard and halves it if Charizard state is under "Paralysis" as
            a status effect inflicted upon by an attacking pokemon
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [int] self.speed
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST CASE:
            O(1), if the first letter of state is different or state has not been declared O(1) and return speed O(1)
            COMPLEXITY FOR WORST CASE:
            O(n), n being the string to be compared with "Paralysis" 
            The return and mathematical calculatin of speed are O(1) 
        """
        if self.state == "Paralysis":
            return self.speed // 2
        else:
            return self.speed

    def get_attack_damage(self) -> int:
        """
            PARAMETERS:
            The instances of Charizard subclass with inherited members from PokemonBase parent class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            This overrides the abstract method derived from the parent class PokemonBase. 
            It returns attack damage of Charizard
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [int] self.attack_damage
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all as we are returning attack damage
        """
        return self.attack_damage

    def get_defence(self) -> int:
        """
            PARAMETERS:
            The instances of Charizard subclass with inherited members from PokemonBase parent class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            This overrides the abstract method derived from the parent class PokemonBase. 
            It returns defence of Charizard
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [int] self.defence
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all as we are returning defence
        """
        return self.defence

    def defend(self,damage: int) -> None:
        """
            PARAMETERS:
            The instancecs of Charizard subclass with inherited members from PokemonBase parent class
            damage[integer]: damage dealt by attacking pokemon
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            Overrides abstract method defend() from PokemonBase 
            Returns reamaining hp lost from damage 
            If damage is greater than Charizard's defence, damage taken 
            is multiplied by 2, else damage taken is same as damage dealt
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [NONE]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), the precondition checking for damage < 0 is O(1), if and else condition O(1), 
            comparing dammage > defence O(1), and decreasing hp based on damage given O(1)
        """
        #PokemonBase.defend(self, 0)
        if damage > self.get_defence(): # i think self.defence is fine
            self.lose_hp(damage * 2)
        else:
            self.lose_hp(damage)
    
    def get_poke_name(self) -> str:
        """
            PARAMETERS:
            The instances of Charizard subclass with inherited members from PokemonBase parent class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            This overrides the abstract method derived from the parent class PokemonBase. 
            It returns its name: Charizard
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [int] self.name
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all as we are returning name 
        """
        return self.name

    def __str__(self) -> str:
        """
            PARAMETERS:
            The instances of Charizard subclass with inherited members from PokemonBase parent class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            This overrides the abstract method __str__() from PokemonBase 
            It puts together a string of pokemon level, pokemon name and pokemon's hp
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            f'string[string]: returns a string containing pokemon level, pokemon name and pokemon's hp
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(n), where n is the string created based on pokemon level, name and hp through formatting
        """
        return f"LV. {self.get_level()} {self.get_poke_name()}: {self.get_hp()} HP"


class Charmander(PokemonBase):
    """
        CLASS DESCRIPTION:
        Charmander(Parent PokemonBase) class with class variables pokemon_name, pokemon_type, base_level, base_hp,
        base_attack_damage, base_speed and base_defence declared and defaulted
    """
    pokemon_name = "Charmander"
    pokemon_type = "Fire"
    base_level = 1
    base_hp = 8 
    base_attack_damage = 6 
    base_speed = 7 
    base_defence = 4
    
    def __init__(self):
        """
            PARAMETERS:
            The instances of Charmander subclass with inherited members from PokemonBase parent class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            FUNCTION DESCRIPTION:
            __init__ function to initialise instances of class Charmander with parent class PokemonBase while
            assigning Charmander class specific attributes to the object 
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [NONE]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all as we are inheriting attributes and instances from parent class and doing
            assignment to instances with some containing mathematical calculation
        """
        PokemonBase.__init__(self, Charmander.base_hp, Charmander.pokemon_type) # maybe the word "FIRE" is enough
        self.name = self.pokemon_name
        self.level = self.base_level # base_level
        self.max_hp = self.base_hp + (1 * self.level)
        self.hp = self.max_hp
        self.attack_damage = self.base_attack_damage + (1 * self.level)
        self.speed = self.base_speed + (1 * self.level)
        self.defence = self.base_defence
        self.has_evolution = Charizard()
        self.evolves_at = Charizard.base_level

    def level_up(self) -> None:
        """
            PARAMETERS:
            The instances of Charmander subclass with inherited members from PokemonBase parent class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            This adds on the base method of level_up() derived from the parent class PokemonBase. 
            It has recalculation for stats needed for adjustment as incrementing Charmander level can influence its stats 
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [NONE]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all as we are inheriting attributes and instances from parent class and doing
            assignment to instances with some containing mathematical calculation
        """
        PokemonBase.level_up(self)
        stat_increase = 1 * self.level  # since all the stats for charmander increase by same amount, create var for ease
        prev_max_hp = self.max_hp
        prev_hp = self.hp
        diff = prev_max_hp - prev_hp
        self.max_hp = self.base_hp + stat_increase
        self.hp = self.max_hp - diff
        self.attack_damage = self.base_attack_damage + stat_increase
        self.speed = self.base_speed + stat_increase

    def get_speed(self) -> int:
        """
            PARAMETERS:
            The instances of Charmander subclass with inherited members from PokemonBase parent class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            This overrides the abstract method derived from the parent class PokemonBase. 
            It returns speed of Charmander and halves it if Charmander state is under "Paralysis" as
            a status effect inflicted upon by an attacking pokemon
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [int] self.speed
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST CASE:
            O(1), if the first letter of state is different or state has not been declared O(1) and return speed O(1)
            COMPLEXITY FOR WORST CASE:
            O(n), n being the string to be compared with "Paralysis" 
            The return and mathematical calculatin of speed are O(1) 
        """
        if self.state == "Paralysis":
            return self.speed // 2
        else:
            return self.speed

    def get_attack_damage(self) -> int:
        """
            PARAMETERS:
            The instances of Charmander subclass with inherited members from PokemonBase parent class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            This overrides the abstract method derived from the parent class PokemonBase. 
            It returns attack damage of Charmander
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [int] self.attack_damage
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all as we are returning attack damage
        """
        return self.attack_damage

    def get_defence(self) -> int:
        """
            PARAMETERS:
            The instances of Charmander subclass with inherited members from PokemonBase parent class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            This overrides the abstract method derived from the parent class PokemonBase. 
            It returns defence of Charmander
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [int] self.defence
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all as we are returning defence
        """
        return self.defence

    def defend(self,damage: int) -> None:
        """
            PARAMETERS:
            The instancecs of Charmander subclass with inherited members from PokemonBase parent class
            damage[integer]: damage dealt by attacking pokemon
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            Overrides the abstract method defend() from PokemonBase 
            Returns reamaining hp lost from damage 
            If damage is greater than Charizard's defence, damage taken is same as damage dealt 
            , else damage taken is halved
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [NONE]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), the precondition checking for damage < 0 is O(1), if and else condition O(1), 
            comparing dammage > defence O(1), and decreasing hp based on damage given O(1)
        """
        #PokemonBase.defend(self, 0)
        if damage > self.get_defence(): # i think self.defence is fine
            self.lose_hp(damage)
        else:
            self.lose_hp(damage//2)

    def get_poke_name(self) -> str:
        """
            PARAMETERS:
            The instances of Charmander subclass with inherited members from PokemonBase parent class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            This overrides the abstract method derived from the parent class PokemonBase. 
            It returns its name: Charmander
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [int] self.name
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all as we are returning name 
        """
        return self.name

    def __str__(self) -> str:
        """
            PARAMETERS:
            The instances of Charmander subclass with inherited members from PokemonBase parent class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            This overrides the abstract method __str__() from PokemonBase 
            It puts together a string of pokemon level, pokemon name and pokemon's hp
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            f'string[string]: returns a string containing pokemon level, pokemon name and pokemon's hp
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(n), where n is the string created based on pokemon level, name and hp through formatting
        """
        return f"LV. {self.get_level()} {self.get_poke_name()}: {self.get_hp()} HP"

class Venusaur(PokemonBase):
    """
        CLASS DESCRIPTION:
        Venusaur(Parent PokemonBase) class with class variables pokemon_name, pokemon_type, base_level, base_hp,
        base_attack_damage, base_speed and base_defence declared and defaulted
    """
    pokemon_name = "Venusaur"
    pokemon_type = "Grass"
    base_level = 2
    base_hp = 20
    base_attack_damage = 5
    base_speed = 3
    base_defence = 10

    def __init__(self):
        """
            PARAMETERS:
            The instances of Venusaur subclass with inherited members from PokemonBase parent class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            FUNCTION DESCRIPTION:
            __init__ function to initialise instances of class Venusaur with parent class PokemonBase while
            assigning Venusaur class specific attributes to the object with increased stats compared to the
            previous evolution
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [NONE]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all as we are inheriting attributes and instances from parent class and doing
            assignment to instances with some containing mathematical calculation
        """
        PokemonBase.__init__(self, Venusaur.base_hp, Venusaur.pokemon_type)
        self.name = self.pokemon_name
        self.level = self.base_level
        self.max_hp = self.base_hp + (self.level // 2)
        self.hp = self.max_hp
        self.attack_damage = self.base_attack_damage
        self.speed = self.base_speed + (self.level // 2)
        self.defence = self.base_defence
    
    def level_up(self) -> None:
        """
            PARAMETERS:
            The instances of Venusaur subclass with inherited members from PokemonBase parent class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            This adds on the base method of level_up() derived from the parent class PokemonBase. 
            It has recalculation for stats needed for adjustment as incrementing Venusaur level can influence its stats 
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [NONE]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all as we are inheriting attributes and instances from parent class and doing
            assignment to instances with some containing mathematical calculation
        """
        PokemonBase.level_up(self)
        stat_increase = self.level // 2
        prev_max_hp = self.max_hp
        prev_hp = self.hp
        diff = prev_max_hp - prev_hp
        self.max_hp = self.base_hp + stat_increase
        self.hp = self.max_hp - diff
        self.speed = self.base_speed + stat_increase

    def get_speed(self) -> int:
        """
            PARAMETERS:
            The instances of Venusaur subclass with inherited members from PokemonBase parent class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            This overrides the abstract method derived from the parent class PokemonBase. 
            It returns speed of Venusaur and halves it if Venusaur state is under "Paralysis" as
            a status effect inflicted upon by an attacking pokemon
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [int] self.speed
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST CASE:
            O(1), if the first letter of state is different or state has not been declared O(1) and return speed O(1)
            COMPLEXITY FOR WORST CASE:
            O(n), n being the string to be compared with "Paralysis" 
            The return and mathematical calculatin of speed are O(1) 
        """
        if self.state == "Paralysis":
            return self.speed // 2
        else:
            return self.speed

    def get_attack_damage(self) -> int:
        """
            PARAMETERS:
            The instances of Venusaur subclass with inherited members from PokemonBase parent class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            This overrides the abstract method derived from the parent class PokemonBase. 
            It returns attack damage of Venusaur
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [int] self.attack_damage
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all as we are returning attack damage
        """

        return self.attack_damage

    def get_defence(self) -> int:
        """
            PARAMETERS:
            The instances of Venusaur subclass with inherited members from PokemonBase parent class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            This overrides the abstract method derived from the parent class PokemonBase. 
            It returns defence of Venusaur
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [int] self.defence
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all as we are returning defence
        """
        return self.defence

    def defend(self, damage: int) -> None:
        """
            PARAMETERS:
            The instancecs of Venusaur subclass with inherited members from PokemonBase parent class
            damage[integer]: damage dealt by attacking pokemon
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            Overrides abstract method defend() from PokemonBase 
            Returns reamaining hp lost from damage 
            If damage is greater than Venusaur's defence + 5, damage taken 
            is equal to damage dealt, else damage taken is half of damage dealt
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [NONE]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), the precondition checking for damage < 0 is O(1), if and else condition O(1), 
            comparing dammage > defence O(1), and decreasing hp based on damage given O(1)
        """
        #PokemonBase.defend(self, 0)
        if damage > (self.get_defence() + 5):
            self.lose_hp(damage)
        else:
            self.lose_hp(damage // 2)

    def get_poke_name(self) -> str:
        """
            PARAMETERS:
            The instances of Venusaur subclass with inherited members from PokemonBase parent class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            This overrides the abstract method derived from the parent class PokemonBase. 
            It returns its name: Venusaur
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [int] self.name
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all as we are returning name 
        """
        return self.name

    def __str__(self) -> str:
        """
            PARAMETERS:
            The instances of Venusaur subclass with inherited members from PokemonBase parent class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            This overrides the abstract method __str__() from PokemonBase 
            It puts together a string of pokemon level, pokemon name and pokemon's hp
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            f'string[string]: returns a string containing pokemon level, pokemon name and pokemon's hp
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(n), where n is the string created based on pokemon level, name and hp through formatting
        """
        return f"LV. {self.get_level()} {self.get_poke_name()}: {self.get_hp()} HP"

class Bulbasaur(PokemonBase):
    """
        CLASS DESCRIPTION:
        Bulbasaur(Parent PokemonBase) class with class variables pokemon_name, pokemon_type, base_level, base_hp,
        base_attack_damage, base_speed and base_defence declared and defaulted
    """
    pokemon_name = "Bulbasaur"
    pokemon_type = "Grass"
    base_level = 1
    base_hp = 12
    base_attack_damage = 5
    base_speed = 7
    base_defence = 5

    def __init__(self):
        """
            PARAMETERS:
            The instances of Bulbasaur subclass with inherited members from PokemonBase parent class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            FUNCTION DESCRIPTION:
            __init__ function to initialise instances of class Bulbasaur with parent class PokemonBase while
            assigning Bulbasaur class specific attributes to the object 
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [NONE]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all as we are inheriting attributes and instances from parent class and doing
            assignment to instances with some containing mathematical calculation
        """
        PokemonBase.__init__(self, Bulbasaur.base_hp, Bulbasaur.pokemon_type)
        self.name = self.pokemon_name
        self.level = self.base_level
        self.max_hp = self.base_hp + (1 * self.level)
        self.hp = self.max_hp
        self.attack_damage = self.base_attack_damage
        self.speed = self.base_speed + (self.level // 2)
        self.defence = self.base_defence
        self.has_evolution = Venusaur()
        self.evolves_at = Venusaur.base_level

    def level_up(self) -> None:
        """
            PARAMETERS:
            The instances of Bulbasaur subclass with inherited members from PokemonBase parent class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            This adds on the base method of level_up() derived from the parent class PokemonBase. 
            It has recalculation for stats needed for adjustment as incrementing Bulbasaur level can influence its stats 
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [NONE]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all as we are inheriting attributes and instances from parent class and doing
            assignment to instances with some containing mathematical calculation
        """
        PokemonBase.level_up(self)
        prev_max_hp = self.max_hp
        prev_hp = self.hp
        diff = prev_max_hp - prev_hp
        self.max_hp = self.base_hp + (1 * self.level)
        self.hp = self.max_hp - diff
        self.speed = self.base_speed + (self.level // 2)

    def get_speed(self) -> int:
        """
            PARAMETERS:
            The instances of Bulbasaur subclass with inherited members from PokemonBase parent class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            This overrides the abstract method derived from the parent class PokemonBase. 
            It returns speed of Bulbasaur and halves it if Bulbasaur state is under "Paralysis" as
            a status effect inflicted upon by an attacking pokemon
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [int] self.speed
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST CASE:
            O(1), if the first letter of state is different or state has not been declared O(1) and return speed O(1)
            COMPLEXITY FOR WORST CASE:
            O(n), n being the string to be compared with "Paralysis" 
            The return and mathematical calculatin of speed are O(1) 
        """
        if self.state == "Paralysis":
            return self.speed // 2
        else:
            return self.speed

    def get_attack_damage(self) -> int:
        """
            PARAMETERS:
            The instances of Bulbasaur subclass with inherited members from PokemonBase parent class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            This overrides the abstract method derived from the parent class PokemonBase. 
            It returns attack damage of Bulbasaur
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [int] self.attack_damage
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all as we are returning attack damage
        """
        return self.attack_damage

    def get_defence(self) -> int:
        """
            PARAMETERS:
            The instances of Bulbasaur subclass with inherited members from PokemonBase parent class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            This overrides the abstract method derived from the parent class PokemonBase. 
            It returns defence of Bulbasaur
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [int] self.defence
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all as we are returning defence
        """
        return self.defence

    def defend(self, damage: int) -> None:
        """
            PARAMETERS:
            The instancecs of Bulbasaur subclass with inherited members from PokemonBase parent class
            damage[integer]: damage dealt by attacking pokemon
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            Overrides abstract method defend() from PokemonBase 
            Returns reamaining hp lost from damage 
            If damage is greater than Venusaur's defence + 5, damage taken 
            is equal to damage dealt, else damage taken is half of damage dealt
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [NONE]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), the precondition checking for damage < 0 is O(1), if and else condition O(1), 
            comparing dammage > defence O(1), and decreasing hp based on damage given O(1)
        """
        #PokemonBase.defend(self, 0)
        if damage > (self.get_defence() + 5):
            self.lose_hp(damage)
        else:
            self.lose_hp(damage // 2)

    def get_poke_name(self) -> str:
        """
            PARAMETERS:
            The instances of Bulbasaur subclass with inherited members from PokemonBase parent class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            This overrides the abstract method derived from the parent class PokemonBase. 
            It returns its name: Bulbasaur
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [int] self.name
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all as we are returning name 
        """
        return self.name

    def __str__(self) -> str:
        """
            PARAMETERS:
            The instances of Bulbasaur subclass with inherited members from PokemonBase parent class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            This overrides the abstract method __str__() from PokemonBase 
            It puts together a string of pokemon level, pokemon name and pokemon's hp
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            f'string[string]: returns a string containing pokemon level, pokemon name and pokemon's hp
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(n), where n is the string created based on pokemon level, name and hp through formatting
        """
        return f"LV. {self.get_level()} {self.get_poke_name()}: {self.get_hp()} HP"

class Blastoise(PokemonBase):
    """
        CLASS DESCRIPTION:
        Blastoise(Parent PokemonBase) class with class variables pokemon_name, pokemon_type, base_level, base_hp,
        base_attack_damage, base_speed and base_defence declared and defaulted
    """
    pokemon_name = "Blastoise"
    pokemon_type = "Water"
    base_level = 3
    base_hp = 15
    base_attack_damage = 8
    base_speed = 10
    base_defence = 8

    def __init__(self):
        """
            PARAMETERS:
            The instances of Blastoise subclass with inherited members from PokemonBase parent class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            FUNCTION DESCRIPTION:
            __init__ function to initialise instances of class Blastoise with parent class PokemonBase while
            assigning Blastoise class specific attributes to the object with increased stats compared to the
            previous evolution
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [NONE]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all as we are inheriting attributes and instances from parent class and doing
            assignment to instances with some containing mathematical calculation
        """
        PokemonBase.__init__(self, Blastoise.base_hp, Blastoise.pokemon_type)
        self.name = self.pokemon_name
        self.level = self.base_level
        self.max_hp = self.base_hp + (2 * self.level)
        self.hp = self.max_hp
        self.attack_damage = self.base_attack_damage + (self.level // 2)
        self.speed = self.base_speed
        self.defence = self.base_defence + (1 * self.level)

    def level_up(self) -> None:
        """
            PARAMETERS:
            The instances of Blastoise subclass with inherited members from PokemonBase parent class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            This adds on the base method of level_up() derived from the parent class PokemonBase. 
            It has recalculation for stats needed for adjustment as incrementing Blastoise level can influence its stats 
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [NONE]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all as we are inheriting attributes and instances from parent class and doing
            assignment to instances with some containing mathematical calculation
        """
        PokemonBase.level_up(self)
        prev_max_hp = self.max_hp
        prev_hp = self.hp
        diff = prev_max_hp - prev_hp
        self.max_hp = self.base_hp + (2 * self.level)
        self.hp = self.max_hp - diff
        self.attack_damage = self.base_attack_damage + (self.level // 2)
        self.defence = self.base_defence + (1 * self.level)

    def get_speed(self) -> int:
        """
            PARAMETERS:
            The instances of Blastoise subclass with inherited members from PokemonBase parent class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            This overrides the abstract method derived from the parent class PokemonBase. 
            It returns speed of Blastoise and halves it if Blastoise state is under "Paralysis" as
            a status effect inflicted upon by an attacking pokemon
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [int] self.speed
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST CASE:
            O(1), if the first letter of state is different or state has not been declared O(1) and return speed O(1)
            COMPLEXITY FOR WORST CASE:
            O(n), n being the string to be compared with "Paralysis" 
            The return and mathematical calculatin of speed are O(1) 
        """
        if self.state == "Paralysis":
            return self.speed // 2
        else:
            return self.speed

    def get_attack_damage(self) -> int:
        """
            PARAMETERS:
            The instances of Blastoise subclass with inherited members from PokemonBase parent class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            This overrides the abstract method derived from the parent class PokemonBase. 
            It returns attack damage of Blastoise
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [int] self.attack_damage
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all as we are returning attack damage
        """
        return self.attack_damage

    def get_defence(self) -> int:
        """
            PARAMETERS:
            The instances of Blastoise subclass with inherited members from PokemonBase parent class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            This overrides the abstract method derived from the parent class PokemonBase. 
            It returns defence of Blastoise
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [int] self.defence
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all as we are returning defence
        """
        return self.defence

    def defend(self, damage: int) -> None:
        """
            PARAMETERS:
            The instancecs of Blastoise subclass with inherited members from PokemonBase parent class
            damage[integer]: damage dealt by attacking pokemon
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            Overrides abstract method defend() from PokemonBase 
            Returns reamaining hp lost from damage 
            If damage is greater than twice of Blastoise's defence, damage taken 
            is equal to damage dealt, else damage taken is half of damage dealt
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [NONE]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), the precondition checking for damage < 0 is O(1), if and else condition O(1), 
            comparing dammage > defence O(1), and decreasing hp based on damage given O(1)
        """
        #PokemonBase.defend(self, 0)
        if damage > (2 * self.get_defence()):
            self.lose_hp(damage)
        else:
            self.lose_hp(damage // 2)

    def get_poke_name(self) -> str:
        """
            PARAMETERS:
            The instances of Blastoise subclass with inherited members from PokemonBase parent class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            This overrides the abstract method derived from the parent class PokemonBase. 
            It returns its name: Blastoise
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [int] self.name
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all as we are returning name 
        """
        return self.name

    def __str__(self) -> str:
        """
            PARAMETERS:
            The instances of Blastoise subclass with inherited members from PokemonBase parent class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            This overrides the abstract method __str__() from PokemonBase 
            It puts together a string of pokemon level, pokemon name and pokemon's hp
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            f'string[string]: returns a string containing pokemon level, pokemon name and pokemon's hp
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(n), where n is the string created based on pokemon level, name and hp through formatting
        """
        return f"LV. {self.get_level()} {self.get_poke_name()}: {self.get_hp()} HP"

class Squirtle(PokemonBase):
    """
        CLASS DESCRIPTION:
        Squirtle(Parent PokemonBase) class with class variables pokemon_name, pokemon_type, base_level, base_hp,
        base_attack_damage, base_speed and base_defence declared and defaulted
    """
    pokemon_name = "Squirtle"
    pokemon_type = "Water"
    base_level = 1
    base_hp = 9
    base_attack_damage = 4
    base_speed = 7
    base_defence = 6

    def __init__(self):
        """
            PARAMETERS:
            The instances of Squirtle subclass with inherited members from PokemonBase parent class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            FUNCTION DESCRIPTION:
            __init__ function to initialise instances of class Squirtle with parent class PokemonBase while
            assigning Squirtle class specific attributes to the object 
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [NONE]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all as we are inheriting attributes and instances from parent class and doing
            assignment to instances with some containing mathematical calculation
        """
        PokemonBase.__init__(self, Squirtle.base_hp, Squirtle.pokemon_type)
        self.name = self.pokemon_name
        self.level = self.base_level
        self.max_hp = self.base_hp + (2 * self.level)
        self.hp = self.max_hp
        self.attack_damage = self.base_attack_damage + (self.level // 2)
        self.speed = self.base_speed
        self.defence = self.base_defence + self.level
        self.has_evolution = Blastoise()
        self.evolves_at = Blastoise.base_level

    def level_up(self) -> None:
        """
            PARAMETERS:
            The instances of Squirtle subclass with inherited members from PokemonBase parent class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            This adds on the base method of level_up() derived from the parent class PokemonBase. 
            It has recalculation for stats needed for adjustment as incrementing Squirtle level can influence its stats 
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [NONE]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all as we are inheriting attributes and instances from parent class and doing
            assignment to instances with some containing mathematical calculation
        """
        PokemonBase.level_up(self)
        prev_max_hp = self.max_hp
        prev_hp = self.hp
        diff = prev_max_hp - prev_hp
        self.max_hp = self.base_hp + (2 * self.level)
        self.hp = self.max_hp - diff
        self.attack_damage = self.base_attack_damage + (self.level // 2)
        self.defence = self.base_defence + self.level

    def get_speed(self) -> int:
        """
            PARAMETERS:
            The instances of Squirtle subclass with inherited members from PokemonBase parent class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            This overrides the abstract method derived from the parent class PokemonBase. 
            It returns speed of Squirtle and halves it if Squirtle state is under "Paralysis" as
            a status effect inflicted upon by an attacking pokemon
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [int] self.speed
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST CASE:
            O(1), if the first letter of state is different or state has not been declared O(1) and return speed O(1)
            COMPLEXITY FOR WORST CASE:
            O(n), n being the string to be compared with "Paralysis" 
            The return and mathematical calculatin of speed are O(1) 
        """
        if self.state == "Paralysis":
            return self.speed // 2
        else:
            return self.speed

    def get_attack_damage(self) -> int:
        """
            PARAMETERS:
            The instances of Squirtle subclass with inherited members from PokemonBase parent class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            This overrides the abstract method derived from the parent class PokemonBase. 
            It returns attack damage of Squirtle
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [int] self.attack_damage
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all as we are returning attack damage
        """
        return self.attack_damage

    def get_defence(self) -> int:
        """
            PARAMETERS:
            The instances of Squirtle subclass with inherited members from PokemonBase parent class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            This overrides the abstract method derived from the parent class PokemonBase. 
            It returns defence of Squirtle
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [int] self.defence
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all as we are returning defence
        """
        return self.defence

    def defend(self, damage: int) -> None:
        """
            PARAMETERS:
            The instancecs of Squirtle subclass with inherited members from PokemonBase parent class
            damage[integer]: damage dealt by attacking pokemon
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            Overrides abstract method defend() from PokemonBase 
            Returns reamaining hp lost from damage 
            If damage is greater than twice of Squirtle's defence, damage taken 
            is equal to damage dealt, else damage taken is half of damage dealt
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [NONE]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), the precondition checking for damage < 0 is O(1), if and else condition O(1), 
            comparing dammage > defence O(1), and decreasing hp based on damage given O(1)
        """
        #PokemonBase.defend(self, 0)
        if damage > (2 * self.get_defence()):
            self.lose_hp(damage)
        else:
            self.lose_hp(damage // 2)

    def get_poke_name(self) -> str:
        """
            PARAMETERS:
            The instances of Squirtle subclass with inherited members from PokemonBase parent class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            This overrides the abstract method derived from the parent class PokemonBase. 
            It returns its name: Squirtle
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [int] self.name
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all as we are returning name 
        """
        return self.name

    def __str__(self) -> str:
        """
            PARAMETERS:
            The instances of Squirtle subclass with inherited members from PokemonBase parent class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            This overrides the abstract method __str__() from PokemonBase 
            It puts together a string of pokemon level, pokemon name and pokemon's hp
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            f'string[string]: returns a string containing pokemon level, pokemon name and pokemon's hp
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(n), where n is the string created based on pokemon level, name and hp through formatting
        """
        return f"LV. {self.get_level()} {self.get_poke_name()}: {self.get_hp()} HP"

class Gengar(PokemonBase):
    """
        CLASS DESCRIPTION:
        Gengar(Parent PokemonBase) class with class variables pokemon_name, pokemon_type, base_level, base_hp,
        base_attack_damage, base_speed and base_defence declared and defaulted
    """
    pokemon_name = "Gengar"
    pokemon_type = "Ghost"
    base_level = 3
    base_hp = 12
    base_attack_damage = 18
    base_speed = 12
    base_defence = 3

    def __init__(self):
        """
            PARAMETERS:
            The instances of Gengar subclass with inherited members from PokemonBase parent class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            FUNCTION DESCRIPTION:
            __init__ function to initialise instances of class Gengar with parent class PokemonBase while
            assigning Gengar class specific attributes to the object with increased stats compared to the
            previous evolution
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [NONE]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all as we are inheriting attributes and instances from parent class and doing
            assignment to instances with some containing mathematical calculation
        """
        PokemonBase.__init__(self, Gengar.base_hp, Gengar.pokemon_type)
        self.name = self.pokemon_name
        self.level = self.base_level
        self.max_hp = self.base_hp + (self.level // 2)
        self.hp = self.max_hp
        self.attack_damage = self.base_attack_damage
        self.speed = self.base_speed
        self.defence = self.base_defence

    def level_up(self) -> None:
        """
            PARAMETERS:
            The instances of Gengar subclass with inherited members from PokemonBase parent class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            This adds on the base method of level_up() derived from the parent class PokemonBase. 
            It has recalculation for stats needed for adjustment as incrementing Gengar level can influence its stats 
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [NONE]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all as we are inheriting attributes and instances from parent class and doing
            assignment to instances with some containing mathematical calculation
        """
        PokemonBase.level_up(self)
        prev_max_hp = self.max_hp
        prev_hp = self.hp
        diff = prev_max_hp - prev_hp
        self.max_hp = self.base_hp + (self.level // 2)
        self.hp = self.max_hp - diff

    def get_speed(self) -> int:
        """
            PARAMETERS:
            The instances of Gengar subclass with inherited members from PokemonBase parent class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            This overrides the abstract method derived from the parent class PokemonBase. 
            It returns speed of Gengar and halves it if Gengar state is under "Paralysis" as
            a status effect inflicted upon by an attacking pokemon
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [int] self.speed
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST CASE:
            O(1), if the first letter of state is different or state has not been declared O(1) and return speed O(1)
            COMPLEXITY FOR WORST CASE:
            O(n), n being the string to be compared with "Paralysis" 
            The return and mathematical calculatin of speed are O(1) 
        """
        if self.state == "Paralysis":
            return self.speed // 2
        else:
            return self.speed

    def get_attack_damage(self) -> int:
        """
            PARAMETERS:
            The instances of Gengar subclass with inherited members from PokemonBase parent class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            This overrides the abstract method derived from the parent class PokemonBase. 
            It returns attack damage of Gengar
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [int] self.attack_damage
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all as we are returning attack damage
        """
        return self.attack_damage

    def get_defence(self) -> int:
        """
            PARAMETERS:
            The instances of Gengar subclass with inherited members from PokemonBase parent class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            This overrides the abstract method derived from the parent class PokemonBase. 
            It returns defence of Gengar
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [int] self.defence
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all as we are returning defence
        """
        return self.defence

    def defend(self, damage: int) -> None:
        """
            PARAMETERS:
            The instancecs of Gengar subclass with inherited members from PokemonBase parent class
            damage[integer]: damage dealt by attacking pokemon
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            Overrides abstract method defend() from PokemonBase 
            Returns reamaining hp lost from damage 
            Damage taken is equal to damage dealt
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [NONE]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), the precondition checking for damage < 0 is O(1), if and else condition O(1), 
            comparing dammage > defence O(1), and decreasing hp based on damage given O(1)
        """
        #PokemonBase.defend(self, 0)
        self.lose_hp(damage)

    def get_poke_name(self) -> str:
        """
            PARAMETERS:
            The instances of Gengar subclass with inherited members from PokemonBase parent class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            This overrides the abstract method derived from the parent class PokemonBase. 
            It returns its name: Gengar
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [int] self.name
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all as we are returning name 
        """
        return self.name

    def __str__(self) -> str:
        """
            PARAMETERS:
            The instances of Gengar subclass with inherited members from PokemonBase parent class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            This overrides the abstract method __str__() from PokemonBase 
            It puts together a string of pokemon level, pokemon name and pokemon's hp
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            f'string[string]: returns a string containing pokemon level, pokemon name and pokemon's hp
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(n), where n is the string created based on pokemon level, name and hp through formatting
        """
        return f"LV. {self.get_level()} {self.get_poke_name()}: {self.get_hp()} HP"

class Haunter(PokemonBase):
    """
        CLASS DESCRIPTION:
        Haunter(Parent PokemonBase) class with class variables pokemon_name, pokemon_type, base_level, base_hp,
        base_attack_damage, base_speed and base_defence declared and defaulted
    """
    pokemon_name = "Haunter"
    pokemon_type = "Ghost"
    base_level = 1
    base_hp = 9
    base_attack_damage = 8
    base_speed = 6
    base_defence = 6

    def __init__(self):
        """
            PARAMETERS:
            The instances of Haunter subclass with inherited members from PokemonBase parent class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            FUNCTION DESCRIPTION:
            __init__ function to initialise instances of class Haunter with parent class PokemonBase while
            assigning Haunter class specific attributes to the object with increased stats compared to the
            previous evolution
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [NONE]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all as we are inheriting attributes and instances from parent class and doing
            assignment to instances with some containing mathematical calculation
        """
        PokemonBase.__init__(self, Haunter.base_hp, Haunter.pokemon_type)
        self.name = self.pokemon_name
        self.level = self.base_level
        self.max_hp = self.base_hp + (self.level // 2)
        self.hp = self.max_hp
        self.attack_damage = self.base_attack_damage
        self.speed = self.base_speed
        self.defence = self.base_defence
        self.has_evolution = Gengar()
        self.evolves_at = 3

    def level_up(self) -> None:
        """
            PARAMETERS:
            The instances of Haunter subclass with inherited members from PokemonBase parent class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            This adds on the base method of level_up() derived from the parent class PokemonBase. 
            It has recalculation for stats needed for adjustment as incrementing Haunter level can influence its stats 
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [NONE]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all as we are inheriting attributes and instances from parent class and doing
            assignment to instances with some containing mathematical calculation
        """
        PokemonBase.level_up(self)
        prev_max_hp = self.max_hp
        prev_hp = self.hp
        diff = prev_max_hp - prev_hp
        self.max_hp = self.base_hp + (self.level // 2)
        self.hp = self.max_hp - diff

    def get_speed(self) -> int:
        """
            PARAMETERS:
            The instances of Haunter subclass with inherited members from PokemonBase parent class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            This overrides the abstract method derived from the parent class PokemonBase. 
            It returns speed of Haunter and halves it if Haunter state is under "Paralysis" as
            a status effect inflicted upon by an attacking pokemon
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [int] self.speed
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST CASE:
            O(1), if the first letter of state is different or state has not been declared O(1) and return speed O(1)
            COMPLEXITY FOR WORST CASE:
            O(n), n being the string to be compared with "Paralysis" 
            The return and mathematical calculatin of speed are O(1) 
        """
        if self.state == "Paralysis":
            return self.speed // 2
        else:
            return self.speed

    def get_attack_damage(self) -> int:
        """
            PARAMETERS:
            The instances of Haunter subclass with inherited members from PokemonBase parent class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            This overrides the abstract method derived from the parent class PokemonBase. 
            It returns attack damage of Haunter
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [int] self.attack_damage
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all as we are returning attack damage
        """
        return self.attack_damage

    def get_defence(self) -> int:
        """
            PARAMETERS:
            The instances of Haunter subclass with inherited members from PokemonBase parent class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            This overrides the abstract method derived from the parent class PokemonBase. 
            It returns defence of Haunter
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [int] self.defence
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all as we are returning defence
        """
        return self.defence

    def defend(self, damage: int) -> None:
        """
            PARAMETERS:
            The instancecs of Haunter subclass with inherited members from PokemonBase parent class
            damage[integer]: damage dealt by attacking pokemon
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            Overrides abstract method defend() from PokemonBase 
            Returns reamaining hp lost from damage 
            Damage taken is same as damage dealt
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [NONE]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), the precondition checking for damage < 0 is O(1), if and else condition O(1), 
            comparing dammage > defence O(1), and decreasing hp based on damage given O(1)
        """
        #PokemonBase.defend(self, 0)
        self.lose_hp(damage)

    def get_poke_name(self) -> str:
        """
            PARAMETERS:
            The instances of Haunter subclass with inherited members from PokemonBase parent class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            This overrides the abstract method derived from the parent class PokemonBase. 
            It returns its name: Haunter
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [int] self.name
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all as we are returning name 
        """
        return self.name

    def __str__(self) -> str:
        """
            PARAMETERS:
            The instances of Haunter subclass with inherited members from PokemonBase parent class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            This overrides the abstract method __str__() from PokemonBase 
            It puts together a string of pokemon level, pokemon name and pokemon's hp
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            f'string[string]: returns a string containing pokemon level, pokemon name and pokemon's hp
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(n), where n is the string created based on pokemon level, name and hp through formatting
        """
        return f"LV. {self.get_level()} {self.get_poke_name()}: {self.get_hp()} HP"

class Gastly(PokemonBase):
    """
        CLASS DESCRIPTION:
        Gastly(Parent PokemonBase) class with class variables pokemon_name, pokemon_type, base_level, base_hp,
        base_attack_damage, base_speed and base_defence declared and defaulted
    """
    pokemon_name = "Gastly"
    pokemon_type = "Ghost"
    base_level = 1
    base_hp = 6
    base_attack_damage = 4
    base_speed = 2
    base_defence = 8

    def __init__(self):
        """
            PARAMETERS:
            The instances of Gastly subclass with inherited members from PokemonBase parent class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            FUNCTION DESCRIPTION:
            __init__ function to initialise instances of class Gastly with parent class PokemonBase while
            assigning Gastly class specific attributes to the object 
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [NONE]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all as we are inheriting attributes and instances from parent class and doing
            assignment to instances with some containing mathematical calculation
        """
        PokemonBase.__init__(self, Gastly.base_hp, Gastly.pokemon_type)
        self.name = self.pokemon_name
        self.level = self.base_level
        self.max_hp = self.base_hp + (self.level // 2)
        self.hp = self.max_hp
        self.attack_damage = self.base_attack_damage
        self.speed = self.base_speed
        self.defence = self.base_defence
        self.has_evolution = Haunter()
        self.evolves_at = 1

    def level_up(self) -> None:
        """
            PARAMETERS:
            The instances of Gastly subclass with inherited members from PokemonBase parent class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            This adds on the base method of level_up() derived from the parent class PokemonBase. 
            It has recalculation for stats needed for adjustment as incrementing Gastly level can influence its stats 
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [NONE]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all as we are inheriting attributes and instances from parent class and doing
            assignment to instances with some containing mathematical calculation
        """
        PokemonBase.level_up(self)
        prev_max_hp = self.max_hp
        prev_hp = self.hp
        diff = prev_max_hp - prev_hp
        self.max_hp = self.base_hp + (self.level // 2)
        self.hp = self.max_hp - diff

    def get_speed(self) -> int:
        """
            PARAMETERS:
            The instances of Gastly subclass with inherited members from PokemonBase parent class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            This overrides the abstract method derived from the parent class PokemonBase. 
            It returns speed of Gastly and halves it if Gastly state is under "Paralysis" as
            a status effect inflicted upon by an attacking pokemon
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [int] self.speed
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST CASE:
            O(1), if the first letter of state is different or state has not been declared O(1) and return speed O(1)
            COMPLEXITY FOR WORST CASE:
            O(n), n being the string to be compared with "Paralysis" 
            The return and mathematical calculatin of speed are O(1) 
        """
        if self.state == "Paralysis":
            return self.speed // 2
        else:
            return self.speed

    def get_attack_damage(self) -> int:
        """
            PARAMETERS:
            The instances of Gastly subclass with inherited members from PokemonBase parent class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            This overrides the abstract method derived from the parent class PokemonBase. 
            It returns attack damage of Gastly
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [int] self.attack_damage
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all as we are returning attack damage
        """
        return self.attack_damage

    def get_defence(self) -> int:
        """
            PARAMETERS:
            The instances of Gastly subclass with inherited members from PokemonBase parent class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            This overrides the abstract method derived from the parent class PokemonBase. 
            It returns defence of Gastly
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [int] self.defence
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all as we are returning defence
        """
        return self.defence

    def defend(self, damage: int) -> None:
        """
            PARAMETERS:
            The instancecs of Gastly subclass with inherited members from PokemonBase parent class
            damage[integer]: damage dealt by attacking pokemon
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            Overrides abstract method defend() from PokemonBase 
            Returns reamaining hp lost from damage 
            Damage taken is same as damage dealt
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [NONE]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), the precondition checking for damage < 0 is O(1), if and else condition O(1), 
            comparing dammage > defence O(1), and decreasing hp based on damage given O(1)
        """
        #PokemonBase.defend(self, 0)
        self.lose_hp(damage)

    def get_poke_name(self) -> str:
        """
            PARAMETERS:
            The instances of Gastly subclass with inherited members from PokemonBase parent class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            This overrides the abstract method derived from the parent class PokemonBase. 
            It returns its name: Gastly
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [int] self.name
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all as we are returning name 
        """
        return self.name

    def __str__(self) -> str:
        """
            PARAMETERS:
            The instances of Gastly subclass with inherited members from PokemonBase parent class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            This overrides the abstract method __str__() from PokemonBase 
            It puts together a string of pokemon level, pokemon name and pokemon's hp
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            f'string[string]: returns a string containing pokemon level, pokemon name and pokemon's hp
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(n), where n is the string created based on pokemon level, name and hp through formatting
        """
        return f"LV. {self.get_level()} {self.get_poke_name()}: {self.get_hp()} HP"
    

class Eevee(PokemonBase):
    """
        CLASS DESCRIPTION:
        Eevee(Parent PokemonBase) class with class variables pokemon_name, pokemon_type, base_level, base_hp,
        base_attack_damage, base_speed and base_defence declared and defaulted
    """
    pokemon_name = "Eevee"
    pokemon_type = "Normal"
    base_level = 1
    base_hp = 10
    base_attack_damage = 6
    base_speed = 7
    base_defence = 4

    def __init__(self):
        """
            PARAMETERS:
            The instances of Eevee subclass with inherited members from PokemonBase parent class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            FUNCTION DESCRIPTION:
            __init__ function to initialise instances of class Eevee with parent class PokemonBase while
            assigning Eevee class specific attributes to the object with increased stats compared to the
            previous evolution
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [NONE]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all as we are inheriting attributes and instances from parent class and doing
            assignment to instances with some containing mathematical calculation
        """
        PokemonBase.__init__(self, Eevee.base_hp, Eevee.pokemon_type)
        self.name = self.pokemon_name
        self.level = self.base_level
        self.max_hp = self.base_hp
        self.hp = self.max_hp
        self.attack_damage = self.base_attack_damage + self.level
        self.speed = self.base_speed + self.level
        self.defence = self.base_defence + self.level
    
    def level_up(self) -> None:
        """
            PARAMETERS:
            The instances of Eevee subclass with inherited members from PokemonBase parent class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            This adds on the base method of level_up() derived from the parent class PokemonBase. 
            It has recalculation for stats needed for adjustment as incrementing Eevee level can influence its stats 
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [NONE]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all as we are inheriting attributes and instances from parent class and doing
            assignment to instances with some containing mathematical calculation
        """
        PokemonBase.level_up(self)
        # health portion of the code does not need to be implemented here, as the hp is 10 regardless of level
        self.attack_damage = self.base_attack_damage + self.level
        self.speed = self.base_speed + self.level
        self.defence = self.base_defence + self.level

    def get_speed(self) -> int:
        """
            PARAMETERS:
            The instances of Eevee subclass with inherited members from PokemonBase parent class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            This overrides the abstract method derived from the parent class PokemonBase. 
            It returns speed of Eevee and halves it if Eevee state is under "Paralysis" as
            a status effect inflicted upon by an attacking pokemon
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [int] self.speed
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST CASE:
            O(1), if the first letter of state is different or state has not been declared O(1) and return speed O(1)
            COMPLEXITY FOR WORST CASE:
            O(n), n being the string to be compared with "Paralysis" 
            The return and mathematical calculatin of speed are O(1) 
        """
        if self.state == "Paralysis":
            return self.speed // 2
        else:
            return self.speed

    def get_attack_damage(self) -> int:
        """
            PARAMETERS:
            The instances of Eevee subclass with inherited members from PokemonBase parent class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            This overrides the abstract method derived from the parent class PokemonBase. 
            It returns attack damage of Eevee
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [int] self.attack_damage
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all as we are returning attack damage
        """
        return self.attack_damage

    def get_defence(self) -> int:
        """
            PARAMETERS:
            The instances of Eevee subclass with inherited members from PokemonBase parent class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            This overrides the abstract method derived from the parent class PokemonBase. 
            It returns defence of Eevee
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [int] self.defence
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all as we are returning defence
        """
        return self.defence

    def defend(self, damage: int) -> None:
        """
            PARAMETERS:
            The instancecs of Eevee subclass with inherited members from PokemonBase parent class
            damage[integer]: damage dealt by attacking pokemon
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            Overrides abstract method defend() from PokemonBase 
            Returns reamaining hp lost from damage 
            If damage dealt is more than or equals to Eevee's defence,
            damage taken is equal to damage dealt, else no damage is taken
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [NONE]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), the precondition checking for damage < 0 is O(1), if and else condition O(1), 
            comparing dammage > defence O(1), and decreasing hp based on damage given O(1)
        """
        #PokemonBase.defend(self, 0)
        if damage >= self.get_defence():
            self.lose_hp(damage)

    def get_poke_name(self) -> str:
        """
            PARAMETERS:
            The instances of Eevee subclass with inherited members from PokemonBase parent class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            This overrides the abstract method derived from the parent class PokemonBase. 
            It returns its name: Eevee
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [int] self.name
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all as we are returning name 
        """
        return self.name

    def __str__(self) -> str:
        """
            PARAMETERS:
            The instances of Eevee subclass with inherited members from PokemonBase parent class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            This overrides the abstract method __str__() from PokemonBase 
            It puts together a string of pokemon level, pokemon name and pokemon's hp
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            f'string[string]: returns a string containing pokemon level, pokemon name and pokemon's hp
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(n), where n is the string created based on pokemon level, name and hp through formatting
        """
        return f"LV. {self.get_level()} {self.get_poke_name()}: {self.get_hp()} HP"


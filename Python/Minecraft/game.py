from __future__ import annotations

from player import Player
from trader import Trader, RandomTrader, RangeTrader, HardTrader
from material import Material
from cave import Cave
from food import Food
from random_gen import RandomGen
from hash_table import LinearProbeTable
from heap import MaxHeap
from constants import EPSILON
import unittest

class Game:
    """
        CLASS DESCRIPTION:
        Game class with class variables TRADERS_CLASS, MIN_MATERIALS, MAX_MATERIALS, MIN_CAVES, MAX_CAVES,
        MIN_TRADERS, MAX_TRADERS, MIN_FOOD, MAX_FOOD and this class stores the game attributes and variables
        which are to be implemented in methods
    """

    TRADERS_CLASS = ["RandomTrader","RangeTrader","HardTrader"]

    # used in generate random materials
    MIN_MATERIALS = 5
    MAX_MATERIALS = 10

    # used in generate random caves
    MIN_CAVES = 5
    MAX_CAVES = 10

    # used in generate random traders
    MIN_TRADERS = 4
    MAX_TRADERS = 8

    # used in generate random foods
    MIN_FOOD = 2
    MAX_FOOD = 5

    def __init__(self) -> None:
        """
            PARAMETERS:
            No paramters given. All variables are defaulted
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            FUNCTION DESCRIPTION:
            -   __init__ magic method to instantiate
                player, materials, caves, traders as default
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [None]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all, only assigns values to variables and check for precondtions
        """
        self.player = None
        self.materials = None
        self.caves = None
        self.traders = None

    def initialise_game(self) -> None:
        """
            PARAMETERS:
            The instances of Game class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            FUNCTION DESCRIPTION:
            -   Initialise all game objects: Materials, Caves, Traders.
                Generate random objects for each game object type
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [None]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all, only assigns values to variables and check for precondtions
        """
        N_MATERIALS = RandomGen.randint(self.MIN_MATERIALS, self.MAX_MATERIALS)
        print(N_MATERIALS)
        self.generate_random_materials(N_MATERIALS)
        print("Materials:\n\t", end="")
        print("\n\t".join(map(str, self.get_materials())))
        N_CAVES = RandomGen.randint(self.MIN_CAVES, self.MAX_CAVES)
        self.generate_random_caves(N_CAVES)
        print("Caves:\n\t", end="")
        print("\n\t".join(map(str, self.get_caves())))
        N_TRADERS = RandomGen.randint(self.MIN_TRADERS, self.MAX_TRADERS)
        self.generate_random_traders(N_TRADERS)
        print("Traders:\n\t", end="")
        print("\n\t".join(map(str, self.get_traders())))

    def initialise_with_data(self, materials: list[Material], caves: list[Cave], traders: list[Trader]):
        """
            PARAMETERS:
            materials[list] : a list of materials
            caves[list]     : a list of caves
            traders[list]   : a list of traders
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            FUNCTION DESCRIPTION:
            -   Set game objects (Materials, Caves and Traders) using parameters values
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [None]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all, only setting values to variables
        """
        self.set_materials(materials)
        self.set_caves(caves)
        self.set_traders(traders)

    def set_materials(self, mats: list[Material]) -> None:
        """
            PARAMETERS:
            mats[list] : a list of materials
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            FUNCTION DESCRIPTION:
            -   Set a list of Material
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [None]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all, only assigning list to self.materials
        """
        self.materials = mats

    def set_caves(self, caves: list[Cave]) -> None:
        """
            PARAMETERS:
            caves[list] : a list of caves
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            FUNCTION DESCRIPTION:
            -   Set a list of Cave
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [None]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all, only assigning list to self.caves
        """
        self.caves = caves

    def set_traders(self, traders: list[Trader]) -> None:
        """
            PARAMETERS:
            traders[list] : a list of traders
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            FUNCTION DESCRIPTION:
            -   Set a list of Trader
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [None]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all, only assigning list to self.traders
        """
        self.traders = traders

    def get_materials(self) -> list[Material]:
        """
            PARAMETERS:
            The instances of Game class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            FUNCTION DESCRIPTION:
            -   return a list of materials
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            self.materials[list] : a list of materials
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all, only returning values
        """
        return self.materials

    def get_caves(self) -> list[Cave]:
        """
            PARAMETERS:
            The instances of Game class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            FUNCTION DESCRIPTION:
            -   return a list of caves
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            self.caves[list] : a list of caves
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all, only returning values
        """
        return self.caves

    def get_traders(self) -> list[Trader]:
        """
            PARAMETERS:
            The instances of Game class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            FUNCTION DESCRIPTION:
            -   return a list of traders
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            self.traders[list] : a list of traders
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all, only returning values
        """
        return self.traders

    def generate_random_materials(self, amount : int):
        """
            PARAMETERS:
            The instances of Game class
            amount[int] : number of materials wanted
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            FUNCTION DESCRIPTION:
            -   Generates <amount> random materials using Material.random_material
                Generated materials must all have different names and different mining_rates.
                (You may have to call Material.random_material more than <amount> times.)
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [None]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST CASE:
            O(<amount>) : iterate <amount> times to generate materials. Assigning and comparisons are O(1)
            COMPLEXITY FOR WORST CASE:
            O(<amount> + M) : iterate <amount> times and M times if generated same material name and mining rate
        """
        # Have empty list if self.materials is set as default
        if self.materials == None:
            self.materials = []

        i = 0
        mat_name_list = [] # a list to detect existing name
        mat_mining_rate_list = [] # a list to detect existing mining rate
        while i < amount:
            rand_mat = Material.random_material() # random material with name and mining rate

            # if we have 1 or more element in self.materials
            if len(self.materials) != 0:

                # if random material generated is unique ( diff name and mining rate)
                if (rand_mat.name not in mat_name_list) and (rand_mat.mining_rate not in mat_mining_rate_list):
                    # add name and material to check whether next rand mat is unique
                    mat_name_list.append(rand_mat.name)
                    mat_mining_rate_list.append(rand_mat.mining_rate)
                    self.materials.append(rand_mat)
                    i += 1
            else:
                # add name and material to check whether next rand mat is unique
                self.materials.append(rand_mat)
                mat_name_list.append(rand_mat.name)
                mat_mining_rate_list.append(rand_mat.mining_rate)
                i += 1


    def generate_random_caves(self, amount):
        """
            PARAMETERS:
            The instances of Game class
            amount[int] : number of caves wanted
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            FUNCTION DESCRIPTION:
            -   Generates <amount> random caves using Cave.random_cave
                Generated caves must all have different names
                (You may have to call Cave.random_cave more than <amount> times.)
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [None]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST CASE:
            O(<amount>) : iterate <amount> times to generate materials. Assigning and comparisons are O(1)
            COMPLEXITY FOR WORST CASE:
            O((<amount> + C) + (<amount> + M)) :
            generate random materials if None and iterate <amount> + C if generated same cave name
        """

        if self.materials == None:
            self.materials = []
        if len(self.materials) == 0: # self.materials is empty list
            self.generate_random_materials(amount)
        if self.caves == None:
            self.caves = []

        i = 0
        cave_name_list = [] # a list to detect existing cave name
        while i < amount:
            rand_cave = Cave.random_cave(self.materials) # random material with name and mining rate
            if len(self.caves) != 0:
                # if random cave generated is unique ( diff name )
                if rand_cave.name not in cave_name_list:
                    # add name to check whether next rand cave is unique
                    cave_name_list.append(rand_cave.name)
                    self.caves.append(rand_cave) # a cave with unique name
                    i += 1
            else:
                # add name to check whether next rand cave is unique
                self.caves.append(rand_cave)
                cave_name_list.append(rand_cave.name)
                i += 1

    def generate_random_traders(self, amount):
        """
            PARAMETERS:
            The instances of Game class
            amount[int] : number of traders wanted
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            FUNCTION DESCRIPTION:
            -   Generates <amount> random traders by selecting a random trader class
                and then calling <TraderClass>.random_trader()
                and then calling set_all_materials with some subset of the already generated materials.
                Generated traders must all have different names
                (You may have to call <TraderClass>.random_trader() more than <amount> times.)
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [None]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST CASE:
            O(<amount> * M) :
            Iterate <amount> times to generate traders with each trader set all materials.
            Assigning and comparisons are O(1)
            COMPLEXITY FOR WORST CASE:
            O((<amount> * M) + T)) :
            Iterate <amount> times to generate traders with each trader set all materials.
            T will be the amount of time missed to set trader due to repeated name
            Assigning and comparisons are O(1)
        """
        if self.traders == None:
            self.traders = []
        i = 0
        trader_name_list = []
        while i < amount:
            rand_trader_class = RandomGen.random_choice(Game.TRADERS_CLASS) # it is in str
            rand_trader = rand_trader_class + ".random_trader()"
            rand_trader = eval(rand_trader) # random trader by evaluating rand_trader str command

            # if self.traders has 1 or more elements in it
            if len(self.traders) != 0:
                # if random trader generated is unique ( diff name )
                if rand_trader.name not in trader_name_list:
                    rand_trader.set_all_materials(self.materials)

                    # add name to check whether next rand trader is unique
                    trader_name_list.append(rand_trader.name)
                    self.traders.append(rand_trader)
                    i += 1
            else:
                rand_trader.set_all_materials(self.materials)

                # add name to check whether next rand trader is unique
                trader_name_list.append(rand_trader.name)
                self.traders.append(rand_trader)
                i += 1

    def finish_day(self):
        """
            PARAMETERS:
            The instances of Game class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            FUNCTION DESCRIPTION:
            -   Update cave quantity after removing and updating
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [None]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(C) :
            Iterate C times (C being number of caves) to update cave quantity
            Assigning , removing, adding and comparisons are O(1)

        """
        for cave in self.get_caves():
            if cave.quantity > 0 and RandomGen.random_chance(0.2):
                cave.remove_quantity(RandomGen.random_float() * cave.quantity)
            else:
                cave.add_quantity(round(RandomGen.random_float() * 10, 2))
            cave.quantity = round(cave.quantity, 2)

class SoloGame(Game):
    """
        CLASS DESCRIPTION:
        Solo Game (Parent Game) class stores the game attributes and variables
        inherited which are to be implemented in methods
    """

    def initialise_game(self) -> None:
        """
            PARAMETERS:
            The instances of Solo subclass with inherited members from Game parent class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            FUNCTION DESCRIPTION:
            -   Initialise player objects (Material, Cave, Traders) after generating a random player
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [None]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all, only assigns values to variables and check for precondtions
        """
        super().initialise_game()
        self.player = Player.random_player()
        self.player.set_materials(self.get_materials())
        self.player.set_caves(self.get_caves())
        self.player.set_traders(self.get_traders())

    def initialise_with_data(self, materials: list[Material], caves: list[Cave], traders: list[Trader], player_names: list[int], emerald_info: list[float]):
        """
            PARAMETERS:
            The instances of Solo subclass with inherited members from Game parent class
            materials[list]: a list of materials
            caves[list]: a list of caves
            traders[list]: a list of traders
            player_names[list]: a list of player names
            emerald_info[list]: a list of emerald amount as float
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            FUNCTION DESCRIPTION:
            -   Initialise player objects (Material, Cave, Traders) with data from parameters
                after generating player with stats
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [None]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all, only assigns values to variables and check for precondtions
        """
        super().initialise_with_data(materials, caves, traders)
        self.player = Player(player_names[0], emeralds=emerald_info[0])
        self.player.set_materials(self.get_materials())
        self.player.set_caves(self.get_caves())
        self.player.set_traders(self.get_traders())

    def simulate_day(self):
        """
            PARAMETERS:
            The instances of Solo subclass with inherited members from Game parent class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            FUNCTION DESCRIPTION:
            -   Simulate a game through
                1. Setting relevant objects for a game and player
                2. Perform mining
                3. Check values after exploration
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [None]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST CASE 
            O(1)/ O(T + F + (F+C+C)) : run through simulation and fail at verifying
            COMPLEXITY FOR WORST CASE:
            O(n^2)/ O(T + F + (F+C+C) + (C + C + C+ F + F + C^2)), run through simulation and pass at verifying
        """
        # 1. Traders make deals
        for i in range(len(self.traders)): # go through a list of traders
            self.traders[i].generate_deal()
        self.player.set_traders(self.get_traders())
        self.traders = self.player.traders # set traders from player to game
        self.caves = self.player.caves # set caves from player to game
        print("Traders Deals:\n\t", end="")
        print("\n\t".join(map(str, self.get_traders())))
        # 2. Food is offered
        food_num = RandomGen.randint(self.MIN_FOOD, self.MAX_FOOD)
        foods = []
        for _ in range(food_num):
            foods.append(Food.random_food())
        print("\nFoods:\n\t", end="")
        print("\n\t".join(map(str, foods)))
        self.player.set_foods(foods)
        # 3. Select one food item to purchase
        food, balance, caves = self.player.select_food_and_caves()
        print(food, balance, caves)
        # 4. Quantites for caves is updated, some more stuff is added.
        self.verify_output_and_update_quantities(food, balance, caves)

    def verify_output_and_update_quantities(self, food: Food | None, balance: float, caves: list[tuple[Cave, float]]) -> None:
        """
            PARAMETERS:
            The instances of Solo subclass with inherited members from Game parent class
            food[Food]: the food chosen from select_food_and_caves()
            balacne[float]: emerald balance
            caves[list] : a list of tuple containing Cave and its quantity mined
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            FUNCTION DESCRIPTION:
            -   Check whether quantity and stats provided from paramaters are right
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [None]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST CASE:
            O(1) : comparison of number of caves plundered and values do not equate
            COMPLEXITY FOR WORST CASE:
            O(C + C + C+ F + F + C^2), multiple iteration of caves and foods list to check values
        """
        # check all amounts align

        # check quantities given are alright
        # check num of caves explored
        if self.player.caves_explored != len(caves):
            raise AssertionError("Plundered caves do not match")

        # check materials mined in each caves do not exceed amount
        for i in range(len(caves)):
            the_cave = caves[i][0].quantity
            print(the_cave)
            amounttocheck = caves[i][1] - caves[i][0].quantity
            print(amounttocheck)
            if (caves[i][1] - caves[i][0].quantity) > EPSILON:
                raise Error("Material mined more than what is available")

        # check materials mined in each caves
        for i in range(len(caves)):
            if caves[i][0].quantity < 0:
                raise Error("Cave is empty")

        # check food can be purchased in the first place
        if (food not in self.player.foods) and (self.player.original_balance > food.food_price):
            raise Error("Food could not be purchased")

        # check balance given is correct
        check_balance = 0
        for i in range(len(caves)):
            cave_mat = caves[i][0].cave_material.name
            mined_mat = caves[i][1]
            trader_deal_amount = self.player.traders_hash.__getitem__(cave_mat)
            check_balance += mined_mat * trader_deal_amount

        check_balance += self.player.balance_after_food # add back balance before mining

        if abs(balance - check_balance) > EPSILON:
            raise Error("wrong balance")

        # check food hunger bar amount aligns
        food_list = self.player.foods
        for the_food in food_list:
            if food.food_name == the_food.food_name:
                print(food.hunger_bars)
                print(the_food.hunger_bars)
                if food.hunger_bars != the_food.hunger_bars:
                    raise Error("food hunger bar is skewed")

        # check food exists
        food_name_list = []
        for i in range(len(food_list)):
            food_name_list.append(food_list[i].food_name)
        if food.food_name not in food_name_list:
            raise Error("food does not exist")

        # check balance is at or below zero
        if balance < EPSILON:
            raise Error("zero balance")

        # update the damn quantities in caves
        cave_name_list = []
        for i in range(len(caves)):
            cave_name_list.append(caves[i][0].name)

        print(cave_name_list)
        new_cave_list = []
        for i in range(len(caves)):
            the_cave = caves[i][0]
            available_mat = caves[i][1]
            if the_cave.name in cave_name_list:
                updated_quantity = the_cave.quantity - available_mat
                for cave in self.caves:
                    if the_cave.name == cave.name:
                        cave.quantity = updated_quantity
        print("caves should be updated")
        #raise NotImplementedError()

class MultiplayerGame(Game):
    """
        CLASS DESCRIPTION:
        MultiplayerGame Game (Parent Game) class contains MIN_PLAYERS, MAX_PLAYERS and stores the game attributes and variables
        inherited which are to be implemented in methods
    """

    MIN_PLAYERS = 2
    MAX_PLAYERS = 5

    def __init__(self) -> None:
        super().__init__()
        self.players = []

    def initialise_game(self) -> None:
        super().initialise_game()
        N_PLAYERS = RandomGen.randint(self.MIN_PLAYERS, self.MAX_PLAYERS)
        self.generate_random_players(N_PLAYERS)
        for player in self.players:
            player.set_materials(self.get_materials())
            player.set_caves(self.get_caves())
            player.set_traders(self.get_traders())
        print("Players:\n\t", end="")
        print("\n\t".join(map(str, self.players)))

    def generate_random_players(self, amount) -> None:
        """Generate <amount> random players. Don't need anything unique, but you can do so if you'd like."""
        pass
        #raise NotImplementedError()

    def initialise_with_data(self, materials: list[Material], caves: list[Cave], traders: list[Trader], player_names: list[int], emerald_info: list[float]):
        super().initialise_with_data(materials, caves, traders)
        for player, emerald in zip(player_names, emerald_info):
            self.players.append(Player(player, emeralds=emerald))
            self.players[-1].set_materials(self.get_materials())
            self.players[-1].set_caves(self.get_caves())
            self.players[-1].set_traders(self.get_traders())
        print("Players:\n\t", end="")
        print("\n\t".join(map(str, self.players)))

    def simulate_day(self):
        # 1. Traders make deals
        print("Traders Deals:\n\t", end="")
        print("\n\t".join(map(str, self.get_traders())))
        # 2. Food is offered
        offered_food = Food.random_food()
        print(f"\nFoods:\n\t{offered_food}")
        # 3. Each player selects a cave - The game does this instead.
        foods, balances, caves = self.select_for_players(offered_food)
        # 4. Quantites for caves is updated, some more stuff is added.
        self.verify_output_and_update_quantities(foods, balances, caves)

    def select_for_players(self, food: Food) -> tuple[list[Food|None], list[float], list[tuple[Cave, float]|None]]:
        """
        Since select_for_players is quite similar to select_food_and_caves from Player class, I can reuse code from
        there. As such, much of the code here is also used in select_food_and_caves, with some changes to better adapt
        a multiplayer game.

        The first for loop is used to determine whether the player in question is able to buy any food. If player has
        enough emeralds to buy food, it will be appended to player_food, otherwise, 'None' is appended to player_food,
        as per the spec sheet.

        The second for loop is used to determine the profitability of each cave, and whether the cave actually has
        materials that are purchasable by the traders. The ratio of trader deals to mining rate is assigned to each
        cave as a key, which is then stored in a hash table. The ratio of trader deals to mining rate is also added
        into a heap, where the most profitable cave can be extracted using .get_max().

        The third for loop is used to actually have the players go into the cave and mine the materials within. The
        materials are then sold to the trader, and the emeralds earned calculated and added to the player's balance.
        After that, the amount of materials remaining inside the cave is updated after the mining venture by the
        player.

        For example,

        Consider the players: Steve and Alex.
        Steve has a starting amount of 30 emeralds, whereas Alex has a starting amount of 15 emeralds.
        The food purchasable is only Apple Pie, with a price of 19 emeralds, and gives 100 hunger.
        Caves generated are Bleakcoast Cave, Boulderfall Cave, Darkshade, Pinemoon Cave, and Rebel's Cairn.
        Materials found in each cave are shown below, in a table.
                    _________________________________________________________________________________________
                    |Bleakcost Cave |Boulderfall Cave     |Darkshade     |Pinemoon Cave     |Rebel's Cairn  |
                    |_______________|_____________________|______________|__________________|_______________|
                    |4 Nether Bricks|8 Prismarine Crystals|2 Fishing Rods|3 Netherite Ingots|10 Gold Nuggets|
                    |_______________|_____________________|______________|__________________|_______________|

        Number of hunger bars needed to mine each material is shown below, in another table.
                    _________________________________________________________________________________________
                    |Nether Bricks |Prismarine Crystals |Fishing Rods   |Netherite Ingots   |Gold Nuggets   |
                    |______________|____________________|_______________|___________________|_______________|
                    |25.4          |14.7                |15.9           |23.7               |19.8           |
                    |______________|____________________|_______________|___________________|_______________|

        The selling price of each trader for the materials is shown below, in another table.
                    _________________________________________________________________________________________
                    |Drew Flynn    |Buck Pierce         |Jo Gillespie   |Letitia Roach      |Audrey Cobb    |
                    |______________|____________________|_______________|___________________|_______________|
                    |Fishing Rod   |Prismarine Crystals |Nether Bricks  |Netherite Ingots   |Gold Nuggets   |
                    |for 7.5       |for 8.5             |for 7.9        |for 8.9            |for 7.6        |
                    |______________|____________________|_______________|___________________|_______________|

        Before the game starts, the resources needed are all declared and initialised.

        The 3 different list, namely player_food, player_balance and player_caves that would be returned as a tuple
        are created.
        Hash table caves_hash is also created, along with the MaxHeap, deal_heap.

        First, Steve and Alex enter the game, and they check whether any food can be purchased. In this case, only
        Steve can buy the Apple Pie for 19 emeralds, whereas Alex cannot. As such, the player_food list is updated
        to contain [Apple Pie, None]. The balance for each player is also updated, and now Steve's balance is 11,
        whereas Alex's balance is still 15.

        After that, the profits from a cave is identified by calculating deal_ratio_miningrate, which is the amount
        of emeralds that can be earned from a particular cave when mined divided by the amount of hunger needed to
        mine the materials found within.

        The deal_ratio_miningrate is then added into caves_hash as a key to the cave name, and it is also added into
        deal_heap.

        In the next step, since Steve is first in line, .get_max() function is used on deal_heap, and the highest
        deal_ratio_miningrate is found and used as a key to get the name of the cave. In thi case, the most profitable
        cave is Boulderfall Cave, where 8 Prismarine Crystals can be found. The deal_ratio_miningrate for this cave
        is 4.6, the highest among all caves available. Steve then goes into the cave and mines the materials found.
        Since Steve only has 100 hunger, he can only mine 6.8 Prismarine Crystals. As such, after selling the
        Prismarine Crystals to Buck Pierce for 8.5 per Prismarine Crystal, he earns 6.8*8.5 = 57.8 emeralds.

        Steve's balance is now 11+57.8 = 68.8 emeralds.

        Since Alex had no hunger, he could not mine anything, and his balance stays at 15 emeralds.

        Each player's balance is then appended to player_balance, and the caves that they went to are also
        appended to player_caves respectively.

        The returned tuple should look like this:
        ([Apple Pie, None],[68.8, 15],[('Boulderfall Caves', 6.8),(None, None)])

        +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        PARAMETERS:
        The instance of MultiplayerGame
        food[Food]: food object to be inputted as chosen food sold.
        ...___...___...___...___...___...___...___...___...___...___...___...___...___...___...___...___...___...___
        METHOD DESCRIPTION:
        Similarly to select_food_and_caves in Player class, this method does almost the same thing, but for multiple
        players. With the addition of more players, a few limitations were added. Only a single food type is available,
        and players can only visit a single cave. All players will also be sharing the same few caves that can be
        entered and mined from.
        A tuple consisting of 3 lists would be returned. These lists contain the food that players choose, the balance
        of each player, and the caves chosen along with the quantity of minerals mined respectively.
        ...___...___...___...___...___...___...___...___...___...___...___...___...___...___...___...___...___...___
        RETURN:
        tuple[list[Food|None], list[float], list[tuple[Cave, float]|None]]:
        -   list[Food|None]: list of foods chosen by each player, or if no food was chosen, None
        -   list[float]: list of balance of each player after buying food and selling mined minerals
        -   list[tuple[Cave,float]|None]: list of caves visited and quantity of minerals mined by each player, or if
                                            none are mined, None
        ...___...___...___...___...___...___...___...___...___...___...___...___...___...___...___...___...___...___
        BEST AND WORST CASE COMPLEXITY: O(P+C+C) where C is number of caves, and P is number of players.
        """

        # assigning shared_caves_list with any player's cave list, since all players are using the same cave list.
        shared_caves_list = self.players[0].caves

        # putting the eventual lists of food, balance and caves as a list.
        # these lists, after being filled, will be put together in a tuple to be returned.
        player_food = []
        player_balance = []
        player_caves = []

        # initialising a hash table and a heap to be used.
        # hash tables have meaningful keys, whereas heaps are used to obtain max value easily
        caves_hash = LinearProbeTable(len(shared_caves_list), len(shared_caves_list))
        deal_heap = MaxHeap(len(shared_caves_list))
        traders_list = self.traders

        # for loop without any methods of more complexity than O(1) or nested loops
        # total complexity: O(P) where P is the number of players
        for i in range(len(self.players)):
            if self.players[i].balance >= food.food_price:
                self.players[i].balance -= food.food_price
                player_food.append(food)
            else:
                player_food.append('None')

        # for loop with methods .__getitem__, .insert, .add, all O(1) complexity
        # total complexity: O(C) where C is the number of caves
        for j in range(len(shared_caves_list)):
            cave = shared_caves_list[j]
            cave_mat = cave.cave_material.name
            cave_mat_mining_rate = cave.cave_material.mining_rate
            cave_quantity = cave.quantity

            traders_cave_mat = self.traders_hash.keys()
            if cave_mat in traders_cave_mat:
                trader_deal = self.traders_hash.__getitem__(cave_mat)
                deal_ratio_miningrate = (trader_deal * cave_quantity/cave_mat_mining_rate)
                caves_hash.insert(str(deal_ratio_miningrate), cave)
                deal_heap.add(deal_ratio_miningrate)

        # for loop with methods .__getitem__, .get_max(), both O(1) complexity
        # total complexity: O(P) where P is the number of players.
        for k in range(len(self.players)):
            current_cave = caves_hash.__getitem__(str(deal_heap.get_max()))
            material_deal_amount = self.traders_hash.__getitem__(current_cave.cave_material.name)
            material_mining_rate = current_cave.cave_material.mining_rate
            max_material_quantity = current_cave.quantity
            if player_food[k] is not None: 
                amount_to_mine = player_food[k].hunger_bars/material_mining_rate
            else:
                amount_to_mine = 0
            quantity_to_mine = max_material_quantity

            if amount_to_mine < max_material_quantity:
                quantity_to_mine = amount_to_mine

            # append current player's cave and quantity of minerals mined into list of player caves
            player_caves.append(current_cave, quantity_to_mine)

            # add more emeralds
            self.balance += (quantity_to_mine * material_deal_amount)

            # append current player's balance into list of player balance
            player_balance.append(self.balance)

            # update material amount in cave
            material_quantity_left = max_material_quantity - quantity_to_mine
            current_cave.quantity = material_quantity_left

        return tuple(player_food, player_balance, player_caves)

    def verify_output_and_update_quantities(self, food: Food | None, balance: float, caves: list[tuple[Cave, float]]) -> None:
        """
        PARAMETERS:
        The instance of MultiplayerGame
        food[Food | None]: food object to be inputted as chosen food, no input is accepeted as well.
        balance[float]: balance of player in question
        caves[list[tuple[Cave, float]]]: list of tuples containing caves and the materials

        ...___...___...___...___...___...___...___...___...___...___...___...___...___...___...___...___...___...___
        METHOD DESCRIPTION:
        Similar to verify_output_and_update_quantities(player_result) in SoloGame, checks all verification and updates
        all the needed values.
        ...___...___...___...___...___...___...___...___...___...___...___...___...___...___...___...___...___...___
        RETURN:
        [None]
        ...___...___...___...___...___...___...___...___...___...___...___...___...___...___...___...___...___...___
        COMPLEXITY FOR BEST CASE:
        O(1) : comparison of number of caves plundered and values do not equate
        COMPLEXITY FOR WORST CASE:
        O(C + C + C+ F + F + C^2), multiple iteration of caves and foods list to check values
        """


        if self.player.caves_explored != len(caves):
            raise AssertionError("Plundered caves do not match")

        print("done1")
        # check materials mined in each caves do not exceed amount
        for i in range(len(caves)):
            the_cave = caves[i][0].quantity
            print(the_cave)
            amounttocheck = caves[i][1] - caves[i][0].quantity
            print(amounttocheck)
            if (caves[i][1] - caves[i][0].quantity) > EPSILON:
                raise Error("material mined more than what is available")

        print("done2")
        # check materials mined in each caves
        for i in range(len(caves)):
            if caves[i][0].quantity < 0:
                raise Error("cave is empty")

        print("done3")
        # check food can be purchased in the first place
        if (food not in self.player.foods) and (self.player.original_balance > food.food_price):
            raise Error("Food could not be purchased")

        print("done4")
        # check balance given is correct
        #mat_with_best_deal = 0
        print("Traders Deals (in set traders ):\n\t", end="")
        print("\n\t".join(map(str, self.player.traders)))
        check_balance = 0
        for i in range(len(caves)):
            cave_mat = caves[i][0].cave_material.name
            mined_mat = caves[i][1]
            trader_deal_amount = self.player.traders_hash.__getitem__(cave_mat)
            check_balance += mined_mat * trader_deal_amount

        check_balance += self.player.balance_after_food #* 1.0)
        #balance = mined_mat * mat_with_best_deal
        print(balance)
        print(check_balance)
        print("done4.1")
        if abs(balance - check_balance) > EPSILON:
            raise Error("wrong balance")


        print("done5")
        # check food hunger bar is legit
        food_list = self.player.foods
        for the_food in food_list:
            if food.food_name == the_food.food_name:
                print(food.hunger_bars)
                print(the_food.hunger_bars)
                if food.hunger_bars != the_food.hunger_bars:
                    raise Error("food hunger bar is skewed")

        print("done6")
        # check food is legit
        food_name_list = []
        for i in range(len(food_list)):
            food_name_list.append(food_list[i].food_name)
        if food.food_name not in food_name_list:
            raise Error("food does not exist")

        print("done7")
        # check balance is at or below zero
        if balance < EPSILON:
            raise Error("zero balance")

        # update the quantities in caves
        cave_name_list = []
        for i in range(len(caves)):
            cave_name_list.append(caves[i][0].name)

        print(cave_name_list)
        new_cave_list = []
        for i in range(len(caves)):
            the_cave = caves[i][0]
            available_mat = caves[i][1]
            if the_cave.name in cave_name_list:
                updated_quantity = the_cave.quantity - available_mat
                for cave in self.caves:
                    if the_cave.name == cave.name:
                        cave.quantity = updated_quantity
        print("caves should be updated")


if __name__ == "__main__":

    r = 3 
    RandomGen.set_seed(r)
    print(r)

    g = SoloGame()
    g.initialise_game()

    g.simulate_day()
    g.finish_day()

    g.simulate_day()
    g.finish_day()

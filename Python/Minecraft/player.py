from __future__ import annotations

__author__ = "Scaffold by Jackson Goerner, Code by Myint Myat Thura, Lau Ka-Kiat, Wong Heng Yew, Tay Chean Hao"

from cave import Cave
from material import Material
from trader import Trader, RandomTrader
from food import Food
from constants import EPSILON
from avl import AVLTree
from random_gen import RandomGen
from hash_table import LinearProbeTable
from heap import MaxHeap

# List taken from https://minecraft.fandom.com/wiki/Mob
PLAYER_NAMES = [
    "Steve",
    "Alex",
    "ɘᴎiɿdoɿɘH",
    "Allay",
    "Axolotl",
    "Bat",
    "Cat",
    "Chicken",
    "Cod",
    "Cow",
    "Donkey",
    "Fox",
    "Frog",
    "Glow Squid",
    "Horse",
    "Mooshroom",
    "Mule",
    "Ocelot",
    "Parrot",
    "Pig",
    "Pufferfish",
    "Rabbit",
    "Salmon",
    "Sheep",
    "Skeleton Horse",
    "Snow Golem",
    "Squid",
    "Strider",
    "Tadpole",
    "Tropical Fish",
    "Turtle",
    "Villager",
    "Wandering Trader",
    "Bee",
    "Cave Spider",
    "Dolphin",
    "Enderman",
    "Goat",
    "Iron Golem",
    "Llama",
    "Panda",
    "Piglin",
    "Polar Bear",
    "Spider",
    "Trader Llama",
    "Wolf",
    "Zombified Piglin",
    "Blaze",
    "Chicken Jockey",
    "Creeper",
    "Drowned",
    "Elder Guardian",
    "Endermite",
    "Evoker",
    "Ghast",
    "Guardian",
    "Hoglin",
    "Husk",
    "Magma Cube",
    "Phantom",
    "Piglin Brute",
    "Pillager",
    "Ravager",
    "Shulker",
    "Silverfish",
    "Skeleton",
    "Skeleton Horseman",
    "Slime",
    "Spider Jockey",
    "Stray",
    "Vex",
    "Vindicator",
    "Warden",
    "Witch",
    "Wither Skeleton",
    "Zoglin",
    "Zombie",
    "Zombie Villager",
    "H̴͉͙̠̥̹͕͌̋͐e̸̢̧̟͈͍̝̮̹̰͒̀͌̈̆r̶̪̜͙̗̠̱̲̔̊̎͊̑̑̚o̷̧̮̙̗̖̦̠̺̞̾̓͆͛̅̉̽͘͜͝b̸̨̛̟̪̮̹̿́̒́̀͋̂̎̕͜r̸͖͈͚̞͙̯̲̬̗̅̇̑͒͑ͅi̶̜̓̍̀̑n̴͍̻̘͖̥̩͊̅͒̏̾̄͘͝͝ę̶̥̺̙̰̻̹̓̊̂̈́̆́̕͘͝͝"
]

class Player:
    """
        CLASS DESCRIPTION:
        Player class with class variables DEFAULT_EMERALDS, MIN_EMERALDS, MAX_EMERALDS and
        this class stores players attributes and variables which are to be implemented in methods
    """

    DEFAULT_EMERALDS = 50

    MIN_EMERALDS = 14
    MAX_EMERALDS = 40

    def __init__(self, name, emeralds=None) -> None:
        """
            PARAMETERS:
            objects instantiated:
            -   name: player name
            -   emeralds: emerald balance used to buy food
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            FUNCTION DESCRIPTION:
            -   __init__ magic method to initialise player name and emerald balance
            -   name and emeralds will be passed into the init function,
            -   rest of the stats such as original_balance, traders, foods will be defaulted
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [None]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all, only assigns values to variables and check for precondtions
        """
        self.player_name = name
        self.balance = self.DEFAULT_EMERALDS if emeralds is None else emeralds
        self.original_balance = 0
        self.balance_after_food = 0
        self.player_hunger_bar = 0
        self.traders = None
        self.traders_hash = None
        self.foods = None
        self.materials = None
        self.caves = None
        self.caves_explored = 0

    def set_traders(self, traders_list: list[Trader]) -> None:
        """
            PARAMETERS:
            traders_list[list]: a list of traders
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            -   Set traders and if each trader has a trade, sort highest trader among others (if any) with
                same material into a hashtable.
            -   The number of elements in hashtable for highest trader may be lesser than traders_list
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [None]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST CASE:
            O(1) : assign traders list to self.traders if all traders have no deal
            COMPLEXITY FOR WORST CASE:
            O(N)/O(T+T) : loop through list of traders twice , T denotes number of traders
        """
        i = 0
        # All traders in the list should not be selling anything without generating deal
        # Hence, testing the first trader is_currently_selling() can show it generate_deal() has been done
        if traders_list[i].is_currently_selling() == False:
            self.traders = traders_list # assign the traders_list to traders with no sorting for highest seller
        else:
            self.traders = traders_list
            old_traders_list = traders_list # assign traders_list as reference
            self.traders_hash = LinearProbeTable(len(old_traders_list), len(old_traders_list))
            intermediate_hash = LinearProbeTable(len(old_traders_list), len(old_traders_list)) # intermediate hash for sorting
            deal_heap = MaxHeap(len(old_traders_list))

            # for every trader in old_traders_list, insert trader deal (in str type) as key in hash and set item to trader
            # as for deal_heap, we add trader deal amount as key
            for trader in old_traders_list:
                intermediate_hash.insert(str(trader.deal_amount), trader)
                deal_heap.add(trader.deal_amount)

            material_list = [] # this list ensures we do not add another trader with lower deal of same material

            # we get highest deal in the intermediate_hash and add its material in material list to prevent lower deal of same material to be added
            for i in range(len(old_traders_list)):
                big_trader = intermediate_hash.__getitem__(str(deal_heap.get_max())) # highest trader regardless material
                big_trader_material = big_trader.material_chosen.name
                if big_trader_material not in material_list:
                    material_list.append(big_trader_material) # add material name to stop trader with lower deal
                    self.traders_hash.insert(big_trader.material_chosen.name, big_trader.deal_amount) # hash material name as key and the deal as item

    def set_foods(self, foods_list: list[Food]) -> None:
        """
            PARAMETERS:
            foods_list[list]: a list of foods
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            -   Set a list of foods to foods
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [None]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1) : assign foods list to self.foods

        """
        self.foods = foods_list

    @classmethod
    def random_player(self) -> Player:
        """
            PARAMETERS:
            The instances of Player class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            -   Create a random player with random player name,
                random amount of emeralds between MIN_EMERALDS and MAX_EMERALDS
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            Player class instance instantiated:
            player_name[str]: random player name from PLAYER_NAMES
            emerald_balance[int]: random amount of emerald
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1) : assigning random items to be instantiated
        """
        player_name = RandomGen.random_choice(PLAYER_NAMES)
        emerald_balance = RandomGen.randint(Player.MIN_EMERALDS,Player.MAX_EMERALDS)
        return self(player_name,emerald_balance)

    def set_materials(self, materials_list: list[Material]) -> None:
        """
            PARAMETERS:
            materials_list[list]: a list of materials
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            -   Set a list of materials
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [None]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1) : assign a list of materials to self.materials
        """
        self.materials = materials_list

    def set_caves(self, caves_list: list[Cave]) -> None:
        """
            PARAMETERS:
            caves_list[list]: a list of caves
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            -   Set a list of caves
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [None]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1) : assign a list of caves to self.caves
        """
        self.caves = caves_list

    def select_food_and_caves(self) -> tuple[Food | None, float, list[tuple[Cave, float]]]:
        """
            PARAMETERS:
            The instances of Player class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            General Idea
            -   Select the food that offers best hunger bars per price and decide the order of caves to explore
                based on sorting a list of caves based on its deal_ratio_miningrate amount.
            The Approach
            -   To earn the highest possible emerald amount, getting a food which offer best hunger bar per price
                ratio is important. To get the ratio, we calculate by

                food_hunger_bar/food_price

            -   Also make sure the initial emerald balance is sufficient to buy the food
            -   Material mining rate and quantity with its selling price are next to be considered
            -   We use this formula call deal_ratio_miningrate to decide cave is worth mining, which is

                (trader_deal * cave_material_quantity/cave_material_mining_rate)

            -   Caves quantity are focused instead of traders selling price as
                there may be a case where there are two caves of same material that can be sold at higher price
                (one higher and another lower quantity) than a cave of different material with lower price
                Focusing on trader would miss the opportunity of mining the other cave
            -   Insert the deal_ratio_miningrate as key in a hashtable with its item as Cave. We also insert
                the ratio into a heap. When is time to get the cave with best ratio, you retrieve max ratio in heap
                and use it as key for hashtable. Through that, we are able to get the Cave we wanted to mine
            -   The reason for this two combination of ADTs is that it helps to reduce complexity by a lot.
                Without the combo, storing the ratio in AVLTree after identification would take up O(C*T) and getting
                the Cave out would be O(C*log(C)*T) where C is number of caves and T is number of traders.
                With this combo, complexity is reduced to O(C) instead of O(C*T) and O(C) instead of O(C*log(C)*T)
            -   As such, we mine caves in a descending order of deal_ratio_miningrate until the food hunger bar
                is below zero or all the caves have been mined
            Example for demonstration
            -   Consider the stats
                PLAYER_STATS:
                Player Name: Steve
                Emerald Balance: 50

                FOODS:
                Tomato Seeds with 298 hunger bars is priced at 18 (ratio ~16.56)
                Mutton Chops with 235 hunger bars is priced at 39 (ratio ~6.03)
                Mixed Salad with 109 hunger bars is priced at 46  (ratio ~2.37)

                CAVES:
                <Cave: Redoran's Retreat. 8.0 of [Slimeball: 32.68🍗/💎]>   (ratio ~1.19)
                <Cave: Gromm's Pass. 2.0 of [Rabbit Hide: 32.29🍗/💎]>      (ratio ~0.41)
                <Cave: Coldcinder Cave. 4.0 of [Rabbit Hide: 32.29🍗/💎]>   (ratio ~0.813)

                TRADERS_HASH:
                ( not traders itself as this includes other traders of same material of lower deal )
                ( to understand more, refer to set_traders() in Player class)
                <RangeTrader: Letitia Roach buying [Slimeball: 32.68🍗/💎] for 4.86💰>
                <RandomTrader: Curtis Dougherty buying [Rabbit Hide: 32.29🍗/💎] for 6.57💰>
                <RangeTrader: Winston York buying [Brick: 21.41🍗/💎] for 7.38💰>

            -   First, we evaluate which food offers best hunger bar to price ratio
                which is Tomato Seeds, giving around 16.56. Hunger bar is 298, emerald balance now 32
            -   Then, we calculate the deal_ratio_miningrate and put them into hashtable and heap
            -   While food hunger bar and heap length containing the ratio as element are above zero,
                1.
                Loop through CAVES and get max ratio off heap (1.19) and retrieve the Cave by using ratio as key access
                The Cave now is Redoran's Retreat. Calculate amount can be mined (298/32.68).
                As we can mine more than what is available (~9.11 > 8.0), we mine max quantity
                Emerald balance now 70.88 (32 + (8 * 4.86)) and hunger bar now 36.56 (298 - 261.44).
                Heap length now is 2 (3-1) after getting max ratio
                2.
                Since hunger bar and heap length above zero, we loop again
                max ratio (0.813)
                Cave is Coldcinder Cave
                amount can be mined ~1.13 (36.56/32.29)
                Since less than max quantity (~1.13 < 4.0), we mine ~1.13
                emerald balance now ~78.3 (70.88 + (~1.13 * 6.57))
                hunger bar now 0 (36.56 - 36.56)
                heap length 1 (2-1)
                3.
                As hunger bar is 0, we exit the loop and return the tuple containing
                Food : Tomato Seeds with 298 hunger bars is priced at 18
                float : ~78.3
                list(tuple[Cave, float]):
                [(<Cave: Redoran's Retreat. 8.0 of [Slimeball: 32.68🍗/💎]>, 8.0),
                (<Cave: Gromm's Pass. 4.0 of [Rabbit Hide: 32.29🍗/💎]> , ~1.13)]

                Note:
                The use of approximation is to simplify numbers with recurring decimals
                Actual calculation takes into account of the whole floating point numbers

            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            A tuple which contains:
            Food | None : the chosen food used to mine materials
            float[float]: the emerald balance after journey of mining materials and purchasing (if any)
            list[tuple[Cave, float]] : list of plundered caves with the quantity mined at each cave
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST CASE:
            O(F) :  run through foods list and no food is chosen because insufficient emerald
            COMPLEXITY FOR WORST CASE:
            O(F+C+C) :  loop through a list of foods to determine best food,
                    first loop of cave list to calculate deal_ratio_miningrate,
                    then second loop of sorted caves list to mine materials

            F = number of foods
            C = number of caves
        """
        self.caves_explored = 0
        num_of_emeralds = self.balance # how many emerald we have
        self.original_balance = num_of_emeralds # store the initial balance

        # calculate hunger bar to price ratio
        food_hunger_bar = 0
        food_chosen = None
        max_bar_to_price_ratio = 0
        for food in self.foods:
            if self.balance >= food.food_price: # if player can purchase the food
                food_hunger_bar = food.hunger_bars
                food_price = food.food_price
                bar_to_price_ratio = food_hunger_bar/food_price # calculate the ratio

                # compare max ratio as the food with max ratio will be assign
                # to food chosen until next food with higher ratio replaces it
                if max_bar_to_price_ratio < bar_to_price_ratio:
                    max_bar_to_price_ratio = bar_to_price_ratio
                    food_chosen = food

        # As till here, we have achieved O(F) where F is number of foods
        # by looping through the entire foods list to determine which food
        # has best hunger bar to price ratio

        caves_and_quantity_mined = []
        # if no food is chosen,
        # only return food_chosen as None, original balance and empty caves_and_quantity_mined list
        if food_chosen != None:
            self.player_hunger_bar = food_chosen.hunger_bars # save player hunger bars before plundering the caves
            emerald_balance = self.balance - food_chosen.food_price
            self.balance_after_food = emerald_balance # update the balance after food purchase
            self.balance = emerald_balance # new balance

            # caves hash is used to store deal_ratio_miningrate (in str) as key that holds the cave
            caves_hash = LinearProbeTable(len(self.caves), len(self.caves))

            # deal_heap is used to store deal_ratio_miningrate (to be used as key for caves_hash)
            deal_heap = MaxHeap(len(self.caves))
            traders_list = self.traders
            food_hunger_bar = food_chosen.hunger_bars
            used_caves_list = self.caves

            # running through every cave,
            # we calculate the deal_ratio_miningrate
            for cave in self.caves:
                cave_mat = cave.cave_material.name
                cave_mat_mining_rate = cave.cave_material.mining_rate
                cave_quantity = cave.quantity
                traders_cave_mat = self.traders_hash.keys() # get a list of materials that can be traded with traders

                # if the material exist in the list
                if cave_mat in traders_cave_mat:
                    trader_deal = self.traders_hash.__getitem__(cave_mat) # retrieve deal amount for the material
                    deal_ratio_miningrate = (trader_deal * cave_quantity/cave_mat_mining_rate) # calculate the ratio
                    caves_hash.insert(str(deal_ratio_miningrate), cave)
                    deal_heap.add(deal_ratio_miningrate)

            # As from food is not None till here, the complexity increases to O(F+C) where C is number of caves
            # For O(C), we loop through the entire cave list to calculate the deal_ratio_miningrate
            # Inserting key to hashtable and adding to heap are O(1) operations and will not be considered for big O
            # Other O(1) operations include comparisons and assigning values
            caves_list = self.caves
            initial_hunger_bar = food_hunger_bar

            # loop through until hunger bar is below zero or all caves that could be mined are empty
            while (food_hunger_bar > 0) and (len(deal_heap) > 0):
                current_cave = caves_hash.__getitem__(str(deal_heap.get_max())) # get cave with current best ratio
                material_deal_amount = self.traders_hash.__getitem__(current_cave.cave_material.name) # get deal based on current cave material
                material_mining_rate = current_cave.cave_material.mining_rate
                max_material_quantity = current_cave.quantity
                amount_to_mine = food_hunger_bar/material_mining_rate # calculate the amount that can be mined
                quantity_to_mine = max_material_quantity # assign max quantity

                # if player cannot mine max quantity from a cave
                if amount_to_mine < max_material_quantity:
                    quantity_to_mine = amount_to_mine # assign amount that could be mined

                # update caves and quantity mined list in tuple
                caves_and_quantity_mined.append((current_cave,quantity_to_mine))

                # add more emeralds
                self.balance += (quantity_to_mine * material_deal_amount)

                # update food hunger bar
                food_hunger_bar -= (quantity_to_mine * material_mining_rate)

                # update material amount in cave
                material_quantity_left = max_material_quantity - quantity_to_mine

                self.caves_explored += 1 # increment self.caves_explored by 1

            # As from checking whether hunger bar and heap length are above zero till here,
            # the complexity increases to O(F+C+C) where C is number of caves
            # For another O(C), we loop through the entire cave list to mine at worst (may exit earlier)
            # Getting max ratio is a O(1) as we are retrieving index 1 of heap which is the largest
            # Other operations like assigning values and comaprisons are O(1) operations and will not be considered for big O

        return food_chosen, self.balance, caves_and_quantity_mined

    def __str__(self) -> str:
        """
            PARAMETERS:
            The instances of Player class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            -   Return a string in format given which contains player name and
                the emerald balance the player has
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            A formatted string
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1) : where n is the string created based on player name and emerald balance through formatting
        """
        return "Player Name: {0} \nEmerald Balance: {1}".format(self.player_name,self.balance)

if __name__ == "__main__":

    print(Player("Steve"))
    print(Player("Alex", emeralds=1000))

from __future__ import annotations

from abc import abstractmethod, ABC
from material import Material, RANDOM_MATERIAL_NAMES
from random_gen import RandomGen
from hash_table import LinearProbeTable
from avl import AVLTree
from heap import MaxHeap

# Generated with https://www.namegenerator.co/real-names/english-name-generator
TRADER_NAMES = [
    "Pierce Hodge",
    "Loren Calhoun",
    "Janie Meyers",
    "Ivey Hudson",
    "Rae Vincent",
    "Bertie Combs",
    "Brooks Mclaughlin",
    "Lea Carpenter",
    "Charlie Kidd",
    "Emil Huffman",
    "Letitia Roach",
    "Roger Mathis",
    "Allie Graham",
    "Stanton Harrell",
    "Bert Shepherd",
    "Orson Hoover",
    "Lyle Randall",
    "Jo Gillespie",
    "Audie Burnett",
    "Curtis Dougherty",
    "Bernard Frost",
    "Jeffie Hensley",
    "Rene Shea",
    "Milo Chaney",
    "Buck Pierce",
    "Drew Flynn",
    "Ruby Cameron",
    "Collie Flowers",
    "Waldo Morgan",
    "Winston York",
    "Dollie Dickson",
    "Etha Morse",
    "Dana Rowland",
    "Eda Ryan",
    "Audrey Cobb",
    "Madison Fitzpatrick",
    "Gardner Pearson",
    "Effie Sheppard",
    "Katherine Mercer",
    "Dorsey Hansen",
    "Taylor Blackburn",
    "Mable Hodge",
    "Winnie French",
    "Troy Bartlett",
    "Maye Cummings",
    "Charley Hayes",
    "Berta White",
    "Ivey Mclean",
    "Joanna Ford",
    "Florence Cooley",
    "Vivian Stephens",
    "Callie Barron",
    "Tina Middleton",
    "Linda Glenn",
    "Loren Mcdaniel",
    "Ruby Goodman",
    "Ray Dodson",
    "Jo Bass",
    "Cora Kramer",
    "Taylor Schultz",
]

class Trader(ABC):

    def __init__(self, name: str) -> None:
        """
            PARAMETERS:
            Name of the trader
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            -   Constructor. This will instantiate all the instance variables
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [None]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST CASE:
            O(1) : Assignment for instance variables
        """
        self.name = name
        self.trader_type = None
        self.inventory = AVLTree() # the inventory of materials they wanna buy
        self.active_deal = None # set to 1 or 0 based on presence of active deal
        self.deal_amount = 0
        self.material_chosen = None
        self.mat_in_inventory = []
        #raise NotImplementedError()

    @classmethod
    def random_trader(cls):
        """
            PARAMETERS:
            CLS
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            -   Trader name will be set to a random trader name chosen from the list of trader names.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            Trader name
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST CASE:
            O(1) : Assignment for instance variables and simple return statement.
        """
        trader_name = RandomGen.random_choice(TRADER_NAMES)
        return cls(trader_name)
        #raise NotImplementedError()

    @ abstractmethod
    def set_all_materials(self, mats: list[Material]) -> None:
        """
            PARAMETERS:
            List of materials
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            -   For each item in the list of materials, it will be appended to the inventory.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [None]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST CASE:
            O(n) : Where n is the size of the list.
        """
        pass
        #raise NotImplementedError()

    @ abstractmethod
    def add_material(self, mat: Material) -> None:
        """
            PARAMETERS:
            Material object
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            -   Material's mining rate will be added to the inventory.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [None]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST CASE:
            O(1) : Assignment for instance variable.
        """
        pass

        #raise NotImplementedError()

    def is_currently_selling(self) -> bool:
        """
            PARAMETERS:
            [None]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            -   Will return a boolean true if there is a current deal in the inventory.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [None]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST CASE:
            O(1) : Assignment for instance variable.
        """
        if self.material_chosen is not None and self.deal_amount != 0:
            return True
        else:
            return False
        #return self.current_deal() is not None # unsure
        #raise NotImplementedError()

    def current_deal(self) -> tuple[Material, float]:
        if self.material_chosen is None and self.deal_amount == 0:
            raise ValueError("current deal not generated")
        return (self.material_chosen, self.deal_amount)
        # return ( random material and price for trade)
        #pass
        #raise NotImplementedError()

    @ abstractmethod
    def generate_deal(self) -> None:
        pass

        #raise NotImplementedError()

    def stop_deal(self) -> None:
        self.deal_amount = 0 # unsure either
        self.material_chosen = None
        #raise NotImplementedError()

    def __str__(self) -> str:
        # maybe show the whole list of deals
        mat_name = None
        mat_rate = None
        if self.material_chosen is not None:
            mat_name = self.material_chosen.name
            mat_rate = self.material_chosen.mining_rate
        return "<{0}: {1} buying [{2}: {3}🍗/💎] for {4}💰>".format(self.trader_type, self.name, mat_name, mat_rate,self.deal_amount)
        # <HardTrader: Mr Barnes buying [Gunpowder: 8🍗/💎] for 2.01>

        #raise NotImplementedError()

class RandomTrader(Trader):

    def __init__(self, name):
        """
            PARAMETERS:
            Name of the food, hunger bars and price
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            -   Constructor. This will instantiate all the instance variables
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [None]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST CASE:
            O(1) : Assignment for instance variables
        """
        Trader.__init__(self, name)
        self.trader_type = "RandomTrader"

    def set_all_materials(self, mats: list[Material]) -> None:
        """
            PARAMETERS:
            List of materials
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            -   For each item in the list of materials, it will be appended to the inventory.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [None]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST CASE:
            O(n) : Where n is the size of the list.
        """
        self.inventory = AVLTree() # reset the entire inventory???
        self.mat_in_inventory = []
        #print(self.inventory.is_empty())
        #len_mat_lst = len(mats)
        for item in mats: #len_mat_lst):
            self.add_material(item) #mats[i])
        #print(len(self.inventory))

    def add_material(self, mat: Material) -> None:
        """
            PARAMETERS:
            Material object
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            -   Material's mining rate will be added to the inventory.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [None]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST CASE:
            O(1) : Assignment for instance variable.
        """
        self.inventory[mat.name] = mat # insert Material into inventory avl tree based on material name
        self.mat_in_inventory.append(mat.name)

    def generate_deal(self):
        """
            PARAMETERS:
            [None]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            -   Will add the material name from the material in the inventory. THe material chosen will be set as
                a randmo material from the inventory. The deal price will go through an arithmetic function.
                The active deal counter will go up by 1.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [None]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST CASE:
            O(1) : Assignment for instance variable.
        """
        rand_mat_name = RandomGen.random_choice(self.mat_in_inventory)
        self.material_chosen = self.inventory[rand_mat_name]
        self.deal_amount = round(2 + 8 * RandomGen.random_float(), 2)


class RangeTrader(Trader):

    def __init__(self, name):
        """
            PARAMETERS:
            Name of the food, hunger bars and price
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            -   Constructor. This will instantiate all the instance variables
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [None]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST CASE:
            O(1) : Assignment for instance variables
        """
        Trader.__init__(self, name)
        self.trader_type = "RangeTrader"

    def set_all_materials(self, mats: list[Material]) -> None:
        """
            PARAMETERS:
            List of materials
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            -   For each item in the list of materials, it will be appended to the inventory.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [None]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST CASE:
            O(n) : Where n is the size of the list.
        """
        self.inventory = AVLTree() # reset the entire inventory???
        self.mat_in_inventory = []
        len_mat_lst = len(mats)
        for i in range(len_mat_lst):
            self.add_material(mats[i])

    def add_material(self, mat: Material) -> None:
        self.inventory[mat.mining_rate] = mat # insert Material into inventory avl tree based on material name

    def generate_deal(self):
        """
            PARAMETERS:
            [None]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            -   Will add the material name from the material in the inventory. THe material chosen will be set as
                a randmo material from the inventory. The deal price will go through an arithmetic function.
                The active deal counter will go up by 1.
            - i will be assigned a random value range frmo 0 to the length of the inventory. This will later
            be used to choose the possible items.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [None]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST CASE:
            O(1) : Assignment for instance variable.
        """
        i = RandomGen.randint(1,len(self.inventory))
        j = RandomGen.randint(i,len(self.inventory))
        print(i)
        print(j)
        mat_list_available = self.materials_between(i-1,j-1)
        print(mat_list_available)
        if len(mat_list_available) != 0: # nothing in the list
            self.material_chosen = RandomGen.random_choice(mat_list_available)
            self.deal_amount = round(2 + 8 * RandomGen.random_float(), 2)

    def materials_between(self, i: int, j: int) -> list[Material]:
        return self.inventory.range_between(i,j) # may need to change the floating point comparison
        #raise NotImplementedError()

class HardTrader(Trader):

    def __init__(self, name):
        """
            PARAMETERS:
            Name of the food, hunger bars and price
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            -   Constructor. This will instantiate all the instance variables
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [None]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST CASE:
            O(1) : Assignment for instance variables
        """
        Trader.__init__(self, name)
        self.trader_type = "HardTrader"

    def set_all_materials(self, mats: list[Material]) -> None:
        """
            PARAMETERS:
            List of materials
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            -   For each item in the list of materials, it will be appended to the inventory.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [None]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST CASE:
            O(n) : Where n is the size of the list.
        """
        self.inventory = AVLTree() # reset the entire inventory???
        self.mat_in_inventory = []
        len_mat_lst = len(mats)
        for i in range(len_mat_lst):
            self.add_material(mats[i])

    def add_material(self, mat: Material) -> None:
        """
            PARAMETERS:
            Material object
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            -   Material's mining rate will be added to the inventory.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [None]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST CASE:
            O(1) : Assignment for instance variable.
        """
        self.inventory[mat.mining_rate] = mat # insert Material into inventory avl tree based on material name

    def generate_deal(self):
        """
            PARAMETERS:
            [None]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            -   Will add the material name from the material in the inventory. THe material chosen will be set as
                a randmo material from the inventory. The deal price will go through an arithmetic function.
                The active deal counter will go up by 1.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [None]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST CASE:
            O(1) : Assignment for instance variable.
        """
        # find the hardest to mine
        #current = self.inventory.root
        #while current.right is not None:
        #    current = current.right
        last_inventory_index = len(self.inventory) - 1
        material_chosen_list = self.inventory.range_between(last_inventory_index, last_inventory_index) # remove and return
        self.material_chosen = material_chosen_list[0]
        self.inventory.__delitem__(self.material_chosen.mining_rate) # get the key
        # pop out everything to a list to update the inventory
        # self.inventory = self.set_all_materials()
        self.deal_amount = round(2 + 8 * RandomGen.random_float(), 2)
    #pass
"""
if __name__ == "__main__":
    trader = RangeTrader("Jackson") # RangeTrader
    #print("\n")
    print(trader)
    trader.set_all_materials([
        Material("Coal", 4.5), # 4.5
        Material("Diamonds", 3), # 3
        Material("Redstone", 20), # 20
    ])
    #print(len(trader.inventory))

    trader.generate_deal()
    #print()
    #print(len(trader.inventory))
    print(trader)
    trader.stop_deal()
    #print()
    print(trader)
"""
"""
if __name__ == "__main__":
    t = RandomTrader.random_trader()
    a, b, c = [
        Material("Arrow", 1),
        Material("Axe", 2),
        Material("Bow", 3),
    ]
    print(a)
    t.set_all_materials([a])
    # This resets the traders inventory to just a.
    t.generate_deal()
    print(t.material_chosen)
    print(t.deal_amount)
    print(t.is_currently_selling())
"""
"""
    t.set_all_materials([a, b])
    assertFalse(t.is_currently_selling())
    # Make a deal. The material in the deal should be either a or b.
    t.generate_deal()
    self.assertTrue(t.is_currently_selling())
    self.assertIn(t.current_deal()[0], [a, b])
    t.add_material(c)
    # Now the trader has access to a, b and c.
    t.generate_deal()
    self.assertTrue(t.is_currently_selling())
    self.assertIn(t.current_deal()[0], [a, b, c])
    t.stop_deal()
    self.assertFalse(t.is_currently_selling())
    print(str(a))
    t.set_all_materials([a])
    # This resets the traders inventory to just a.
    t.generate_deal()
    #print(t.material_chosen.material_name)
    self.assertTrue(t.is_currently_selling())
    self.assertIn(t.current_deal()[0], [a])
    t.add_material(c)
    # And now we have access to a and c.
    t.generate_deal()
    self.assertTrue(t.is_currently_selling())
    self.assertIn(t.current_deal()[0], [a, c])
"""

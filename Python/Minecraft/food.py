from __future__ import annotations

from material import Material
from random_gen import RandomGen

# List of food names from https://github.com/vectorwing/FarmersDelight/tree/1.18.2/src/main/resources/assets/farmersdelight/textures/item
FOOD_NAMES = [
    "Apple Cider",
    "Apple Pie",
    "Apple Pie Slice",
    "Bacon",
    "Bacon And Eggs",
    "Bacon Sandwich",
    "Baked Cod Stew",
    "Barbecue Stick",
    "Beef Patty",
    "Beef Stew",
    "Cabbage",
    "Cabbage Leaf",
    "Cabbage Rolls",
    "Cabbage Seeds",
    "Cake Slice",
    "Chicken Cuts",
    "Chicken Sandwich",
    "Chicken Soup",
    "Chocolate Pie",
    "Chocolate Pie Slice",
    "Cod Slice",
    "Cooked Bacon",
    "Cooked Chicken Cuts",
    "Cooked Cod Slice",
    "Cooked Mutton Chops",
    "Cooked Rice",
    "Cooked Salmon Slice",
    "Dog Food",
    "Dumplings",
    "Egg Sandwich",
    "Fish Stew",
    "Fried Egg",
    "Fried Rice",
    "Fruit Salad",
    "Grilled Salmon",
    "Ham",
    "Hamburger",
    "Honey Cookie",
    "Honey Glazed Ham",
    "Honey Glazed Ham Block",
    "Horse Feed",
    "Hot Cocoa",
    "Melon Juice",
    "Melon Popsicle",
    "Milk Bottle",
    "Minced Beef",
    "Mixed Salad",
    "Mutton Chops",
    "Mutton Wrap",
    "Nether Salad",
    "Noodle Soup",
    "Onion",
    "Pasta With Meatballs",
    "Pasta With Mutton Chop",
    "Pie Crust",
    "Pumpkin Pie Slice",
    "Pumpkin Slice",
    "Pumpkin Soup",
    "Ratatouille",
    "Raw Pasta",
    "Rice",
    "Rice Panicle",
    "Roast Chicken",
    "Roast Chicken Block",
    "Roasted Mutton Chops",
    "Rotten Tomato",
    "Salmon Slice",
    "Shepherds Pie",
    "Shepherds Pie Block",
    "Smoked Ham",
    "Squid Ink Pasta",
    "Steak And Potatoes",
    "Stuffed Potato",
    "Stuffed Pumpkin",
    "Stuffed Pumpkin Block",
    "Sweet Berry Cheesecake",
    "Sweet Berry Cheesecake Slice",
    "Sweet Berry Cookie",
    "Tomato",
    "Tomato Sauce",
    "Tomato Seeds",
    "Vegetable Noodles",
    "Vegetable Soup",
]

class Food:

    def __init__(self, name: str, hunger_bars: int, price: int) -> None:
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
        self.food_name = name
        self.hunger_bars = hunger_bars
        self.food_price = price
        #raise NotImplementedError()

    def __str__(self) -> str:
        """
            PARAMETERS:
            [None]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            -   Magic method to display the information of an object. Such as name of the food, the hunger
                bars, and the price of the food.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            Returns a string representation of the object.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST CASE:
            O(1) : Simple return statement
        """
        return f"{self.food_name} with {self.hunger_bars} hunger bars is priced at {self.food_price}"
        #raise NotImplementedError()

    @classmethod
    def random_food(cls) -> Food:
        """
            PARAMETERS:
            CLS
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            -   The method will take a random food name from the list of food names, it will also take a 
                random hunger bar from a random range between 100 adn 500. It will take the price from 
                a random range between 10 and 60. Then it will return a tuple.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            Returns food name, hunger bars and price.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST CASE:
            O(1) : Return statement for tuples.
        """
        food_name = RandomGen.random_choice(FOOD_NAMES)
        hunger_bars = RandomGen.randint(100,500) # no limit just arbitrary values
        price = RandomGen.randint(10,60) # no limit same idea
        return cls(food_name,hunger_bars,price)
        #raise NotImplementedError()

if __name__ == "__main__":
    print(Food.random_food())


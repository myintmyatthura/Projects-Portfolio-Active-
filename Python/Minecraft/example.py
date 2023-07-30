from game import SoloGame
from material import Material
from cave import Cave
from trader import RandomTrader
from food import Food

gold = Material("Gold Nugget", 27.24)
netherite = Material("Netherite Ingot", 20.95)
fishing_rod = Material("Fishing Rod", 26.93)
ender_pearl = Material("Ender Pearl", 13.91)
prismarine = Material("Prismarine Crystal", 11.48)

materials = [
    gold,
    netherite,
    fishing_rod,
    ender_pearl,
    prismarine,
]

caves = [
    Cave("Boulderfall Cave", prismarine, 10),
    Cave("Castle Karstaag Ruins", netherite, 4),
    Cave("Glacial Cave", gold, 3),
    Cave("Orotheim", fishing_rod, 6),
    Cave("Red Eagle Redoubt", fishing_rod, 3),
]

waldo = RandomTrader("Waldo Morgan")
waldo.add_material(fishing_rod)
waldo.generate_deal()
waldo.sell = (fishing_rod, 7.44) # This is how my solution can hackily set the selling price - your solution does NOT need to support the same.
orson = RandomTrader("Orson Hoover")
orson.add_material(gold)
orson.generate_deal()
orson.sell = (gold, 7.70) # This is how my solution can hackily set the selling price - your solution does NOT need to support the same.
lea = RandomTrader("Lea Carpenter")
lea.add_material(prismarine)
lea.generate_deal()
lea.sell = (prismarine, 7.63) # This is how my solution can hackily set the selling price - your solution does NOT need to support the same.
ruby = RandomTrader("Ruby Goodman")
ruby.add_material(netherite)
ruby.generate_deal()
ruby.sell = (netherite, 9.78) # This is how my solution can hackily set the selling price - your solution does NOT need to support the same.
mable = RandomTrader("Mable Hodge")
mable.add_material(gold)
mable.generate_deal()
mable.sell = (gold, 5.40) # This is how my solution can hackily set the selling price - your solution does NOT need to support the same.

traders = [
    waldo,
    orson,
    lea,
    ruby,
    mable,
]

g = SoloGame()
g.initialise_with_data(materials, caves, traders, ["Jackson"], [50])

# Avoid simulate_day - This regenerates trader deals and foods.
foods = [
    Food("Cabbage Seeds", 106, 30),
    Food("Fried Rice", 129, 24),
    Food("Cooked Chicken Cuts", 424, 19),
]

g.player.set_foods(foods)
food, balance, caves = g.player.select_food_and_caves()
# Food = Cooked Chicken Cuts
# Balance = 209.21473449684368
# Caves = [
    # (<Cave: Castle Karstaag Ruins. 4 of [Netherite Ingot: 20.95🍗/💎]>, 4.0), 
    # (<Cave: Red Eagle Redoubt. 3 of [Fishing Rod: 26.93🍗/💎]>, 3.0),
    # (<Cave: Glacial Cave. 3 of [Gold Nugget: 27.24🍗/💎]>, 3.0), 
    # (<Cave: Boulderfall Cave. 10 of [Prismarine Crystal: 11.48🍗/💎]>, 10.0), 
    # (<Cave: Orotheim. 6 of [Fishing Rod: 26.93🍗/💎]>, 2.335313776457482), 
# ]
print(food, balance, caves)

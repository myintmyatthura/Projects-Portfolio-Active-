from game import MultiplayerGame
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

g = MultiplayerGame()
g.initialise_with_data(materials, caves, traders, ["Alexey", "Jackson", "Saksham", "Brendon"], [50, 14, 35, 44])

# Avoid simulate_day - This regenerates trader deals and foods.
foods, balances, caves = g.select_for_players(Food("Cooked Chicken Cuts", 100, 19))
# Foods = [
    # Cooked Chicken Cuts
    # None
    # Cooked Chicken Cuts
    # Cooked Chicken Cuts
# ]
# Balances = [
    # 97.46341463414635
    # 14
    # 55.12
    # 52.62718158187894
# ]
# Caves = [
    # (<Cave: Boulderfall Cave. 10 of [Prismarine Crystal: 11.48🍗/💎]>, 8.710801393728223)
    # None
    # (<Cave: Castle Karstaag Ruins. 4 of [Netherite Ingot: 20.95🍗/💎]>, 4)
    # (<Cave: Orotheim. 6 of [Fishing Rod: 26.93🍗/💎]>, 3.7133308577794284)
# ]
print(foods, balances, caves)

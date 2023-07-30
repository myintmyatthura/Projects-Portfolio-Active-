from random_gen import RandomGen

# Material names taken from https://minecraft-archive.fandom.com/wiki/Items
RANDOM_MATERIAL_NAMES = [
    "Arrow",
    "Axe",
    "Bow",
    "Bucket",
    "Carrot on a Stick",
    "Clock",
    "Compass",
    "Crossbow",
    "Exploration Map",
    "Fire Charge",
    "Fishing Rod",
    "Flint and Steel",
    "Glass Bottle",
    "Dragon's Breath",
    "Hoe",
    "Lead",
    "Map",
    "Pickaxe",
    "Shears",
    "Shield",
    "Shovel",
    "Sword",
    "Saddle",
    "Spyglass",
    "Totem of Undying",
    "Blaze Powder",
    "Blaze Rod",
    "Bone",
    "Bone meal",
    "Book",
    "Book and Quill",
    "Enchanted Book",
    "Bowl",
    "Brick",
    "Clay",
    "Coal",
    "Charcoal",
    "Cocoa Beans",
    "Copper Ingot",
    "Diamond",
    "Dyes",
    "Ender Pearl",
    "Eye of Ender",
    "Feather",
    "Spider Eye",
    "Fermented Spider Eye",
    "Flint",
    "Ghast Tear",
    "Glistering Melon",
    "Glowstone Dust",
    "Gold Ingot",
    "Gold Nugget",
    "Gunpowder",
    "Ink Sac",
    "Iron Ingot",
    "Iron Nugget",
    "Lapis Lazuli",
    "Leather",
    "Magma Cream",
    "Music Disc",
    "Name Tag",
    "Nether Bricks",
    "Paper",
    "Popped Chorus Fruit",
    "Prismarine Crystal",
    "Prismarine Shard",
    "Rabbit's Foot",
    "Rabbit Hide",
    "Redstone",
    "Seeds",
    "Beetroot Seeds",
    "Nether Wart Seeds",
    "Pumpkin Seeds",
    "Wheat Seeds",
    "Slimeball",
    "Snowball",
    "Spawn Egg",
    "Stick",
    "String",
    "Wheat",
    "Netherite Ingot",
]

class Material:
    def __init__(self, name: str, mining_rate: float) -> None:
        """
            PARAMETERS:
            Name of the material and the mining rate.
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
        self.mining_rate = mining_rate
    
    def __str__(self) -> str:
        """
            PARAMETERS:
            [None]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            -   Magic method to display the string representation of an object. In this instance, the magic 
                method will return a string that has the material name and mining rate.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            Returns a string representation of the object.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST CASE:
            O(1) : Simple return statement
        """
        return f"[{self.name}: {self.mining_rate}🍗/💎]"

    @classmethod
    def random_material(cls):
        """
            PARAMETERS:
            CLS
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            -   The method will take a random name from the list of material names. It will take a random 
                number of mining rate from a range of numbers. It will then return the material and the
                mining rate.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            Returns material name and mining rate.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST CASE:
            O(1) : Return statement for tuples.
        """
        material_name = RandomGen.random_choice(RANDOM_MATERIAL_NAMES)
        mining_rate = RandomGen.random_float() * RandomGen.randint(20,40)
        return cls(material_name,mining_rate)

if __name__ == "__main__":
    print(Material("Coal", 4.5))
    print(Material.random_material())


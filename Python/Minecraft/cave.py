from __future__ import annotations

from material import Material
from random_gen import RandomGen

# List of cave names from https://en.uesp.net/wiki/Skyrim:Caves. Thanks Skyrim.
CAVE_NAMES = [
    "Ashfall's Tear", # A hidden Tribunal Temple shrine to the Goddess Almalexia in a cave north of Raven Rock.
    "Benkongerike", # A medium-sized cave southeast of Saering's Watch and northwest of Headwaters of Harstrad containing bristlebacks and rieklings.
    "Blackbone Isle Grotto", # A small cave connected to the sea, situated on Blackbone Isle.
    "Bleakcoast Cave", # A small cave southeast of Winterhold and directly east of the Shrine of Azura occupied by frost trolls.
    "Blind Cliff Cave", # A medium-sized cave southwest of Karthwasten along the banks of the Karth River occupied by Forsworn.
    "Bloated Man's Grotto", # A small cave inhabited by spriggans and cave bears.
    "Bloodchill Cavern", # A vampiric player home in Winterhold, southeast of Snowpoint Beacon.
    "Bonechill Passage", # A small cave containing monsters, located east of Falkreath and to the southwest of Helgen.
    "Boulderfall Cave", # A small cave inhabited by leveled necromancers.
    "Brinewater Grotto", # A small cave on the coast between Solitude Lighthouse and Broken Oar Grotto.
    "Bristleback Cave", # A medium-sized cave due northwest of Broken Tusk Mine containing bristlebacks and rieklings.
    "Brittleshin Pass", # A small passage through the mountains between Whiterun Hold and Falkreath Hold.
    "Broken Fang Cave", # A small cave situated south of Swindler's Den (west of Whiterun).
    "Broken Helm Hollow", # A small cave in the southeast corner of The Rift occupied by bandits.
    "Broken Oar Grotto", # A large cave connected to the sea, located north of Solitude and northwest of Brinewater Grotto.
    "Bronze Water Cave", # A one-chamber cave west of Windhelm on the northern shore of Lake Yorgrim.
    "Brood Cavern", # A small cave high in the mountains southwest of Morthal.
    "Bruca's Leap Redoubt", # A small cave inhabited by Forsworn.
    "Castle Karstaag Caverns", # A medium-sized cave on the north coast of Solstheim containing bristlebacks and rieklings.
    "Castle Karstaag Ruins", # An icy clearing outside Castle Karstaag Caverns.
    "Chillwind Depths", # A medium-sized cave south of Dragon Bridge, on the border of Hjaalmarch and The Reach.
    "Clearspring Cave", # A small cave overlooking Eastmarch occupied by a troll.
    "Cold Rock Pass", # A small passage through a mountain northwest of Whiterun.
    "Coldcinder Cave", # A small cave with two entrances: one via a grate in the Bulwark Jail, and the other through a trap door atop the cliff just southeast of Raven Rock, near the top of the Bulwark.
    "Cragslane Cavern", # A small cave being used by bandits for skooma operations and animal blood sports.
    "Cragwallow Slope", # A medium-sized cave southeast of Windhelm home to conjurers and atronachs.
    "Cronvangr Cave", # A medium-sized cave southwest of Kynesgrove, inhabited by frostbite spiders and vampires.
    "Crystaldrift Cave", # A small cave that serves as the resting place for an insane Bosmer, with a shrine Kynareth built to watch over him and to bring peace to weary travelers.
    "Darkfall Cave", # A small cave just south-southwest of the Orc stronghold Mor Khazgur.
    "Darkfall Passage", # A small cave which is only accessible through Darkfall Cave, and is the only access to the Forgotten Vale.
    "Darkshade", # A small cave located just off of the base of the White River waterfall east of Valtheim Towers.
    "Darkwater Pass", # A medium-sized cave near Darkwater Crossing home to Falmer and chaurus.
    "Dimhollow Crypt", # A large cave southwest of Dawnstar where Serana is trapped.
    "Duskglow Crevice", # A small cave east of Fort Dunstad, occupied mainly by Falmer and chaurus.
    "Eldergleam Sanctuary", # An underground grove and worship site of the followers of Kynareth.
    "Fallowstone Cave", # A small cave with an exit to Giant's Grove, located in the Velothi Mountains northeast of Riften and a short distance north of Lost Prospect Mine.
    "Forebears' Holdout", # A small cave southeast of Dragon Bridge.
    "Forsaken Cave", # A medium-sized cave located west of Windhelm.
    "Frossel", # A small cave on a peninsula east of Haknir's Shoal and north of Skaal Village containing bristlebacks and rieklings.
    "Frostmoon Crag", # A small camp under a rock overhang south of Mount Moesring and northeast of the Abandoned Lodge inhabited by werewolves.
    "Frostroot Cave", # A cave in Eastmarch, north of Kagrenzel.
    "Glacial Cave", # A small cave north of Benkongerike, carved into the glacial cliff face along the northeastern coast, containing rieklings and horkers.
    "Glenmoril Coven", # A small cave far to the northwest of Falkreath inhabited by a group of unique hagravens, the Glenmoril Witches.
    "Gloomreach", # A medium-sized cave in the Reach containing chaurus and Falmer.
    "Graywinter Watch", # A one-chamber cave underneath the Ritual Stone (east of Whiterun) occupied by trolls.
    "Greywater Grotto", # A small cave far east of Falkreath, located south-southwest of Helgen, containing leveled predatory animals.
    "Gromm's Pass", # A small cave located in the Rift, south of Forelhost.
    "Haemar's Shame", # A medium-sized cave that is home to vampiric worshippers of Clavicus Vile.
    "Halldir's Cairn", # A small cave and tomb in the southernmost part of Skyrim that was built to house the remains of the fierce Halldir.
    "Hob's Fall Cave", # A small cave on the coast between Winterhold and Dawnstar inhabited by leveled warlocks and skeletons.
    "Honeystrand Cave", # A small cave occupied by bears.
    "Hrothmund's Barrow", # A small cave southwest of Benkongerike.
    "Iron Tusk Cave", # A small cave on the island of Giant's Tooth.
    "Liar's Retreat", # A small cave and connected underground cellar northwest of Broken Tower Redoubt and northeast of Karthwasten.
    "Lost Echo Cave", # A small cave near the northwestern coast of Haafingar occupied by Falmer.
    "Lost Knife Hideout", # A large cave that serves as the hideout for the Lost Knife bandits.
    "Mara's Eye Den", # A small cave found on the middle island of Mara's Eye Pond.
    "Moss Mother Cavern", # A small, open-roofed cavernous grove lush with many kinds of flora and fungi, located due north of Hunter's Rest and northwest of Half-Moon Mill.
    "Movarth's Lair", # A small cave north of Morthal inhabited by vampires.
    "Nightingale Hall", # The home of the Nightingales between Riften and the Shadow Stone.
    "Orotheim", # A small cave that is home to bandits intent on poaching mammoths.
    "Pinemoon Cave", # A small cave located to the northwest of Dragon Bridge and east of Volskygge.
    "Pinepeak Cavern", # A small cave along the Treva River occupied by bears.
    "Purewater Run", # A small cave south-southeast of Markarth containing slaughterfish.
    "Ravenscar Hollow", # A small cave inhabited by hagravens west of the Thalmor Embassy and due east of the Steed Stone.
    "Reachcliff Cave", # A small cave filled with draugr located northeast of Dushnikh Yal and southeast of Markarth.
    "Reachwater Rock", # A small cave east-southeast of Markarth and south of Sky Haven Temple, containing draugr.
    "Rebel's Cairn", # A small cave located in The Reach between the Sundered Towers and Bleakwind Bluff.
    "Red Eagle Redoubt", # A small cave and two exterior camps, one small and one sprawling, all occupied by Forsworn located east of Markarth.
    "Redoran's Retreat", # A small cave northwest of Whiterun occupied by bandits.
    "Rimerock Burrow", # A small cave located at the northwestern edge of Skyrim.
    "Runoff Caverns", # A large cave in the Reach, west of Lost Valley Redoubt.
    "Ruunvald Excavation", # A medium-sized cave east-southeast of Shor's Watchtower and north-northeast of Riften.
    "Septimus Signus's Outpost", # A small cave on a small remote icy island off the north coast of Skyrim, where Septimus Signus has made his home.
    "Shadowgreen Cavern", # A small cave northwest of Solitude, which is home to leveled spriggans and animals.
    "Shimmermist Cave", # A medium-sized cave northeast of Whiterun occupied by Falmer.
    "Sightless Pit", # A medium-sized cave in Winterhold occupied by Falmer.
    "Snapleg Cave", # A medium-sized cave carved into the side of a mountain.
    "Soljund's Sinkhole", # A medium-sized moonstone mine east of Sky Haven Temple with a smelter near the entrance.
    "Southfringe Sanctum", # A small cave occupied by the conjurer Bashnag and his coven.
    "Steepfall Burrow", # A small cave containing animals on the north coast of Haafingar.
    "Stillborn Cave", # A small cave north-northwest of Windhelm, on the other side of the mountains from the city.
    "Stony Creek Cave", # A small cave located in the southeastern corner of Eastmarch that is occupied by bandits.
    "Sunderstone Gorge", # A medium-sized cave west of Bloated Man's Grotto occupied by warlocks.
    "Swindler's Den", # A small cave between Whiterun and Rorikstead occupied by bandits.
    "Tolvald's Cave", # A large cave in the Velothi Mountains, northeast of Shor's Stone and south-southeast of Ansilvund.
    "Uttering Hills Cave", # A small cave in the mountains southwest of Windhelm occupied by bandits.
    "White River Watch", # A small cave east-northeast of Honningbrew Meadery and southwest of the Ritual Stone occupied by the White River bandits.
    "Wolfskull Cave", # A medium-sized cave west of Solitude filled with necromancers or bandits.
    "Yngvild", # A medium-sized cave on an island east-northeast of Dawnstar in the far northern reaches of Skyrim.
]

class Cave(Material):

    def __init__(self, name: str, material: Material, quantity: float=0) -> None:
        """
            PARAMETERS:
            Name of the cave, Material name, Quantity of the material
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
        self.cave_material = Material(material.name, material.mining_rate)
        self.material_name = self.cave_material.name
        self.material_mining_rate = self.cave_material.mining_rate
        self.name = name
        #self.cave_material = material # contains the material and its mining rate
        self.quantity = quantity
        #raise NotImplementedError()

    def add_quantity(self, amount: float) -> None:
        """
            PARAMETERS:
            Quantity of the material that you want to add.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            -   Sets the instance variable self.quantiy as the amount that we want.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [None]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST CASE:
            O(1) : Assignment for instance variables
        """
        self.quantity += amount
        #raise NotImplementedError()

    def remove_quantity(self, amount: float) -> None:
        """
            PARAMETERS:
            Quantity of the material that you want to remove.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            -   Removes a certain amount from the self.quantity instance variable. This will be used for removing
                materials after they have been mined.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [None]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST CASE:
            O(1) : Assignment for instance variables
        """
        self.quantity -= amount
        #raise NotImplementedError()

    def get_quantity(self) -> float:
        """
            PARAMETERS:
            [None]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            -   Returns the instance variable so that it may be appended or used in other sorts of ways.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            Returns the instance variable (quantity)
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST CASE:
            O(1) : Simple return statement
        """
        return self.quantity
        #raise NotImplementedError()

    def __str__(self) -> str:
        """
            PARAMETERS:
            [None]
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            -   Magic method to display the information of an object. Such as, name , quantity in inventory and
                the name of the material.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            Returns a string representation of the object.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST CASE:
            O(1) : Simple return statement
        """
        return "<Cave: {0}. {1} of {2}>".format(self.name,self.get_quantity(),str(self.cave_material))

        #<Cave: Castle Karstaag Ruins. 4 of [Netherite Ingot: 20.95🍗/💎]>,
        #raise NotImplementedError()

    @classmethod
    def random_cave(self, material_list: list[Material]) -> Cave:
        """
            PARAMETERS:
            A list of materials.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            -   The method will take a random cave name from the list of cave names, it will also take a 
                random material from the list in the parameter and then it will return a random combination.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            Returns cave_name, cave_material, material quantity.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST CASE:
            O(1) : Return statement for tuples.
        """
        cave_name = RandomGen.random_choice(CAVE_NAMES)
        cave_material = RandomGen.random_choice(material_list) # stll works as it is in list
        material_quantity = float(RandomGen.randint(2,12))
        return self(cave_name, cave_material, material_quantity)
        #raise NotImplementedError()

if __name__ == "__main__":
    print(Cave("Mt Coronet", Material("Coal", 4.5), 3))

    print(Cave.random_cave([Material("Coal", 4.5),Material("Coal", 5.5),Material("Coal", 6.5)]))


from .enemy import Goblin, Skeleton, DarkKnight


class Room:
    def __init__(self, name, description, exits, enemy=None, item=None, visited=False):
        self.name = name
        self.description = description
        self.exits = exits
        self.enemy = enemy
        self.item = item
        self.visited = visited

    def __str__(self):
        header = "========================="
        return f"{header}\n  {self.name.upper()}\n{header}\n{self.description}\nExits: {', '.join(self.exits.keys())}"

def build_world():
    village_gates_exits = {
        "north": "dark_forest_entrance",
        "south": "armor_smith",
    }

    dark_forest_entrance_exits = {
        "south": "village_gates",
        "east": "abandoned_cabin",
        "west": "ancient_ruins",
        "north": "cursed_grove"
    }

    cursed_grove_exits = {
        "south": "dark_forest_entrance"
    }

    abandoned_cabin_exits = {
        "west": "dark_forest_entrance"
    }

    ancient_ruins_exits = {
        "east": "dark_forest_entrance"
    }

    armor_smith_exits = {
        "north": "village_gates",
        "east": "tavern",
        "west": "weapon_smith"
    }

    tavern_exits = {
        "west": "armor_smith"
    }

    weapon_smith_exits = {
        "east": "armor_smith"
    }
    
    rooms = {
        "village_gates": Room("Village Gates", "You find yourself at the entrance of the village, a place of safety and commerce.", village_gates_exits),
        "dark_forest_entrance": Room("Dark Forest Entrance", "You walk towards the entrance to the Dark Forest, a place of danger and mystery.", dark_forest_entrance_exits, enemy=Goblin()),
        "armor_smith": Room("Armor Smith", "A humble blacksmith who specializes in crafting protective gear.", armor_smith_exits),
        "tavern": Room("Tavern", "A cozy establishment where travelers gather to rest and share stories.", tavern_exits),
        "weapon_smith": Room("Weapon Smith", "A skilled craftsman who creates powerful weapons for heroes.", weapon_smith_exits),
        "cursed_grove": Room("Cursed Grove", "A haunting place filled with ancient magic and malevolent spirits.", cursed_grove_exits, enemy=Skeleton()),
        "abandoned_cabin": Room("Abandoned Cabin", "A dilapidated structure that seems to be abandoned, but you can't shake the feeling of being watched.", abandoned_cabin_exits, enemy=Goblin()),
        "ancient_ruins": Room("Ancient Ruins", "Remnants of a long-lost civilization, shrouded in mystery and danger.", ancient_ruins_exits, enemy=DarkKnight())
    }

    return rooms
from enemy import Goblin


class Room:
    def __init__(self, name, description, exits, enemy=None, item=None, visited=False):
        self.name = name
        self.description = description
        self.exits = exits
        self.enemy = enemy
        self.item = item
        self.visited = visited

    def __str__(self):
        header = "==============================="
        return f"{header}\n{self.name.upper()}\n{header}\n{self.description}\nExits: {', '.join(self.exits.keys())}"

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
        "village_gates": Room("Village Gates", "The gates of the village, a place of safety and commerce.", village_gates_exits),
        "dark_forest_entrance": Room("Dark Forest Entrance", "The entrance to the Dark Forest, a place of danger and mystery.", dark_forest_entrance_exits, enemy=Goblin()),
        "armor_smith": Room("Armor Smith", "A humble blacksmith who specializes in crafting protective gear.", armor_smith_exits),
        "tavern": Room("Tavern", "A cozy establishment where travelers gather to rest and share stories.", tavern_exits),
        "weapon_smith": Room("Weapon Smith", "A skilled craftsman who creates powerful weapons for heroes.", weapon_smith_exits)
    }

    return rooms
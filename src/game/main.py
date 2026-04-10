from hero import Warrior, Mystic, Assassin
from enemy import Goblin, Skeleton, DarkKnight
from world import build_world
from combat import run_combat
from save import save_game, load_game

def choose_hero():
    name = input("What will your hero's name be?")
    hero_class = input("\nNext select your class.").lower().replace(" ", "")
    
    class_options = {
        "Option 1": "Mystic",
        "Option 2": "Warrior",
        "Option 3": "Assassin"
    }

    for option, hero_type in class_options:
        print(f" - {option}: {hero_type}")

    if hero_class == "option1" or hero_class == "1" or hero_class == "mystic":
        print(f"\nWelcome {name} the {hero_class}! Your adventure begins now...")
        return Mystic(name)
    elif hero_class == "option2" or hero_class == "2" or hero_class == "warrior":
        print(f"\nWelcome {name} the {hero_class}! Your adventure begins now...")
        return Warrior(name)
    elif hero_class == "option3" or hero_class == "3" or hero_class == "assassin":
        print(f"\nWelcome {name} the {hero_class}! Your adventure begins now...")
        return Assassin(name)
    else:
        print("Invalid class selected.")
        return choose_hero()
    
def explore(hero, rooms):
    for room in rooms:
        print(f"\nYou enter ")
    
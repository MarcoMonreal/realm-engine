from src.game.hero import Warrior, Mystic, Assassin
from src.game.enemy import Goblin, Skeleton, DarkKnight
from src.game.world import build_world
from src.game.combat import run_combat
from src.game.save import save_game, load_game

def choose_hero():
    name = input("\nWhat will your hero's name be?\n").strip()
    
    class_options = {
        "Option 1": "Mystic",
        "Option 2": "Warrior",
        "Option 3": "Assassin"
    }

    keep_looping = True

    while keep_looping == True:
        for option, hero_type in class_options.items():
            print(f"\n - {option}: {hero_type}")
            
        hero_class = input("\nSelect your class.\n").lower().strip()
        

        if hero_class == "option 1" or hero_class == "1" or hero_class == "mystic":
            print(f"\nWelcome {name} the Mystic! Your adventure begins now...")
            keep_looping = False
            return Mystic(name)
        elif hero_class == "option 2" or hero_class == "2" or hero_class == "warrior":
            print(f"\nWelcome {name} the Warrior! Your adventure begins now...")
            keep_looping = False
            return Warrior(name)
        elif hero_class == "option 3" or hero_class == "3" or hero_class == "assassin":
            print(f"\nWelcome {name} the Assassin! Your adventure begins now...")
            keep_looping = False
            return Assassin(name)
        else:
            print("Invalid class selected.")

def explore(hero, rooms, current_room_id="village_gates"):
    while True:
        current_room = rooms[current_room_id]
        print(current_room)

        # Check for enemy
        if current_room.enemy and current_room.enemy.is_alive():
            enemy = current_room.enemy
            print(f"\n{enemy}\nStarting combat...")
            run_combat(hero, current_room.enemy)
            if hero.is_alive():
                print(f"\nYou're currently at the {current_room.name}.\nExits: {', '.join(current_room.exits.keys())}")
            else:
                print("GAME OVER...")
                break

        action = input("\nWhat will you do?\n").lower().strip()

        if action in current_room.exits:
            current_room_id = current_room.exits[action]
        elif action == "save":
            save_game(hero, current_room_id)
            print("\nGame saved.")
        elif action == "quit":
            print("\nThanks for playing!")
            break
        else:
            print("\nInvalid action. Try a direction, 'save', or 'quit'.")

def main():
    print("=========================")
    print("  Welcome to Veilborn!")
    print("=========================")
    choice = input("Do you want to start a new adventure or load a saved game? (new/load)\n").lower().strip()

    rooms = build_world()
    current_room_id = "village_gates"
    keep_looping = True

    while keep_looping == True:
        if choice == "new":
            hero = choose_hero()
            keep_looping = False
        elif choice == "load":
            result = load_game()
            if result is not None:
                hero, current_room_id = result
                print(f"\nWelcome back, {hero.name} the {hero.hero_class}! Your adventure continues...")
                keep_looping = False
            else:
                print("No saved adventure found.")
        else:
            print("Invalid option.")
    
    explore(hero, rooms, current_room_id)

if __name__ == "__main__":
    main()
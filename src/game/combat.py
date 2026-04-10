import math
import random
from hero import Warrior, Mystic, Assassin
from enemy import Goblin, Skeleton, DarkKnight

def calculate_damage(attacker_attack, defender_defense):
    if attacker_attack > defender_defense:
        damage_after_defense = attacker_attack - defender_defense
        damage = random.randint(1, damage_after_defense)
    else:
        damage = 0

    return damage

def is_critical_hit(crit_chance):
    pass

def use_potion(hero):
    max_hp = hero.max_hp
    
    if hero.potions > 0:
        hero.hp += 30
        hero.potions -= 1

        # Ensure health doesn't exceed max HP
        if hero.hp > max_hp:
            hero.hp = max_hp

        return print(f"\nYou drink a potion and restore some health. \nYou have {hero.potions} potions left. \nYour current health is {hero.hp}.")
    else:
        return print("\nYou are out of potions!")

def hero_turn(hero, enemy):
    enemy_name = enemy.name

    options = {
        "Option 1": "Attack",
        "Option 2": "Drink a potion"
    }

    print("\nIt's your turn! What will you do?")
    print("================================")
    print("Choose an action:")
    for option, value in options.items():
        print(f"\n - {option}: {value}")

    option_selected = input("\nEnter your choice: \n").lower().replace(" ", "")

    if option_selected == "option1" or option_selected == "1":
        damage_dealt = calculate_damage(hero.attack, enemy.defense)
        enemy.take_damage(damage_dealt)
        print(f"\nYou attack the {enemy_name}, dealing {damage_dealt} damage!")
    elif option_selected == "option2" or option_selected == "2":
        use_potion(hero)
    else:
        print("Please select a valid option.")

    enemy_health = enemy.hp

    if enemy_health <= 0:
        return print(f"{enemy_name}'s health is 0.")
    else:
        #Only returning updated health for now
        return print(f"{enemy_name}'s health is {enemy_health}.")

def enemy_turn(hero, enemy):
    enemy_name = enemy.name
    print("\nThe enemy is taking their turn...")
    print("================================")

    enemy_options = {
        "1": "Basic attack",
        "2": "Skill"
    }

    enemy_choice = random.randint(1, len(enemy_options))
    
    if enemy_choice == 1:
        damage_dealt = calculate_damage(enemy.attack, hero.defense)
        hero.take_damage(damage_dealt)
        print(f"\nThe {enemy_name} attacks you, dealing {damage_dealt} damage!")
    elif enemy_choice == 2:
        #Simple caculation that I may update later
        skill_damage = math.ceil(calculate_damage(enemy.attack, hero.defense) * 1.5)
        hero.take_damage(skill_damage)
        print(f"\nThe {enemy_name} uses a powerful skill, dealing {skill_damage} damage!")

    hero_health = hero.hp

    return print(f"Your current health is {hero_health}.")

def run_combat(hero, enemy):
    enemy_name = enemy.name

    turn = 1

    while hero.is_alive() and enemy.is_alive():
        if (turn % 2) == 0:
            enemy_turn(hero, enemy)
        else:
            hero_turn(hero, enemy)
        
        turn += 1

    if hero.is_alive():
        return print(f"\nYou have slain the {enemy_name}!\n")
    else:
        return print("\nYou have DIED!\n")


if __name__ == "__main__":
    hero = Warrior("Aric")
    enemy = Goblin()

    print(hero)
    print(enemy)

    run_combat(hero, enemy)
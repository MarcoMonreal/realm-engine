import math
import random

def calculate_damage(attacker_attack, defender_defense):
    if attacker_attack > defender_defense:
        damage_after_defense = attacker_attack - defender_defense
        damage = random.randint(1, damage_after_defense)
    else:
        damage = 0

    return damage

def is_critical_hit(crit_chance):
    pass

def use_potion(hero_stats):
    max_hp = hero_stats.get("Max HP")
    
    if hero_stats.get("Potions") > 0:
        hero_stats["HP"] += 30
        hero_stats["Potions"] -= 1

        # Ensure health doesn't exceed max HP
        if hero_stats["HP"] > max_hp:
            hero_stats["HP"] = max_hp

        return print(f"\nYou drink a potion and restore some health. \nYou have {hero_stats.get("Potions")} potions left. \nYour current health is {hero_stats.get("HP")}.")
    else:
        return print("\nYou are out of potions!")

def hero_turn(hero_stats, enemy_stats):
    hero_attack = hero_stats.get("Attack")
    enemy_defense = enemy_stats.get("Defense")
    enemy = enemy_stats.get("Name")

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
        damage_dealt = calculate_damage(hero_attack, enemy_defense)
        enemy_stats["HP"] -= damage_dealt
        print(f"\nYou attack the {enemy}, dealing {damage_dealt} damage!")
    elif option_selected == "option2" or option_selected == "2":
        use_potion(hero_stats)
    else:
        print("Please select a valid option.")

    enemy_health = enemy_stats.get("HP")

    #Only returning updated health for now
    return print(f"{enemy}'s health is {enemy_health}.")

def enemy_turn(hero_stats, enemy_stats):
    enemy = enemy_stats.get("Name")

    print("\nThe enemy is taking their turn...")
    print("================================")

    enemy_options = {
        "1": "Basic attack",
        "2": "Skill"
    }

    enemy_choice = random.randint(1, len(enemy_options))
    
    if enemy_choice == 1:
        damage_dealt = calculate_damage(enemy_stats.get("Attack"), hero_stats.get("Defense"))
        hero_stats["HP"] -= damage_dealt
        print(f"\nThe {enemy} attacks you, dealing {damage_dealt} damage!")
    elif enemy_choice == 2:
        #Simple caculation that I may update later
        skill_damage = math.ceil(calculate_damage(enemy_stats.get("Attack"), hero_stats.get("Defense")) * 2)
        hero_stats["HP"] -= skill_damage
        print(f"\nThe {enemy} uses a powerful skill, dealing {skill_damage} damage!")

    hero_health = hero_stats.get("HP")

    return print(f"Your current health is {hero_health}.")

def run_combat(hero_stats, enemy_stats):
    enemy = enemy_stats.get("Name")
    print(f"A wild {enemy} appears!")

    turn = 1

    while hero_stats["HP"] > 0 and enemy_stats["HP"] > 0:
        if (turn % 2) == 0:
            enemy_turn(hero_stats, enemy_stats)
        else:
            hero_turn(hero_stats, enemy_stats)
        
        turn += 1

    if hero_stats["HP"] <= 0:
        return print("\nYou have DIED!")
    elif enemy_stats["HP"] <= 0:
        return print(f"\nYou have slain the {enemy}.")



if __name__ == "__main__":
    hero_stats = {
        "Name": "Aldric",
        "Attack": 20,
        "Defense": 8,
        "Max HP": 100,
        "HP": 100,
        "Potions": 3
    }

    enemy_stats = {
        "Name": "Goblin Scout",
        "Attack": 12,
        "Defense": 4,
        "HP": 30
    }

    run_combat(hero_stats, enemy_stats)
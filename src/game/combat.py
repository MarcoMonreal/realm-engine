import math
import random
from .hero import Warrior, Mystic, Assassin
from .enemy import Goblin, Skeleton, DarkKnight

def calculate_damage(attacker_attack, defender_defense, crit_chance = 0):
    if attacker_attack > defender_defense:
        damage_after_defense = attacker_attack - defender_defense
        damage_before_crit = math.ceil(random.uniform(1, damage_after_defense))

        if is_critical_hit(crit_chance):
            damage = damage_before_crit * 2
            print("\nYou land a VICIOUS blow!")
        else:
            damage = damage_before_crit
    else:
        damage = 0

    return damage

def is_critical_hit(crit_chance):
    return random.random() <= crit_chance

def use_potion(hero):
    max_hp = hero.max_hp
    
    if hero.potions > 0:
        hero.hp += 30
        hero.potions -= 1

        # Ensure health doesn't exceed max HP
        if hero.hp > max_hp:
            hero.hp = max_hp

        if hero.potions == 1:
            return f"\nYou drink a potion and restore some health. \nYou have {hero.potions} potion left. \nYour current health is {hero.hp}."
        else:
            return f"\nYou drink a potion and restore some health. \nYou have {hero.potions} potions left. \nYour current health is {hero.hp}."
    else:
        return "\nYou are out of potions!"

def hero_turn(hero, enemy):
    enemy_name = enemy.name

    if hero.skill_cooldown != 0:
        options = {
            "Option 1": "Attack",
            "Option 2": f"Skill has a {hero.skill_cooldown} turn cooldown",
            "Option 3": "Drink a potion"
        }
    else:
        options = {
            "Option 1": "Attack",
            "Option 2": "Use skill",
            "Option 3": "Drink a potion"
        }

    print("\nIt's your turn! What will you do?")
    print("==========================")
    print("Choose an action:")
    for option, value in options.items():
        print(f"\n - {option}: {value}")

    option_selected = input("\nEnter your choice: \n").lower().replace(" ", "")

    if option_selected == "option1" or option_selected == "1":
        damage_dealt = calculate_damage(hero.attack, enemy.defense, hero.crit_chance)
        enemy.take_damage(damage_dealt)
        print(f"\nYou attack the {enemy_name}, dealing {damage_dealt} damage!")
    elif option_selected == "option2" or option_selected == "2":
        if hero.skill_cooldown != 0:
            print(f"\nYou cannot use your skill yet, {hero.name}!\nYour skill's cooldown is currently {hero.skill_cooldown} turns.")
            return hero_turn(hero, enemy)
        else:
            if hero.hero_class == "Warrior":
                if hero.skill_cooldown != 0:
                    print(f"\nYou cannot use your skill yet, {hero.name}!\nCleave's cooldown is currently {hero.skill_cooldown} turns.")
                else:
                    # Two separate attacks that each calculate damage and crits independently
                    first_hit = calculate_damage(hero.cleave(), enemy.defense, hero.crit_chance)
                    second_hit = calculate_damage(hero.cleave(), enemy.defense, hero.crit_chance)
                    damage_dealt = first_hit + second_hit
                    enemy.take_damage(damage_dealt)
                    hero.skill_cooldown = 6
                    print(f"\nYou Cleave the {enemy_name}, dealing {damage_dealt} damage!")
                    print(f"Cleave's first strike dealt {first_hit} damage and the second strike dealt {second_hit} damage! \nCleave's cooldown is now {hero.skill_cooldown} turns.")
            elif hero.hero_class == "Mystic":
                if hero.skill_cooldown != 0:
                    print(f"\nYou cannot use your skill yet, {hero.name}!\nEntomb's cooldown is currently {hero.skill_cooldown} turns.")
                else:
                    entomb_damage = hero.attack * 1.5
                    damage_dealt = calculate_damage(entomb_damage, enemy.defense, hero.crit_chance)
                    enemy.take_damage(damage_dealt)
                    hero.skill_cooldown = 6

                    if hero.entomb():
                        enemy.stun_counter = 1
                        print(f"\nYou cast Entomb on the {enemy_name}, dealing {damage_dealt} damage and stunning it for 1 turn!")
                        print(f"Entomb's cooldown is now {hero.skill_cooldown} turns.")
                    else:
                        print(f"\nYou cast Entomb on the {enemy_name}, dealing {damage_dealt} damage!")
                        print(f"Entomb's cooldown is now {hero.skill_cooldown} turns.")
            elif hero.hero_class == "Assassin":
                if hero.skill_cooldown != 0:
                    print(f"\nYou cannot use your skill yet, {hero.name}!\nKidney Strike's cooldown is currently {hero.skill_cooldown} turns.")
                else:
                    increased_attack = hero.attack * 1.75
                    damage_dealt = calculate_damage(increased_attack, enemy.defense, hero.kidney_strike())
                    enemy.take_damage(damage_dealt)
                    hero.skill_cooldown = 6
                    print(f"\nYou use Kidney Strike on the {enemy_name}, dealing {damage_dealt} damage!")
                    print(f"Kidney Strike's cooldown is now {hero.skill_cooldown} turns.")
    elif option_selected == "option3" or option_selected == "3":
        print(use_potion(hero))
    else:
        print("Please select a valid option.")
        hero_turn(hero, enemy)

    enemy_health = enemy.hp

    if enemy_health <= 0:
        return print(f"{enemy_name}'s health is 0.")
    else:
        #Only returning updated health for now
        return print(f"{enemy_name}'s health is {enemy_health}.")

def enemy_turn(hero, enemy):
    enemy_name = enemy.name

    if enemy.is_stunned():
        print(f"\nThe {enemy_name} is stunned and cannot move this turn!")
        enemy.stun_counter -= 1
        return
    
    print("\nThe enemy is taking their turn...")
    print("=========================")

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

    if hero_health <= 0:
        return print(f"Your current health is 0.")
    else:
        return print(f"Your current health is {hero_health}.")

def run_combat(hero, enemy):
    enemy_name = enemy.name

    turn = 1

    while hero.is_alive() and enemy.is_alive():
        if (turn % 2) == 0:
            enemy_turn(hero, enemy)
        else:
            hero_turn(hero, enemy)

        if hero.skill_cooldown > 0:
            hero.skill_cooldown -= 1
        
        turn += 1

    if hero.is_alive():
        return print(f"\nYou have slain the {enemy_name}!\n")
    else:
        return print("\nYou have DIED!\n")
    


if __name__ == "__main__":
    hero = Mystic("Aric")
    enemy = Goblin()

    print(hero)
    print(enemy)

    run_combat(hero, enemy)
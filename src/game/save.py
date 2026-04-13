import json
from .hero import Warrior, Mystic, Assassin
import os
os.makedirs("data", exist_ok=True)

SAVE_FILE = "data/save.json"

def save_game(hero, current_room_id):
    save_data = {
        "hero": {
            "name": hero.name,
            "hp": hero.hp,
            "max_hp": hero.max_hp,
            "attack": hero.attack,
            "defense": hero.defense,
            "potions": hero.potions,
            "gold": hero.gold,
            "experience": hero.experience,
            "level": hero.level,
            "hero_class": hero.hero_class
        },
        "current_room_id": current_room_id
    }
    with open(SAVE_FILE, 'w') as f:
        json.dump(save_data, f)

def load_game():
    try:
        with open(SAVE_FILE, 'r') as f:
            save_data = json.load(f)
            hero_data = save_data["hero"]

            class_map = {
                "Warrior": Warrior,
                "Mystic": Mystic,
                "Assassin": Assassin
            }

            hero = class_map[hero_data["hero_class"]](hero_data["name"])
            hero.hp = hero_data["hp"]
            hero.max_hp = hero_data["max_hp"]
            hero.attack = hero_data["attack"]
            hero.defense = hero_data["defense"]
            hero.potions = hero_data["potions"]
            hero.gold = hero_data["gold"]
            hero.experience = hero_data["experience"]
            hero.level = hero_data["level"]

            return hero, save_data["current_room_id"]
    except FileNotFoundError:
        return None
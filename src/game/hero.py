import random

class Hero:
    def __init__(self, name, hero_class, attack, crit_chance, defense, hp, max_hp, skill_cooldown, potions, gold, experience, level, stun_counter=0):
        self.name = name
        self.hero_class = hero_class
        self.attack = attack
        self.crit_chance = crit_chance
        self.defense = defense
        self.stun_counter = stun_counter
        self.hp = hp
        self.max_hp = max_hp
        self.skill_cooldown = skill_cooldown
        self.potions = potions
        self.gold = gold
        self.experience = experience
        self.level = level
 
    def take_damage(self, amount):
        self.hp = self.hp - amount
        return f"\nYou took {amount} damage. \nYou have {self.hp} health left."

    def heal(self, amount):
        if self.potions > 0:
            self.hp = self.hp + amount
            self.potions -= 1

            if self.hp > self.max_hp:
                self.hp = self.max_hp

            return f"\nYou take a potion and heal for {amount} health.\nYou currently have {self.hp} HP. \nYou have {self.potions} left."
        else:
            return "\nYou have run out of potions!"

    def is_alive(self):
        return self.hp > 0
    
    def is_stunned(self):
        return self.stun_counter > 0

    def __str__(self):
        return f"Hail {self.name} the level {self.level} {self.hero_class}! \nYou have {self.hp} health and {self.gold} gold in your pocket."

class Warrior(Hero):
    def __init__(self, name):
        # High HP and defense, low attack
        super().__init__(name, "Warrior", attack=5, crit_chance=0.1, defense=10, hp=30, max_hp=30, skill_cooldown=0, potions=1, gold=0, experience=0, level=1)
        
    def cleave(self):
        # A powerful attack that hits an enemy twice, 
        # but has a cooldown of 6 turns
        double_strike = self.attack * 2
        return double_strike

class Mystic(Hero):
    def __init__(self, name):
        # Low HP, high attack
        super().__init__(name, "Mystic", attack=15, crit_chance=0.2, defense=5, hp=20, max_hp=20, skill_cooldown=0, potions=3, gold=5, experience=0, level=1)

    def entomb(self):
        # A powerful attack that has a chance to stun the enemy for 1 turn,
        # but has a cooldown of 6 turns
        stun_chance = 0.3
        return random.random() <= stun_chance

class Assassin(Hero):
    def __init__(self, name):
        # Balanced class, high crit chance
        super().__init__(name, "Assassin", attack=10, crit_chance=0.3, defense=7, hp=25, max_hp=25, skill_cooldown=0, potions=2, gold=10, experience=0, level=1)
        
    def kidney_strike(self):
        # A powerful attack that has a high chance to crit,
        # but has a cooldown of 6 turns
        crit_chance = self.crit_chance + 0.2
        return crit_chance

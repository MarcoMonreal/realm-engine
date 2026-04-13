class Enemy:
    def __init__(self, name, hp, attack, defense, stun_counter=0):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.stun_counter = stun_counter

    def take_damage(self, amount):
        self.hp = self.hp - amount
        return f"{self.name} took {amount} damage. It has {self.hp} health."   

    def is_alive(self):
        return self.hp > 0
    
    def is_stunned(self):
        return self.stun_counter > 0

    def __str__(self):
        return f"\nA wild {self.name} appears! \n{self.name} - HP: {self.hp}, Attack: {self.attack}, Defense: {self.defense}"

class Goblin(Enemy):
    def __init__(self):
        super().__init__("Goblin", 20, 12, 2)

class Skeleton(Enemy):
    def __init__(self):
        super().__init__("Skeleton", 50, 16, 6)

class DarkKnight(Enemy):
    def __init__(self):
        # Boss-tier enemy
        super().__init__("Dark Knight", 250, 52, 78)
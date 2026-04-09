class Enemy:
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        pass

    def take_damage(self, amount):
        pass   

    def is_alive(self):
        pass

    def __str__(self):
        pass

class Goblin(Enemy):
    def __init__(self):
        pass

class Skeleton(Enemy):
    def __init__(self):
        pass

class DarkKnight(Enemy):
    def __init__(self):
        # Boss-tier enemy
        pass
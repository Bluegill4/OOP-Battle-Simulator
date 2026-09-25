import random

class Hero:
    """The hero blueprint will be implemented later in the project."""
    def __init__ (self, name):
        self.name = name
        self.health = random.randint(100,150)
        self.attack_power = random.randint(15,25)
        self.battleline = "In the Name of Excell!"
        self.magic = random.randint(1,15)
    def attack(self):
        return random.randint(1,self.attack_power)
    def take_damage(self, damage):
        self.health = max(0, self.health - damage)
    def sad(self):
        self.magic = -5
    def is_alive(self):
        return self.health > 0
    def battle_cry(self):
        return self.battleline  
    def fire_bomb(self):
        return random.randint(1, 25)
    def heal(self):
        self.health = int(self.health + (self.magic / 2))
    pass


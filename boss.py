import random
from enemy import Enemy

class Dragon(Enemy):
    """A completed character class students can examine as an OOP example."""

    def __init__(self, name):
        super().__init__(name, health = 100, attackPower = 11)
        self.gold = 0

    def attack(self):
        """Goblins steal hero gold"""
        return random.randint(10, self.attack_power)
        print("no more Excell for you")


from goblin import Goblin
from boss import Dragon
from hero import Hero

hero = Hero("Dr Brown")
enemies = [
    Goblin("Gribble"),
    Dragon("The Goblin King"),
]

for enemy in enemies:
    print(f"\n{enemy.name} enters with {enemy.health} health.")

    damage = enemy.attack()
    print(f"{enemy.name} attacks for {damage} damage!")

    enemy.take_damage(20)
    print(f"Still alive: {enemy.is_alive()}")
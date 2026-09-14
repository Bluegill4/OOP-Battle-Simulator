from goblin import Goblin
from hero import Hero

ARENA_NAME = "The Iron Square"


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("Gribble Gobble")
    goblin1 = Goblin("Gobble Gribble")
    hero = Hero("Dr Brown")
    print(f"{goblin.name} enters the arena with {goblin.health} health.")
    print(f"{goblin1.name} enters the arena with {goblin1.health} health.")

    print("But no hero has answered the call... yet.")
    print(f"{hero.name} enter the arena with {hero.health} health.")
    print(f"{hero.name} surprises {goblin1.name} with an attack!")
    theAttack = hero.attack()
    print(f"It does "+ str(theAttack)+" damage!")
    goblin1.take_damage(theAttack)
    theAttack = goblin1.attack()
    print(f"{goblin.name} attacks {hero.name}")
    print(f"It does "+ str(theAttack)+" damage!")
    hero.take_damage(theAttack)





if __name__ == "__main__":
    main()

from goblin import Goblin
from hero import Hero
import random
import time

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
    time.sleep(1)
    print(f"{hero.name} enter the arena with {hero.health} health and {hero.magic} magic.")
    time.sleep(1)
    print(f"{hero.battle_cry()}")
    time.sleep(1)
    print(f"{hero.name} surprises {goblin1.name} with an attack!")
    time.sleep(1)
    theAttack = hero.attack()
    print(f"It does "+ str(theAttack)+" damage!")
    time.sleep(1)
    goblin1.take_damage(theAttack)
    theAttack = goblin1.attack()
    print(f"{goblin.name} attacks {hero.name}")
    time.sleep(1)
    print(f"It does "+ str(theAttack)+" damage!")
    time.sleep(1)
    hero.take_damage(theAttack)
    def battleRound():
        while (goblin.is_alive() and goblin1.is_alive()) or (hero.is_alive()):
            Action = input("What is you next action? (B, Battle Cry; A, Basic Attack; H, Heal;)")
            if Action == "B":
                print(f"{hero.battle_cry()}")
                time.sleep(1)
            elif Action == "H":
                hero.heal()
                print(f"{hero.name} heals with his magic, His new health is {hero.health}")
                time.sleep(1)
            elif Action == "A":
                Goblin_choice = random.randint(1,2)
                if Goblin_choice == 1:
                    theAttack = goblin1.attack()
                    print(f"{hero.name} Attacks {goblin1.name}, It does "+ str(theAttack)+" damage!")
                    time.sleep(1)
                    print(f"{goblin1.name} Health is now {goblin1.health}")
                if Goblin_choice == 2:
                    theAttack = goblin.attack()
                    print(f"{hero.name} Attacks {goblin1.name}, It does "+ str(theAttack)+" damage!")
                    time.sleep(1)
                    print(f"{goblin.name} Health is now {goblin.health}")
            theAttack = goblin.attack()
            hero.take_damage(theAttack)
            print(f"{goblin.name} attacks {hero.name}")
            time.sleep(1)
            print(f"It does "+ str(theAttack)+ f" damage! {hero.name} Health is now {hero.health}")
            time.sleep(1)
            theAttack = goblin1.attack()
            hero.take_damage(theAttack)
            print(f"{goblin1.name} attacks {hero.name}")
            time.sleep(1)
            print(f"It does "+ str(theAttack)+ f" damage! {hero.name} Health is now {hero.health}")  
            time.sleep(1) 
            if (goblin.is_alive() and goblin1.is_alive()) == False:
                print("You won!")
            if (hero.is_alive()) == False:
                print("You lost!")

    battleRound()




if __name__ == "__main__":
    main()

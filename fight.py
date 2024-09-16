from Character import Shockmaster, shockmaster
from fight_system import Wrestler
import random

def fight(shockmaster, opponent):
    print(f"\n{shockmaster.name} vs {opponent.name}! Let the battle begin!")
    
    while shockmaster.health > 0 and opponent.health > 0:
        print(f"\n{shockmaster.name}'s Health: {shockmaster.health}/{shockmaster.max_health}, Stamina: {shockmaster.stamina}/{shockmaster.max_stamina}")
        print(f"{opponent.name}'s Health: {opponent.health}, Stamina: {opponent.stamina if hasattr(opponent, 'stamina') else 'N/A'}")
        
        choice = input("\nChoose your action:\n[1] Normal Attack\n[2] Use Special Move\n[3] Taunt the Opponent\nWhat will you do? ").strip()

        if choice == '1':
            normal_attack(shockmaster, opponent)
        elif choice == '2':
            use_special_move(shockmaster, opponent)
        elif choice == '3':
            taunt_opponent(shockmaster, opponent)
        else:
            print("Invalid choice. You missed your chance to act!")

        if opponent.health <= 0:
            print(f"\n{opponent.name} has been defeated! {shockmaster.name} wins the match!")
            break

        opponent_turn(shockmaster, opponent)

        if shockmaster.health <= 0:
            print(f"\n{shockmaster.name} has been defeated by {opponent.name}!")
            break

def normal_attack(attacker, defender):
    damage = random.randint(5, 15)
    defender.health -= damage
    print(f"\n{attacker.name} attacks {defender.name} with a normal attack, dealing {damage} damage!")

def use_special_move(shockmaster, opponent):
    if shockmaster.skills:
        print("\nChoose a special move:")
        for idx, skill in enumerate(shockmaster.skills, 1):
            print(f"[{idx}] {skill}")
        choice = input("Choose your special move: ").strip()

        try:
            skill_choice = shockmaster.skills[int(choice) - 1]
            shockmaster.use_skill(skill_choice, opponent)
        except (IndexError, ValueError):
            print("Invalid choice. You missed your chance to use a special move!")
    else:
        print(f"\n{shockmaster.name} doesn't know any special moves yet!")

def taunt_opponent(shockmaster, opponent):
    success = random.random() < 0.5
    if success:
        print(f"\n{shockmaster.name} taunts {opponent.name}, making them furious! {shockmaster.name} gains 3 fame points.")
        shockmaster.fame_points += 3
    else:
        print(f"\n{shockmaster.name}'s taunt fails! {opponent.name} isn't impressed.")

def opponent_turn(shockmaster, opponent):
    action = random.choice(["attack", "taunt"])
    
    if action == "attack":
        normal_attack(opponent, shockmaster)
    elif action == "taunt":
        print(f"\n{opponent.name} taunts {shockmaster.name}, but {shockmaster.name} doesn't care.")

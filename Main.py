from Character import Shockmaster
from Opponents import jobbers, tv_title_contenders, us_title_contenders, main_eventers
from menu import Menu
import random
import time
import threading
import pygame
from fight import fight, Shockmaster, normal_attack, use_special_move, taunt_opponent, opponent_turn
from feed import feed_shockmaster
from rasslin_time import rasslin_time
from talk_backstage import talk_backstage

shockmaster = Shockmaster()
opponents = []

main_menu_options = [
    "The saga of The Shockmaster",
    "Train Shockmaster",
    "Feed Shockmaster",
    "Upgrade Skills",
    "Talk to other wrestlers backstage",
    "'Rasslin Time!!",
    "Quit"
]

train_menu_options = [
    "Exercise",
    "Exercise? Yeah, right.",
]

exercise_options = [
    "Lazy Jog",
    "Chair Yoga",
    "Pizza Plank",
    "Lift the Fridge",
    "Jazzercise!",
    "Commercial Break Push-Ups"
]

not_exercise_options = [
    "Dodge... Responsibilities",
    "Microwave Mega Mastery",
    "Remote Control Reach",
    "Social Media Super Scroll",
    "12oz Curls",
    "Post-Workout Nap (Without the Workout)"
]

feed_shockmaster_options = [
    "Mystery Meat",
    "Expired Yogurt",
    "Chocolate Covered Bacon Strips",
    "Tofu-turducken",
    "Purple Stuff"
]

other_wrestlers_menu = [
    "2 Cold Scorpio",
    "Brian Pillman",
    "Jim Ross",
    "'Stunning' Steve Austin",
    "Big Van Vader"
]

opponent_level_options = [
    "Jobber",
    "TV Title Contender",
    "US Title Contender",
    "Main Eventer",
    "Go Back"
]

def print_menu_error():
    print("Not a valid choice! Shameful!! Try again!")

def main():
    running = True
    main_menu = Menu(main_menu_options)

    while running:
        print("\n=== Main Menu ===")
        choice = main_menu.get_choice()

        if choice == 1:
            show_saga()
        elif choice == 2:
            train_shockmaster()
        elif choice == 3:
            feed_shockmaster()
        elif choice == 4:
            upgrade_skills()
        elif choice == 5:
            talk_backstage()
        elif choice == 6:
            rasslin_time(shockmaster)  # Pass shockmaster to rasslin_time()
        elif choice == 7:
            print("Thanks for playing!")
            running = False
        else:
            print_menu_error()

def show_saga():
    def play_music():
        try:
            pygame.mixer.init()
            pygame.mixer.music.load('sad_violin.mp3')
            pygame.mixer.music.play()
        except Exception as e:
            print("Couldn't play music:", e)
    
    music_thread = threading.Thread(target=play_music)
    music_thread.start()

    print("\nThe Saga of The Shockmaster\n")
    time.sleep(4)
    print("Once upon a time, in the world of professional wrestling...")
    time.sleep(4)
    print("A new hero was set to make an earth-shattering debut.")
    time.sleep(4)
    print("Clad in a sparkling stormtrooper helmet and a fur-lined vest...")
    time.sleep(4)
    print("He was The Shockmaster!")
    time.sleep(4)
    print("\nBut fate had other plans.")
    time.sleep(4)
    print("As he burst through the wall...")
    time.sleep(4)
    print("He tripped over a misplaced board...")
    time.sleep(4)
    print("And fell flat on his face, helmet rolling away.")
    time.sleep(4)
    print("\nSilence fell over the arena.")
    time.sleep(4)
    print("Snickers could be heard from his fellow wrestlers.")
    time.sleep(4)
    print("The moment was... shocking, but not in the way anyone expected.")
    time.sleep(4)
    print("\nDetermined to overcome this mishap,")
    time.sleep(4)
    print("The Shockmaster embarks on a journey of redemption,")
    time.sleep(4)
    print("To prove that he can rise to the top and win the World Championship!!")
    time.sleep(5)

    pygame.mixer.music.fadeout(2000)
    print("\nThe journey of the Shockmaster begins now...")
    time.sleep(5)

def train_shockmaster():
    print("\n=== Training Menu ===")
    train_menu = Menu(train_menu_options)
    choice = train_menu.get_choice()

    if choice == 1:
        exercise()
    elif choice == 2:
        not_exercise()
    else:
        print_menu_error()



def exercise():
    print("\nChoose an exercise:")
    exercise_menu = Menu(exercise_options)
    choice = exercise_menu.get_choice()
    activity = exercise_options[choice - 1]
    shockmaster.train(activity)

def not_exercise():
    print("\nChoose a non-exercise activity:")
    not_exercise_menu = Menu(not_exercise_options)
    choice = not_exercise_menu.get_choice()
    activity = not_exercise_options[choice - 1]
    shockmaster.train(activity)

def print_menu_error():
    print("Not a valid choice! Shameful!! Try again!")

def feed_shockmaster():
    print("\n=== Feeding Options ===")
    feed_menu = Menu(feed_shockmaster_options)
    choice = feed_menu.get_choice()
    food = feed_shockmaster_options[choice - 1]
    
    if food == "Mystery Meat":
        health_increase = random.choice([-10, 5, 15])
        stamina_increase = random.choice([0, 5, 10])
        shockmaster.feed(food, health_increase, stamina_increase, message="You feel... odd.")
    elif food == "Expired Yogurt":
        shockmaster.feed(food, health_increase=-10, stamina_increase=0, message="Why did you eat that? You feel sick!")
    elif food == "Chocolate Covered Bacon Strips":
        shockmaster.feed(food, health_increase=20, stamina_increase=10, message="Delicious and energizing!")
    elif food == "Tofu-turducken":
        shockmaster.feed(food, health_increase=10, stamina_increase=15, message="Surprisingly satisfying.")
    elif food == "Purple Stuff":
        shockmaster.feed(food, health_increase=-5, stamina_increase=5, message="Is that even safe to drink?")
    else:
        print("Unknown food item.")

def upgrade_skills():
    print("\n=== Upgrade Skills ===")
    print("You have", shockmaster.fame_points, "fame points.")
    
    skill_menu_options = [
        "[1] Learn 'Thunderous Slam' (Cost: 20 fame points)",
        "[2] Learn 'Helmet Headbutt' (Cost: 15 fame points)",
        "[3] Increase Max Health by 20 (Cost: 15 fame points)",
        "[4] Increase Power by 5 (Cost: 10 fame points)",
        "[5] Increase Stamina by 10 (Cost: 10 fame points)",
        "[6] Unlock 'Showboating' - Gain extra fame points after each match (Cost: 25 fame points)"
    ]
    
    for option in skill_menu_options:
        print(option)
    
    choice = input("\nChoose an upgrade: ").strip()

    if choice == '1':
        if shockmaster.fame_points >= 20 and "Thunderous Slam" not in shockmaster.skills:
            shockmaster.skills.append("Thunderous Slam")
            shockmaster.fame_points -= 20
            print("You have learned 'Thunderous Slam'!")
        else:
            print("You either don't have enough fame points or already know this skill.")
    
    elif choice == '2':
        if shockmaster.fame_points >= 15 and "Helmet Headbutt" not in shockmaster.skills:
            shockmaster.skills.append("Helmet Headbutt")
            shockmaster.fame_points -= 15
            print("You have learned 'Helmet Headbutt'!")
        else:
            print("You either don't have enough fame points or already know this skill.")
    
    elif choice == '3':
        if shockmaster.fame_points >= 15:
            shockmaster.max_health += 20
            shockmaster.fame_points -= 15
            print(f"Max health increased! Your new max health is {shockmaster.max_health}.")
        else:
            print("Not enough fame points.")
    
    elif choice == '4':
        if shockmaster.fame_points >= 10:
            shockmaster.power += 5
            shockmaster.fame_points -= 10
            print(f"Power increased! Your new power is {shockmaster.power}.")
        else:
            print("Not enough fame points.")
    
    elif choice == '5':
        if shockmaster.fame_points >= 10:
            shockmaster.max_stamina += 10
            shockmaster.fame_points -= 10
            print(f"Stamina increased! Your new max stamina is {shockmaster.max_stamina}.")
        else:
            print("Not enough fame points.")
    
    elif choice == '6':
        if shockmaster.fame_points >= 25 and "Showboating" not in shockmaster.skills:
            shockmaster.skills.append("Showboating")
            shockmaster.fame_points -= 25
            print("You have unlocked 'Showboating'! You will gain extra fame points after every match.")
        else:
            print("You either don't have enough fame points or already unlocked this ability.")
    
    else:
        print("Invalid choice.")
    check_skill_combinations()

def check_skill_combinations():
    if "Shockmaster Slam" in shockmaster.skills and "Rolling Helmet Headbutt" in shockmaster.skills:
        if "Shocking Combo" not in shockmaster.skills:
            shockmaster.skills.append("Shocking Combo")
            print("\nCongratulations! You have unlocked the secret skill 'Shocking Combo' by mastering Shockmaster Slam and Rolling Helmet Headbutt!")

def talk_backstage():
    print("\n=== Backstage ===")
    wrestlers_menu = Menu(other_wrestlers_menu)
    choice = wrestlers_menu.get_choice()
    wrestler = other_wrestlers_menu[choice - 1]
    print(f"You have a conversation with {wrestler}.")
    shockmaster.talk(wrestler)

def rasslin_time():
    print("\nChoose the level of opponent you want to face:")
    level_menu = Menu(opponent_level_options)
    choice = level_menu.get_choice()

def select_random_opponent(opponent_list):
    """Select a random opponent from the given list of opponents."""
    if opponent_list:
        return random.choice(opponent_list)
    else:
        return None  # Return None if the opponent list is empty

def rasslin_time(shockmaster):
    print("\nChoose the level of opponent you want to face:")
    opponent_level_options = [
        "Jobber",
        "TV Title Contender",
        "US Title Contender",
        "Main Eventer",
        "Go Back"
    ]
    level_menu = Menu(opponent_level_options)
    choice = level_menu.get_choice()

    # Use select_random_opponent based on player choice
    if choice == 1:
        opponent = select_random_opponent(jobbers)  # This function is now properly defined
    elif choice == 2:
        opponent = select_random_opponent(tv_title_contenders)
    elif choice == 3:
        opponent = select_random_opponent(us_title_contenders)
    elif choice == 4:
        opponent = select_random_opponent(main_eventers)
    elif choice == 5:
        return  # Go back to the main menu
    else:
        print("Invalid choice!")
        return

    # Proceed to fight if an opponent is found
    if opponent:
        print(f"\n{shockmaster.name} is wrestling against {opponent.name}!")
        fight(shockmaster, opponent)  # Assuming fight is defined elsewhere
        if opponent.health <= 0:
            shockmaster.fame_points += opponent.fame_reward
            print(f"Earned {opponent.fame_reward} fame points! Total fame: {shockmaster.fame_points}")
            shockmaster.matches_won += 1

            # Reset health and stamina after the match
            shockmaster.health = shockmaster.max_health
            shockmaster.stamina = shockmaster.max_stamina

        else:
            print(f"{opponent.name} defeated {shockmaster.name}!")
    else:
        print("No more opponents available in this category.")
if __name__ == "__main__":
    main()
import random
from Opponents import jobbers, tv_title_contenders, us_title_contenders, main_eventers
from menu import Menu
from fight import fight

def select_random_opponent(opponent_list, shockmaster=None):
    """Select a random opponent from the given list of opponents."""
    if opponent_list:
        if opponent_list == main_eventers and shockmaster:
            # Exclude defeated main eventers
            available_opponents = [op for op in opponent_list if op.name.lower() not in [name.lower() for name in shockmaster.defeated_main_eventers]]
            if available_opponents:
                return random.choice(available_opponents)
            else:
                print("You have defeated all main eventers!")
                return None
        else:
            return random.choice(opponent_list)
    else:
        return None  # Return None if the opponent list is empty

def declare_world_champion(shockmaster):
    print("\n**************************************************")
    print(f"Congratulations, {shockmaster.name}!")
    print("You have defeated all the main eventers and won the World Championship!")
    print("Your journey from a botched debut to the top of the wrestling world is complete!")
    print("**************************************************")
    print("Thank you for playing!")
    exit()  # Ends the program

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
        opponent = select_random_opponent(jobbers)
    elif choice == 2:
        opponent = select_random_opponent(tv_title_contenders)
    elif choice == 3:
        opponent = select_random_opponent(us_title_contenders)
    elif choice == 4:
        opponent = select_random_opponent(main_eventers, shockmaster)
    elif choice == 5:
        return  # Go back to the main menu
    else:
        print("Invalid choice!")
        return

    # Proceed to fight if an opponent is found
    if opponent:
        print(f"\n{shockmaster.name} is wrestling against {opponent.name}!")
        fight(shockmaster, opponent)
        if opponent.health <= 0:
            shockmaster.fame_points += opponent.fame_reward
            print(f"Earned {opponent.fame_reward} fame points! Total fame: {shockmaster.fame_points}")
            shockmaster.matches_won += 1

            # Check if the opponent is a main eventer
            opponent_name = opponent.name.lower()
            main_eventer_names = [me.name.lower() for me in main_eventers]

            if opponent_name in main_eventer_names:
                if opponent_name not in [name.lower() for name in shockmaster.defeated_main_eventers]:
                    shockmaster.defeated_main_eventers.append(opponent.name)
                    print(f"You have defeated a main eventer: {opponent.name}!")
                    print(f"Defeated Main Eventers: {shockmaster.defeated_main_eventers}")

                    # Check if all main eventers have been defeated
                    all_defeated = all(
                        me_name in [name.lower() for name in shockmaster.defeated_main_eventers] for me_name in main_eventer_names
                    )
                    if all_defeated:
                        declare_world_champion(shockmaster)

            # Reset health and stamina after the match
            shockmaster.health = shockmaster.max_health
            shockmaster.stamina = shockmaster.max_stamina

            # Reset opponent's health and stamina for future matches
            opponent.health = opponent.max_health
            opponent.stamina = opponent.max_stamina
        else:
            print(f"{opponent.name} defeated {shockmaster.name}!")
            # Optionally, reset Shockmaster's health and stamina here
            shockmaster.health = shockmaster.max_health
            shockmaster.stamina = shockmaster.max_stamina
    else:
        print("No more opponents available in this category.")

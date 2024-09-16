import random

def talk_backstage(shockmaster):
    
    wrestlers = {
        '1': '2 Cold Scorpio',
        '2': 'Brian Pillman',
        '3': 'Jim Ross',
        '4': '"Stunning" Steve Austin',
        '5': 'Big Van Vader'
    }

    print("\nBackstage, you see several wrestlers you can talk to:")
    for key, name in wrestlers.items():
        print(f"[{key}] {name}")

    choice = input("Who would you like to talk to? ").strip()

    if choice in wrestlers:
        wrestler_name = wrestlers[choice]
        interact_with_wrestler(shockmaster, wrestler_name)
    else:
        print("Invalid choice. You decide to keep to yourself.")

def interact_with_wrestler(shockmaster, wrestler_name):
    
    teasing_comments = [
        f"{wrestler_name} smirks, 'Well, if it isn't the Shockmaster! Still making grand entrances?'",
        f"{wrestler_name} laughs, 'Didn't expect to see you still around, Shockmaster!'",
        f"{wrestler_name} chuckles, 'Heard you tripped over your own feet again!'"
    ]

    
    encouraging_comments = [
        f"But seriously, {wrestler_name} adds, 'Gotta hand it to you, not many stick it out like you have.'",
        f"{wrestler_name} continues, 'Respect for hanging in there. Keep pushing!'",
        f"Then {wrestler_name} says, 'All jokes aside, your persistence is impressive.'"
    ]


    tease = random.choice(teasing_comments)
    encourage = random.choice(encouraging_comments)

    fame_gain = random.randint(5, 12)
    power_gain = random.randint(5, 12)

    print(f"\n{tease}")
    print(f"{encourage}")
    print(f"\nYou gain {fame_gain} fame points and {power_gain} power points!")

    shockmaster.fame_points += fame_gain
    shockmaster.power += power_gain

    print(f"\nCurrent Fame Points: {shockmaster.fame_points}")
    print(f"Current Power: {shockmaster.power}")

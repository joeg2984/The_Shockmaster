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
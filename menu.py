class Menu:
    def __init__(self, options):
        self.options = options

    def get_choice(self):
        for idx, option in enumerate(self.options, 1):
            print(f"{idx}. {option}")
        choice = input("Choose an option: ")
        try:
            choice = int(choice)
            if 1 <= choice <= len(self.options):
                return choice
            else:
                print("Not a valid choice! Shameful!! Try again!")
                return self.get_choice()
        except ValueError:
            print("Not a valid choice! Shameful!! Try again!")
            return self.get_choice()

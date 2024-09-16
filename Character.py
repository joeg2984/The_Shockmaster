from fight_system import Wrestler, Move
import random

class Shockmaster(Wrestler):
    def __init__(self):
        moves = [
            Move("Basic Strike", damage=10, sp_cost=5, move_type="Strike"),
            Move("Power Slam", damage=15, sp_cost=10, move_type="Grapple"),
            Move("Thunderous Slam", damage=25, sp_cost=20, move_type="Grapple", effect="Stun")
        ]

        super().__init__(
            name="The Shockmaster",
            health=100,
            max_health=100,
            power=10,
            stamina=100,
            max_stamina=100,
            moves=moves
        )

        self.fame_points = 0
        self.skills = []
        self.matches_won = 0
        self.defeated_main_eventers = []

    def train(self, activity):
        exercise_options = ["Lazy Jog", "Chair Yoga", "Pizza Plank", "Lift the Fridge", "Jazzercise!", "Commercial Break Push-Ups"]
        not_exercise_options = ["Dodge... Responsibilities", "Microwave Mega Mastery", "Remote Control Reach", "Social Media Super Scroll", "12oz Curls", "Post-Workout Nap (Without the Workout)"]
        
        if activity in exercise_options:
            self.power += 2
            self.stamina -= 10
            if self.stamina < 0:
                self.stamina = 0
            print(f"{self.name} did {activity}. Power increased to {self.power}, stamina decreased to {self.stamina}.")
        elif activity in not_exercise_options:
            self.health += 5
            if self.health > self.max_health:
                self.health = self.max_health
            print(f"{self.name} did {activity}. Health increased to {self.health}.")
        else:
            print("Unknown training activity.")

    def use_skill(self, skill_name, opponent):
        if skill_name == "Shockmaster Slam":
            if self.stamina >= 20:
                opponent.health -= 25
                self.stamina -= 20
                print(f"{self.name} used Shockmaster Slam! {opponent.name} took 25 damage and is stunned.")
            else:
                print("Not enough stamina to use Shockmaster Slam.")
        elif skill_name == "Rolling Helmet Headbutt":
            if self.stamina >= 15:
                opponent.health -= 20
                opponent.power -= 2
                self.stamina -= 15
                print(f"{self.name} used Rolling Helmet Headbutt! {opponent.name} took 20 damage and lost 2 power.")
            else:
                print("Not enough stamina to use Rolling Helmet Headbutt.")
        elif skill_name == "Shocking Combo":
            if self.stamina >= 30:
                opponent.health -= 40
                opponent.power -= 5
                self.stamina -= 30
                print(f"{self.name} used Shocking Combo! {opponent.name} took 40 damage and is severely stunned!")
            else:
                print("Not enough stamina to use Shocking Combo.")

    def feed(self, food, health_increase, stamina_increase, message):
        self.health += health_increase
        if self.health > self.max_health:
            self.health = self.max_health
        elif self.health < 0:
            self.health = 0  
        
        self.stamina += stamina_increase
        if self.stamina > self.max_stamina:
            self.stamina = self.max_stamina
        elif self.stamina < 0:
            self.stamina = 0  

        print(f"{self.name} ate {food}. {message}")
        print(f"Health: {self.health}/{self.max_health}, Stamina: {self.stamina}/{self.max_stamina}")

    def talk(self, wrestler_name):
        teasing_comments = [
            f"{wrestler_name} grins, 'Hey {self.name}, still making waves?'",
            f"{wrestler_name} laughs, 'Didn't trip on your way here, did you?'",
            f"{wrestler_name} smirks, 'I see you're still rocking that helmet!'"
        ]

        encouraging_comments = [
            f"But seriously, {wrestler_name} says, 'Keep at it, {self.name}, you're improving.'",
            f"{wrestler_name} adds, 'You've got heart, I'll give you that.'",
            f"{wrestler_name} nods, 'Respect for sticking around and getting better.'"
        ]

        tease = random.choice(teasing_comments)
        encourage = random.choice(encouraging_comments)

        fame_gain = random.randint(1, 5)
        power_gain = random.randint(0, 3)

        print(f"\n{tease}")
        print(f"{encourage}")
        print(f"\nYou gain {fame_gain} fame points and {power_gain} power points!")

        self.fame_points += fame_gain
        self.power += power_gain

        print(f"\nCurrent Fame Points: {self.fame_points}")
        print(f"Current Power: {self.power}")

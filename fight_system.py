class Move:
    def __init__(self, name, damage, sp_cost, move_type, effect=None):
        self.name = name
        self.damage = damage
        self.sp_cost = sp_cost
        self.move_type = move_type
        self.effect = effect

class Wrestler:
    def __init__(self, name, health, max_health, power, stamina, max_stamina, moves):
        self.name = name
        self.health = health
        self.max_health = max_health
        self.power = power
        self.stamina = stamina
        self.max_stamina = max_stamina
        self.moves = moves

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        return self.health > 0

    def attack(self, opponent, move):
        if self.stamina >= move.sp_cost:
            self.stamina -= move.sp_cost
            opponent.take_damage(move.damage)
            print(f"{self.name} used {move.name} on {opponent.name}, dealing {move.damage} damage!")
        else:
            print(f"{self.name} is too tired to use {move.name}.")

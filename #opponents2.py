#opponents2.py

from fight_system import Wrestler, Move

class Opponent(Wrestler):
    def __init__(self, name, health, power, stamina, moves, fame_reward):
        super().__init__(name, health, power, stamina, moves)
        self.fame_reward = fame_reward

# Define moves for opponents
opponent_moves = {
    "Bobby Eaton": [
        Move("Dropkick", damage=8, sp_cost=5, move_type="Strike"),
        Move("Headlock", damage=6, sp_cost=4, move_type="Submission")
    ],
    # Define moves for other opponents...
}

# Jobbers roster
jobbers = [
    Opponent("Bobby Eaton", 50, 5, 40, opponent_moves["Bobby Eaton"], fame_reward=5),
    # Add other jobbers...
]

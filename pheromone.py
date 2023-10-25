# ======= #
# IMPORTS #
# ======= #
import numpy as np

from ant import *
from antcolony import *
from environment import *


# =============== #
# PHEROMONE CLASS #
# =============== #
class Pheromone:
    # =========== #
    # INIT METHOD #
    # =========== #
    def __init__(self, env: Environment, type: str, evaporation_rate=0.2):
        self.env = env
        self.type = type  # 'food' or 'home' for example
        self.evaporation_rate = evaporation_rate
        self.pheromone_grid = np.zeros((env.height, env.width))

    # ============== #
    # DEPOSIT METHOD #
    # ============== #
    def deposit(self, x, y, amount: float):
        # Deposit pheromone at a specific location (x, y) with a specified amount
        self.pheromone_grid[y, x] += amount

    # ================ #
    # EVAPORATE METHOD #
    # ================ #
    def evaporate(self):
        # Apply evaporation to pheromones in the grid
        self.pheromone_grid *= 1 - self.evaporation_rate

    # =================== #
    # GET STRENGHT METHOD #
    # =================== #
    def get_strength(self, x, y):
        # Get the strength of pheromone at a specific location (x, y)
        return self.pheromone_grid[y, x]

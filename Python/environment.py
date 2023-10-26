import numpy as np


# ================= #
# ENVIRONMENT CLASS #
# ================= #
class Environment:
    # =========== #
    # INIT METHOD #
    # =========== #
    def __init__(self, width: int, height: int):
        # Environment dimensions:
        self.width = width
        self.height = height

        # Environment 2D representation:
        self.grid = np.empty((height, width))

        # Pheromone tracks:
        self.home_pheromones = Pheromone(self, "home", evaporation_rate=0.1)
        self.food_pheromones = Pheromone(self, "food", evaporation_rate=0.2)

        # Default pheromone value:
        self.default_pheromone_value = 5

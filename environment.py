import numpy as np


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
        self.home_pheromones = np.zeros((height, width))
        self.food_pheromones = np.zeros((height, width))

        # Default pheromone value:
        self.default_pheromone_value = 5

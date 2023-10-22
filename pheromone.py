import numpy as np

class Pheromone:

	# =========== #
    # INIT METHOD #
    # =========== #
	def __init__(self, env, type, evaporation_rate=0.1):
        self.env = env
        self.type = type  # 'food' or 'home' for example
        self.evaporation_rate = evaporation_rate
        self.pheromone_grid = np.zeros((env.height, env.width))


    # ============== #
    # DEPOSIT METHOD #
    # ============== #
    def deposit(self, x, y, amount):
        # Deposit pheromone at a specific location (x, y) with a specified amount
        self.pheromone_grid[y, x] += amount

    # ================ #
    # EVAPORATE METHOD #
    # ================ #
    def evaporate(self):
        # Apply evaporation to pheromones in the grid
        self.pheromone_grid *= (1 - self.evaporation_rate)

    # =================== #
    # GET STRENGHT METHOD #
    # =================== #
    def get_strength(self, x, y):
        # Get the strength of pheromone at a specific location (x, y)
        return self.pheromone_grid[y, x]
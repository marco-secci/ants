# ======= #
# IMPORTS #
# ======= #
import numpy as np

from antcolony import *
from environment import *
from pheromone import *


# ========= #
# ANT CLASS #
# ========= #
class Ant:
    # =========== #
    # INIT METHOD #
    # =========== #
    def __init__(self, id: int, x: float, y: float):
        self.id = id
        self.x = x
        self.y = y
        self.searching_food = True
        self.returning_home = False

    # =========== #
    # MOVE METHOD #
    # =========== #
    def move(self, new_x: float, new_y: float):
        # TODO implement logic behind  (maybe not needed)
        self.x = new_x
        self.y = new_y

    # ========================================================================= #
    # ============================== PHEROMONES =============================== #
    # ========================================================================= #

    # ==================== #
    # LAY PHEROMONE METHOD #
    # ==================== #
    def lay_pheromone(self, env: Environment):
        x, y = self.x, self.y
        if self.searching_food:
            # Adding the environment's default pheromone amount:
            env.home_pheromones[x, y] += env.default_pheromone_value
        if self.returning_home:
            # Adding the environment's default pheromone amount
            env.home_pheromones[x, y] += env.default_pheromone_value

    # ======================= #
    # FOLLOW PHEROMONE METHOD #
    # ======================= #
    def follow_pheromone(self, x, y, env: Environment, type: Pheromone):
        # Cells where the ant is capable of moving:
        adjacent_cells = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        positions = np.array(adjacent_cells)

        # Valid positions for following the right pheromone track - gets updated at every iteration:
        valid_positions = positions[
            (positions[:, 0] >= 0)
            & (positions[:, 0] < env.width)
            & (positions[:, 1] >= 0)
            & (positions[:, 1] < env.height)
        ]

        # Checking if there's a pheromone track of the right type nearby:
        for position in valid_positions:
            # Following a track leading to food:
            if (
                type.type == "food"
                and env.food_pheromones[position[1], position[0]] > 0
            ):
                # Moving to the pheromone's position
                self.move(position[0], position[1])

                # Calling recursively this functon to look around the new position
                # for other pheromones:
                self.follow_pheromone(self, position[0], position[1], env, type)
                break

            # Following a track leading to the colony:
            elif (
                type.type == "home"
                and env.home_pheromones[position[1], position[0]] > 0
            ):
                # Moving to the pheromone's position
                self.move(position[0], position[1])

                # Calling recursively this functon to look around the new position
                # for other pheromones:
                self.follow_pheromone(self, position[0], position[1], env, type)
                break


# =============== #
# LARVAE SUBCLASS #
# =============== #
class Larvae(Ant):
    # =========== #
    # INIT METHOD #
    # =========== #
    def __init__(self, x, y):
        # Inheritance from the Ant superclass
        super().__init__(x, y)
        self.stage = "larvae"

    def eat(self, food_needed, food_portion):
        pass

    def pupate(self):
        pass


# ============== #
# PUPAE SUBCLASS #
# ============== #
class Pupae(Ant):
    # =========== #
    # INIT METHOD #
    # =========== #
    def __init__(self, x, y, stage):
        # Inheriting attributes:
        super().__init__(x, y)

        # Defining new attributes:
        self.stage = stage

    def eat(self, food_needed, food_portion):
        pass

    def grow(self):
        pass


# =============== #
# WORKER SUBCLASS #
# =============== #
class Worker(Ant):
    pass

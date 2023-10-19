import numpy as np
import matplotlib
import pandas as pd
import statistics
from datetime import datetime as dt
import random


# =============== #
# ANT AGENT CLASS #
# =============== #
class AntAgent:
    """
    ## `AntAgent` class

    ====================================

    #### Description

    Creates the various ant agents that exist in an anthouse, like the Queen, workers, larvae, eggs, etc
    and give them attributes like their lifespan, their hatching time, their task, if they're holding something, etc.
    """

    # =========== #
    # INIT METHOD #
    # =========== #
    def __init__(self, x: float, y: float, agent_type: str):
        """
        ## `__init__` method

        ====================================

        #### Description

        Creates an ant. It gives it a position, a role, and check if it has laid egg (only queens can lay eggs).

        ====================================

        #### Parameters

        #### - `x`: `float`
            position of the ant on the `x` axis;

        #### - `y`: `float`
            position of the ant on the `y` axis;

        #### - `agent_type`: `str`
            title or role of the ant; choose from list:
            - Queen
            - Egg
            - Larvae
            - Worker
        """
        self.x = x
        self.y = y
        self.agent_type = agent_type
        self.has_laid_egg = False


# ===================== #
# ANT ENVIRONMENT CLASS #
# ===================== #
class AntEnvironment:
    """
    ## `AntEnvironment` class

    ====================================

    #### Description

    Creates the starting environment in which the ants will operate and create their settlement.
    It's in 2D for now but will soon become 3D as an anthouse has multiple layers.
    """

    # =========== #
    # INIT METHOD #
    # =========== #
    def __init__(self, width, height):
        """
        ## `__init__` method

        ====================================

        #### Description

        Creates the starting environment in which the ants will operate and create their settlement.
        It's in 2D for now but will soon become 3D as an anthouse has multiple layers.

        ====================================

        #### Parameters

        #### - `width`: `int`
            width of the environment;

        #### - `height`: `int`
            height of the environment.
        """
        self.width = width
        self.height = height
        # Creating an empty environment - 0 = empty
        self.grid = np.zeros((width, height), dtype=object)

    # ================ #
    # ADD AGENT METHOD #
    # ================ #
    def add_agent(self, x: float, y: float, agent_type: str):
        """
        ## `add_agent` method

        ====================================

        #### Description

        Collocates an `Agent` of the specified type in the environment,
        at the chosen coordinates.

        ====================================

        #### Parameters

        #### - `x`: `float`
            `x` coordinate of the first location of the `Agent`

        #### - `y`: `float`
            `y` coordinate of the first location of the `Agent`
        """
        agent = AntAgent(x, y, agent_type)
        self.grid[x, y] = agent

    # ======================= #
    # EXPAND TERRITORY METHOD #
    # ======================= #
    def expand_territory(self, x: float, y: float):
        """
        ## `expand_territory` method

        ====================================

        #### Description

        Expands the territory controlled by the ant colony. In this early stage, it's made by only laying eggs.
        TODO: every square of the grid will have an ID that indicates its state: if it's free, if there's an obstacle,
        food, or if it has been colonized by the ants.

        ====================================

        #### Parameters

        #### - `x`: `float`
            `x` coordinate of the territory that will be checked for expansion

        #### - `y`: `float`
            `y` coordinate of the territory that will be checked for expansion
        """
        # Simulate the queen expanding her territory
        if self.grid[x, y] is None:
            self.add_agent(x, y, "Queen")
        elif self.grid[x, y].agent_type == "Egg":
            self.grid[x, y].has_laid_egg = True

    # ============== #
    # DISPLAY METHOD #
    # ============== #
    def display(self):
        for row in self.grid:
            row_str = ""
            for cell in row:
                if cell is None:
                    row_str += " "
                elif isinstance(cell, AntAgent):
                    row_str += cell.agent_type[0]
                else:
                    row_str += str(cell)
            print(row_str)

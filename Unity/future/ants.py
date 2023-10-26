import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statistics
from datetime import datetime as dt
import random
from matplotlib.colors import ListedColormap
from matplotlib.animation import FuncAnimation
import seaborn as sns

# Agent index definition:
AGENT_TYPES = {"Empty": 0, "Queen": 1, "Egg": 2, "Larvae": 3}

cmap = ListedColormap(["white", "red", "blue", "green"])


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
        self.incubation_time = self.calculate_incubation_time()

    # ========================= #
    # CALCULATE INCUBATION TIME #
    # ========================= #
    def calculate_incubation_time(self):
        """
        ## `calculate_incubation_time` method

        ====================================

        #### Description

        Calculates a random incubation time for each egg and assigns it to the egg.
        """
        # Using a normal distribution to assign an incubation time to each egg:
        mean_incubation_time = 10
        std_deviation = 2
        return max(1, int(random.normalvariate(mean_incubation_time, std_deviation)))


# ============ #
# LARVAE CLASS #
# ============= #
class Larvae(AntAgent):
    """
    ## `Larvae` class

    ====================================

    #### Description

    After an Egg hatches, a Larvae will be born. This Larvae has special needs like eating
    (for now just eating lol)
    """

    # =========== #
    # INIT METHOD #
    # =========== #
    def __init__(self, x: float, y: float):
        """
        ## `__init__` method

        ====================================

        #### Description

        Defines how quickly the larvae gets hungry. It can ask for `3` to `5` meals a week

        ====================================

        #### Parameters

        same as superclass
        """
        super().__init__(x, y, "Larvae")
        # Defining how hungry is this larvae:
        self.feeding_needs = random.randint(2, 4)
        # Indicating how long ago the larvae ate:
        self.days_since_last_meal = 0

    # =========== #
    # FEED METHOD #
    # =========== #
    def feed(self):
        """
        ## `feed` method

        ====================================

        #### Description

        If a Larvae is fed, today is the day of its last meal, so the according
        variable will be set to 0.
        """
        self.days_since_last_meal = 0

    # ================ #
    # IS HUNGRY METHOD #
    # ================ #
    def is_hungry(self):
        """
        `is_hungry` method

        ====================================

        #### Description

        Returns `True` if the Larvae is hungry, `False` if it's not, according to how long
        ago was its last meal.
        """
        return self.days_since_last_meal >= self.feeding_needs


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
        self.grid = np.zeros((width, height), dtype=int)
        self.figure, self.ax = plt.subplots()
        self.img = self.ax.imshow(self.grid, interpolation="none", cmap=cmap)
        self.animation = FuncAnimation(
            self.figure, self.update, frames=20, repeat=False, blit=False
        )

    # ============= #
    # UPDATE METHOD #
    # ============= #
    def update(self, day):
        for x in range(self.width):
            for y in range(self.height):
                if isinstance(self.grid[x, y], int):
                    self.grid[x, y] = max(0, self.grid[x, y] - 1)
        self.img.set_data(self.grid)
        return self.img

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
        # agent = AntAgent(x, y, agent_type)
        self.grid[x, y] = AGENT_TYPES[agent_type]

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
        if self.grid[x, y] is None:
            # If there's nothing on the selected square, add a Queen Agent
            # at that coordinates:
            self.add_agent(x, y, "Queen")
        elif self.grid[x, y].agent_type == "Egg":
            # If there's already an Egg Agent there, mark the square as such:
            self.grid[x, y].has_laid_egg = True

    # ================= #
    # HATCH EGGS METHOD #
    # ================= #
    def hatch_eggs(self):
        """
        ## `hatch_eggs` method

        ====================================

        #### Description

        When run, this scripts subtracts a day from the hatching time remaining to every Egg agent
        that is eligible for it.

        At the actual state, every egg will be eligible for hatching, but
        later in development the idea is to check if an Egg has eaten in the last `x` days, if it
        has been protected, and adding a layer of randomness to its survival (like one in some
        quantity dies for no reason).
        """
        # Searching each square of the grid for eggs:
        for x in range(self.width):
            for y in range(self.height):
                # Assume there's an agent everywhere - this will be verified later:
                agent = self.grid[x, y]
                if isinstance(agent, AntAgent) and agent.agent_type == "Egg":
                    if agent.incubation_time > 0:
                        agent.incubation_time -= 1
                    else:
                        # The egg hatched. Now there's a Larvae agent in its place.
                        self.grid[x, y] = "Larvae"

    # ================== #
    # FEED LARVAE METHOD #
    # ================== #
    def feed_larvae(self):
        """
        ## `feed_larvae` method

        ====================================

        #### Description

        When run, the script resets to `0` the days since the last meal of every Larvae agent.

        For now it's done using a simple function, but later this will take into consideration food
        stocks, workers available to feed Larvae, etc.
        """
        # Checking the whole grid for larvae to feed:
        for x in range(self.width):
            for y in range(self.height):
                agent = self.grid[x, y]
                # If it finds a Larvae agent, it gets fed:
                if isinstance(agent, Larvae):
                    if agent.is_hungry():
                        agent.feed()

    # ============== #
    # DISPLAY METHOD #
    # ============== #

    def display(self):
        """
        ## `display` method
        ====================================
        #### Description
        Prints a grid displaying territory occupation and `Agent` presence.
        """
        # Create a new grid to display
        display_grid = np.zeros((self.width, self.height), dtype=int)

        for x in range(self.width):
            for y in range(self.height):
                agent = self.grid[x, y]
                if isinstance(agent, AntAgent):
                    # If the cell contains an AntAgent, use its type for the display
                    display_grid[x, y] = AGENT_TYPES[agent.agent_type]
                else:
                    # If the cell is empty, leave it as 0
                    display_grid[x, y] = 0

        # Use seaborn to create a heatmap
        sns.heatmap(display_grid, cmap="viridis")
        plt.show()

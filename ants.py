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
    ## AntAgent class

    ====================================

    #### Description:

    Creates the various ant agents that exist in an anthouse, like the Queen, workers, larvae, eggs, etc
    and give them attributes like their lifespan, their hatching time, their task, if they're holding something, etc.
    """

    def __init__(self, x, y, agent_type):
        self.x = x
        self.y = y
        self.agent_type = agent_type
        self.has_laid_egg = False


# ===================== #
# ANT ENVIRONMENT CLASS #
# ===================== #
class AntEnvironment:
    """
    ## AntEnvironment class

    ====================================

    #### Description:

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

        #### Description:

        Creates the starting environment in which the ants will operate and create their settlement.
        It's in 2D for now but will soon become 3D as an anthouse has multiple layers.

        ====================================

        #### Parameters:

        #### - `width`: `int`
            width of the environment;

        #### - `height`: `int`
            height of the environment.
        """
        self.width = width
        self.height = height
        # Creating an empty environment - 0 = empty
        self.grid = np.zeros((width, height))

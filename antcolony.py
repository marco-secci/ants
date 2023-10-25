# ======= #
# IMPORTS #
# ======= #
import ant


# ================ #
# ANT COLONY CLASS #
# ================ #
class AntColony:
    # =========== #
    # INIT METHOD #
    # =========== #
    def __init__(self):
        self.ants = []

    # ============== #
    # ADD ANT METHOD #
    # ============== #
    def add_ant(self, ant: Ant):
        self.ants.append(ant)

    # ================= #
    # REMOVE ANT METHOD #
    # ================= #
    def rm_ant(self, ant: Ant):
        self.ants.remove(ant)

    # ================= #
    # MOVE LOGIC METHOD #
    # ================= #
    def move_logic(self):
        pass  # TODO later in development

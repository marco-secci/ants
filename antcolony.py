import ant


class AntColony:
    def __init__(self):
        self.ants = []

    def add_ant(self, ant: Ant):
        self.ants.append(ant)

    def rm_ant(self, ant: Ant):
        self.ants.remove(ant)

    def move_logic(self):
        pass  # TODO later in development

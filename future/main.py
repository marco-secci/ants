import ants
import matplotlib.pyplot as plt

environment = ants.AntEnvironment(width=10, height=10)

queen_x = 1
queen_y = 1

environment.add_agent(queen_x, queen_y, "Queen")

# Laying eggs
egg_positions = [
    (queen_x + 1, queen_y),
    (queen_x - 1, queen_y),
    (queen_x + 2, queen_y + 3),
]

for egg_x, egg_y in egg_positions:
    environment.add_agent(egg_x, egg_y, "Egg")


# =============== #
# SIMULATION LOOP #
# =============== #

# Display environment
for _ in range(20):
    environment.hatch_eggs()
    environment.feed_larvae()
    environment.display()

# plt.show()

class FoodSource:
    def __init__(self, x, y, quantity):
        self.x = x
        self.y = y
        self.quantity = quantity

    def deplete(self, amount):
        """
        Removing an amount of food from the food source because of various causes, such as ants
        eating from it
        """
        self.quantity -= amount

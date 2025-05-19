class product:
    def __init__(self, name, cost, quantity):
        self.name = name
        self.cost = cost
        self.quantity = quantity
    def __str__(self):
        return f"Product with name {self.name} and cost {self.cost}"
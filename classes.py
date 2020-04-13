# **************************** Challenge: Pizza Joint ****************************
"""
Author: Trinity Terry
pyrun: python classes.py
"""

# Create a Pizza type for representing pizzas in Python. Think about some basic properties that would define a pizza's values; things like size, crust type, and toppings would help. Define those in the __init__ method so each instance can have its own specific values for those properties.
class Pizza:
    def __init__(self):
        self.size = ""
        self.crust = ""
        self.toppings = []
    
    # Add a method for interacting with a pizza's toppings, called add_topping.
    def add_topping(self, topping):
        self.toppings.append(topping)

    # Add a method for outputting a description of the pizza (sample output below).
    def print_order(self):
        order = self.__dict__
        # print(order)
        print(f"I would like a {order['size']}-inch, {order['style']} pizza with {' and '.join(order['toppings'])}.")

meat_lovers = Pizza()
meat_lovers.size = 16
meat_lovers.style = "Deep dish"
meat_lovers.add_topping("Pepperoni")
meat_lovers.add_topping("Olives")
meat_lovers.print_order()


# Make two different instances of a pizza. If you have properly defined the class, you should be able to do something like the following code with your Pizza type.
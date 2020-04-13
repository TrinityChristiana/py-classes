# **************************** Challenge: Urban Planner ****************************
"""
Author: Trinity Terry
pyrun: python building.py
"""

import datetime
from random_names import random_name

# Create a class named Building in the building.py file and define the following fields, properties, and methods.
class Building:

    # Define your __init__ method to accept two arguments
    def __init__(self, address, stories):
        # designer - It will hold your name.
        self.designer = "Trinity Terry"
        # date_constructed - This will hold the exact time the building was created.
        self.date_constructed = "Today"
        # owner - This will store the same of the person who owns the building.
        self.owner = "Triity Terry"
        # address
        self.address = address
        # stories
        self.stories = stories

    # Define a construct() method. The method's logic should set the date_constructed field's value to datetime.datetime.now(). You will need to have import datetime at the top of your file.
    def construct(self):
        self.date_constructed = datetime.datetime.now()

    # Define a purchase() method. The method should accept a single string argument of the name of the person purchasing a building. The method should take that string and assign it to the owner property.
    def purchase(self, name):
        self.owner = name

    def print_details(self):
        building = self.__dict__
        print(f"{building['address']} was purchased by {building['owner']} on {building['date_constructed']} and has {building['stories']} stories.")


# Create 5 building instances
buildings = [Building("333 Commerce Street", 33), Building("Strada General Traian Moșoiu 24", 5), Building(
    "5 Avenue Anatole France", 276), Building("1600 Pennsylvania Ave NW", 6), Building("48009 Bilbo", 3)]

print("**************** Init Details ************ \n")
for building in buildings:
    building.print_details()

for building in buildings:
    person = random_name()
    # Have each one get purchased by a real estate magnate
    building.purchase(person)
    # After purchased, construct each one
    building.construct()

# Once all building are purchased and constructed, print the address, owner, stories, and date constructed to the terminal for each one.
print("\n **************** New Details ************ \n")
for building in buildings:
    building.print_details()
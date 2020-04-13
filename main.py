# **************************** Challenge: Urban Planner II ****************************
"""
Author: Trinity Terry
pyrun: python main.py
"""

from building import Building
from city import City
from random_names import random_name

# Create a new city instance and add your building instances to it. Once all buildings are in the city, iterate the city's building collection and output the information about each building in the city.
megalopolis = City("Megalopolis", "Trinity", "2020")

buildings = [Building("333 Commerce Street", 33), Building("Strada General Traian Moșoiu 24", 5), Building(
    "5 Avenue Anatole France", 276), Building("1600 Pennsylvania Ave NW", 6), Building("48009 Bilbo", 3)]

for building in buildings:
    person = random_name()
    building.purchase(person)
    building.construct()
    megalopolis.add_building(building)

megalopolis.print_building_details()
class City:
    def __init__(self, name, mayor, year):
        # Name of the city.
        self.name = name
        self.mayor = mayor
        self.year = year
        self.buildings = list()

    def add_building(self, building):
        self.buildings.append(building)

    def print_building_details(self):
        buildings = self.buildings
        for building in buildings:
            build = building.__dict__
            print(f"{build['address']} was designed By {build['designer']} on {build['date_constructed']} is owned by {build['owner']} and has {build['stories']} floors")
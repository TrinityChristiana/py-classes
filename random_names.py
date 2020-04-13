import random

names = ["Presley Timms",
                "Neave Mora",
                "Antoine Smyth",
                "Nigel Conroy",
                "Kristina Mansell",
                "Gurpreet Hopper",
                "Ronaldo Vickers",
                "Rory Mendoza",
                "Zidane Bonilla",
                "Athena Roach"]

def random_name():
    person = random.choice(names)
    del names[names.index(person)]
    return person
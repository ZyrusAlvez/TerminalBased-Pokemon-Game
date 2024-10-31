from termcolor import colored

class Pokemon:
    def __init__ (self, name: str, type: str, health: int, power: int, looks: str):
        # name color
        if type == "fire":
            name_color = "red"
        if type == "grass":
            name_color = "green"
        if type == "water":
            name_color = "blue"
            
        # initialized variables
        self.name = colored(name, name_color, attrs=["bold"])
        self.type = type
        self.health = health
        self.power = power
        self.looks = looks
        self.initial_health = health
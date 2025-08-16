import json

# Basic dice: 4 basic, 1 vanguard, 1 bang
# Icon dice: 3 icon, 1 basic, 1 vanguard, 1 bang
# Vanguard dice: 2 vanguard, 1 double-vanguard, 3 bang

class Die(object):

    def __new__(cls, color, icon):
        if cls is not Die:
            return super(Die, cls).__new__(cls)
        for subclass in cls.__subclasses__():
            if icon in subclass.icons:
                return subclass(color, icon)
        raise ValueError(f'Unknown die icon: {icon}')

    def __init__(self, color, icon):
        self.color = color
        self.icon = icon

class BasicDie(Die):

    icons = ['basic']

    def __init__(self, color, icon):
        self.color = color
        self.icon = icon

class IconDie(Die):

    icons = [
            'strength', 'shield', 'pickaxe',  # red
            'compass', 'eyeball', 'dna',      # green
            'wrench', 'computer', 'science'   # blue
    ]

class VanguardDie(Die):

    icons = ['vanguard']

def calculate_probability(inputs):
    return {
            'inputs': inputs,
            'failure_probability': .1,
            'success_probability': .25,
    }

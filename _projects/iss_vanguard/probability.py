import itertools
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

    def roll_probability(self, icon):
        return self.faces.count(icon) / 6

class BasicDie(Die):

    icons = ['basic']
    faces = ['basic', 'basic', 'basic', 'basic', 'vanguard', 'bang']

    def __init__(self, color, icon):
        self.color = color
        self.icon = icon

class IconDie(Die):

    icons = [
            'strength', 'shield', 'pickaxe',  # red
            'compass', 'eyeball', 'dna',      # green
            'wrench', 'computer', 'science'   # blue
    ]

    @property
    def faces(self):
        return [
            self.icon, self.icon, self.icon,
            'basic', 'vanguard', 'bang'
        ]

class VanguardDie(Die):

    icons = ['vanguard']
    faces = ['vanguard', 'vanguard', 'double-vanguard', 'bang', 'bang', 'bang']

def prod(nums):
    result = 1
    for num in nums:
        result *= num
    return result

def choose(n, k):
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    if k == 1:
        return n
    if k > n // 2:
        k = n - k
    result = 1
    for i in range(k):
        result *= (n - i)
        result //= (i + 1)
    return result

def calculate_probability(inputs):
    dice = [
        Die(**die) for die in inputs['dice']
    ]
    fails = inputs.get('fails') or []

    failure_probability, success_probability  = 0.0, 0.0

    if len(fails) == 0 or len(dice) == 0:
        pass
    elif len(fails) == 1:
        probabilities = [die.roll_probability(fails[0]) for die in dice]
        neg = 1
        for dice_cnt in range(1, len(dice)+1):
            for probs in itertools.combinations(probabilities, dice_cnt):
                failure_probability += neg * prod(probs)
            neg *= -1

    return {
            'failure_probability': failure_probability,
            'success_probability': 0.0,
    }

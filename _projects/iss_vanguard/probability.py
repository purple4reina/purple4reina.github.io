import itertools
import json
import random

# Basic dice: 4 basic, 1 vanguard, 1 bang
# Icon dice: 3 icon, 1 basic, 1 vanguard, 1 bang
# Vanguard dice: 2 vanguard, 1 double-vanguard, 3 bang

vanguard_conversion_icons = (
        'strength', 'shield', 'pickaxe',
        'compass', 'eyeball', 'dna',
        'wrench', 'computer', 'science',
        'basic',
)

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

    def roll(self):
        return random.choice(self.faces)

class BasicDie(Die):

    icons = ['basic']
    faces = ['basic', 'basic', 'basic', 'basic', 'vanguard', 'bang']

class IconDie(Die):

    icons = [
            'strength', 'shield', 'pickaxe',  # red
            'compass', 'eyeball', 'dna',      # green
            'wrench', 'computer', 'science',  # blue
    ]

    @property
    def faces(self):
        return [
            self.icon, self.icon, self.icon,
            'basic', 'vanguard', 'bang',
        ]

class VanguardDie(Die):

    icons = ['vanguard']
    faces = ['vanguard', 'vanguard', 'double-vanguard', 'bang', 'bang', 'bang']

class DiceRoller(object):

    @staticmethod
    def from_inputs(inputs):
        return DiceRoller(
                dice=[Die(**die) for die in inputs['dice']],
                fails=inputs.get('fails') or [],
                fail_condition=inputs.get('failCondition', 'or'),
                successes=inputs.get('successes') or [],
                success_condition=inputs.get('successCondition', 'or'),
                conversion=inputs.get('conversion'),
        )

    def __init__(self, dice, fails=None, fail_condition=None, successes=None,
            success_condition=None, conversion=None):
        self.dice = dice
        self.fails = fails or []
        self.fail_condition = fail_condition or 'or'
        self.successes = successes or []
        self.success_condition = success_condition or 'or'
        self.conversion = conversion

    def roll(self):
        return Result(
                [(die.color, die.roll()) for die in self.dice],
                fails=self.fails,
                fail_condition=self.fail_condition,
                successes=self.successes,
                success_condition=self.success_condition,
                conversion=self.conversion,
        )

class Result(object):

    def __init__(self, result, fails=None, fail_condition=None, successes=None,
            success_condition=None, conversion=None):
        self.result = result
        self.fails = fails or []
        self.fail_condition = fail_condition or 'or'
        self.successes = successes or []
        self.success_condition = success_condition or 'or'
        self.conversion = conversion

    def fail(self):
        if not self.fails:
            return False
        if self.fail_condition == 'and':
            fails = self.fails.copy()
            for _, face in self.result:
                if face in fails:
                    fails.remove(face)
            return not fails
        elif self.fail_condition == 'or':
            for _, face in self.result:
                if face in self.fails:
                    return True
        return False

    def success(self):
        # assume only `or` for now
        if not self.successes:
            return False
        for color, face in self.result:
            if face in self.successes:
                return True
            elif face == 'vanguard':
                return True
            elif face == 'double-vanguard':
                return True
            elif face == 'basic' \
                    and self.conversion \
                    and self.conversion['color'] == color \
                    and self.conversion['icon'] in self.successes:
                return True
        return False

def calculate_probability(inputs):
    roller = DiceRoller.from_inputs(inputs)
    fail_count, success_count, samples = 0, 0, 10_000_000

    for _ in range(samples):
        result = roller.roll()
        if result.fail():
            fail_count += 1
        elif result.success():
            success_count += 1

    return {
            'failure_probability': fail_count / samples,
            'success_probability': success_count / samples,
    }

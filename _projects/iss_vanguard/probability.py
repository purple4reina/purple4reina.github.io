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
        return self.faces[int(random.random() * 6)]

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
                dice=[Die(**die) for die in inputs.get('dice') or []],
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
            for color, face in self.result:
                if face in fails:
                    fails.remove(face)
                elif color in fails:
                    fails.remove(color)
                if not fails:
                    return True
        elif self.fail_condition == 'or':
            for color, face in self.result:
                if face in self.fails:
                    return True
                if color in self.fails:
                    return True
        return False

    def success(self):
        if not self.successes:
            return False
        if self.success_condition == 'and':
            successes = self.successes.copy()
            vanguards = 0
            for color, face in self.result:
                if face in successes:
                    successes.remove(face)
                elif face == 'vanguard':
                    vanguards += 1
                elif face == 'double-vanguard':
                    vanguards += 2
                elif face == 'basic' \
                        and self.conversion \
                        and self.conversion['color'] == color \
                        and self.conversion['icon'] in successes:
                    successes.remove(self.conversion['icon'])
                if len(successes) <= vanguards:
                    return True
        elif self.success_condition == 'or':
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
    fail_count, success_count, samples = 0, 0, 1_000_000

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

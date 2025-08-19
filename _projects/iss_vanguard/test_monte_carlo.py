import itertools
import json
import os
import pytest
import random

from probability import Die, calculate_probability

monte_carlo_results_file = os.path.join(os.path.dirname(__file__), 'monte_carlo_results.json')

@pytest.fixture(scope='session')
def monte_carlo(request, monte_carlo_update, monte_carlo_create):
    class monte_carlo:
        update = monte_carlo_update
        create = monte_carlo_create

        samples = 100_000
        diff = 0.01

        results = []
        write = results.append

    if monte_carlo.create:
        inputs  = []
        for dice_cnt in range(4):
            for dice in itertools.combinations_with_replacement(available_dice, dice_cnt):
                for fails_cnt in range(dice_cnt+1):
                    inputs.append(({
                        'dice': [{'color': color, 'icon': icon} for color, icon in dice],
                        'fails': ['bang'] * fails_cnt,
                        'failCondition': 'or',
                    }, 0))
                for success in selected_successes:
                    for conversion_color, conversion_icon in selected_conversions:
                        inputs.append(({
                            'dice': [{'color': color, 'icon': icon} for color, icon in dice],
                            'successes': [success],
                            'successCondition': 'or',
                            'conversion': {'color': conversion_color, 'icon': conversion_icon},
                        }, 0))
        with open(monte_carlo_results_file, 'w') as f:
            json.dump(inputs, f, indent=2)
        pytest.skip("Monte Carlo data created, run tests again with --monte-carlo to check results")

    yield monte_carlo

    if monte_carlo.update:
        with open(monte_carlo_results_file, 'w') as f:
            json.dump(monte_carlo.results, f, indent=2)

available_colors = [
        'red',
        'green',
        'blue',
]
available_dice = [
        ('red', 'basic'),
        ('red', 'strength'),
        ('red', 'shield'),
        ('red', 'pickaxe'),
        ('red', 'vanguard'),

        ('green', 'basic'),
        ('green', 'compass'),
        ('green', 'eyeball'),
        ('green', 'dna'),
        ('green', 'vanguard'),

        ('blue', 'basic'),
        ('blue', 'wrench'),
        ('blue', 'computer'),
        ('blue', 'science'),
        ('blue', 'vanguard'),
]
selected_successes = [
        'strength', 'shield',
        'compass', 'eyeball',
        'wrench', 'computer',
        'basic', 'vanguard',
]
available_icons = [
        'strength', 'shield', 'pickaxe',
        'compass', 'eyeball', 'dna',
        'wrench', 'computer', 'science',
]
selected_conversions = [
        ('red', 'compass'),
        ('blue', 'wrench'),
        ('green', 'strength'),
]

def roll_die(die):
    return random.choice(die.faces)

def roll_dice(dice):
    return [(die.color, roll_die(die)) for die in dice]

class ResultsCalculator(object):

    def __init__(self, dice, fails=None, successes=None, conversion=None):
        self.dice = dice
        self.fails = fails or []
        self.successes = successes or []
        self.conversion = conversion

    def roll_dice(self):
        return [(die.color, roll_die(die)) for die in self.dice]

    def roll_die(self, die):
        return random.choice(die.faces)

    def fails_in_result(self, result):
        # assume only `or` for now
        for _, face in result:
            if face in self.fails:
                return True
        return False

    def successes_in_result(self, result):
        # assume only `or` for now
        if not self.successes:
            return False
        for color, face in result:
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

with open(monte_carlo_results_file) as f:
    monte_carlo_tests = json.load(f)

@pytest.mark.parametrize('inputs,expect', monte_carlo_tests)
def test_monte_carlo_json(inputs, expect, monte_carlo):
    actual = calculate_probability(inputs)

    if not monte_carlo.update:
        assert actual == expect
        return

    dice = [Die(**die) for die in inputs['dice']]
    fails = inputs.get('fails') or []
    successes = inputs.get('successes') or []

    runner = ResultsCalculator(
            dice,
            fails=fails,
            successes=successes,
            conversion=inputs.get('conversion'),
    )

    fail_hits = success_hits = 0
    for i in range(monte_carlo.samples):
        result = runner.roll_dice()
        fail_hits += runner.fails_in_result(result)
        success_hits += runner.successes_in_result(result)

    expect = fail_hits / monte_carlo.samples
    assert abs(actual['failure_probability'] - expect) < monte_carlo.diff

    expect = success_hits / monte_carlo.samples
    assert abs(actual['success_probability'] - expect) < monte_carlo.diff

    monte_carlo.write((inputs, actual))

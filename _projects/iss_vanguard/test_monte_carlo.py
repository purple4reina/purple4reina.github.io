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
                    for fail_cond in fail_conditions:
                        inputs.append(({
                            'dice': [{'color': color, 'icon': icon} for color, icon in dice],
                            'fails': ['bang'] * fails_cnt,
                            'failCondition': fail_cond,
                        }, 0))
        with open(monte_carlo_results_file, 'w') as f:
            json.dump(inputs, f, indent=2)
        pytest.skip("Monte Carlo data created, run tests again with --monte-carlo to check results")

    yield monte_carlo

    if monte_carlo.update:
        with open(monte_carlo_results_file, 'w') as f:
            json.dump(monte_carlo.results, f, indent=2)

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
available_faces = [
        'strength', 'shield', 'pickaxe',
        'compass', 'eyeball', 'dna',
        'wrench', 'computer', 'science',
        'basic', 'vanguard', 'double-vanguard', 'bang',
]
fail_conditions = ['or']

def roll_die(die):
    return random.choice(die.faces)

def roll_dice(dice):
    return [roll_die(die) for die in dice]

def fails_in_result(fails, result):
    # assume only `or` for now
    return any(fail in result for fail in fails)

with open(monte_carlo_results_file) as f:
    monte_carlo_tests = json.load(f)

@pytest.mark.parametrize('inputs,expect', monte_carlo_tests)
def test_monte_carlo_json(inputs, expect, monte_carlo):
    actual = calculate_probability(inputs)

    if not monte_carlo.update:
        assert actual == expect
        return

    dice = [Die(**die) for die in inputs['dice']]
    fails = inputs['fails']
    hits = 0
    for i in range(monte_carlo.samples):
        result = roll_dice(dice)
        hits += fails_in_result(fails, result)
    expect = hits / monte_carlo.samples

    assert abs(actual['failure_probability'] - expect) < monte_carlo.diff

    monte_carlo.write((inputs, actual))

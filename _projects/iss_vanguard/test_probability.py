import pytest

from probability import (
        Die, BasicDie, IconDie, VanguardDie, calculate_probability, prod,
        choose,
)

_test_die_classes = (
        ('red', 'basic', BasicDie),
        ('red', 'strength', IconDie),
        ('red', 'shield', IconDie),
        ('red', 'pickaxe', IconDie),
        ('red', 'vanguard', VanguardDie),

        ('green', 'basic', BasicDie),
        ('green', 'compass', IconDie),
        ('green', 'eyeball', IconDie),
        ('green', 'dna', IconDie),
        ('green', 'vanguard', VanguardDie),

        ('blue', 'basic', BasicDie),
        ('blue', 'wrench', IconDie),
        ('blue', 'computer', IconDie),
        ('blue', 'science', IconDie),
        ('blue', 'vanguard', VanguardDie),
)

@pytest.mark.parametrize('color,icon,expect', _test_die_classes)
def test_die_classes(color, icon, expect):
    die = Die(color, icon)
    assert isinstance(die, expect)
    assert die.color == color
    assert die.icon == icon

_test_die_roll_probability = (
        ('red', 'basic', 'basic', None, 4/6),
        ('red', 'basic', 'vanguard', None, 1/6),
        ('red', 'basic', 'bang', None, 1/6),

        ('red', 'strength', 'basic', None, 1/6),
        ('red', 'strength', 'strength', None, 3/6),
        ('red', 'strength', 'vanguard', None, 1/6),
        ('red', 'strength', 'bang', None, 1/6),

        ('red', 'shield', 'basic', None, 1/6),
        ('red', 'shield', 'shield', None, 3/6),
        ('red', 'shield', 'vanguard', None, 1/6),
        ('red', 'shield', 'bang', None, 1/6),

        ('red', 'pickaxe', 'basic', None, 1/6),
        ('red', 'pickaxe', 'pickaxe', None, 3/6),
        ('red', 'pickaxe', 'vanguard', None, 1/6),
        ('red', 'pickaxe', 'bang', None, 1/6),

        ('red', 'vanguard', 'basic', None, 0),
        ('red', 'vanguard', 'strength', None, 0),
        ('red', 'vanguard', 'shield', None, 0),
        ('red', 'vanguard', 'pickaxe', None, 0),
        ('red', 'vanguard', 'vanguard', None, 2/6),
        ('red', 'vanguard', 'double-vanguard', None, 1/6),
        ('red', 'vanguard', 'bang', None, 3/6),

        ('green', 'basic', 'basic', None, 4/6),
        ('green', 'basic', 'vanguard', None, 1/6),
        ('green', 'basic', 'bang', None, 1/6),

        ('green', 'compass', 'basic', None, 1/6),
        ('green', 'compass', 'compass', None, 3/6),
        ('green', 'compass', 'vanguard', None, 1/6),
        ('green', 'compass', 'bang', None, 1/6),

        ('green', 'eyeball', 'basic', None, 1/6),
        ('green', 'eyeball', 'eyeball', None, 3/6),
        ('green', 'eyeball', 'vanguard', None, 1/6),
        ('green', 'eyeball', 'bang', None, 1/6),

        ('green', 'dna', 'basic', None, 1/6),
        ('green', 'dna', 'dna', None, 3/6),
        ('green', 'dna', 'vanguard', None, 1/6),
        ('green', 'dna', 'bang', None, 1/6),

        ('green', 'vanguard', 'basic', None, 0),
        ('green', 'vanguard', 'compass', None, 0),
        ('green', 'vanguard', 'eyeball', None, 0),
        ('green', 'vanguard', 'dna', None, 0),
        ('green', 'vanguard', 'vanguard', None, 2/6),
        ('green', 'vanguard', 'double-vanguard', None, 1/6),
        ('green', 'vanguard', 'bang', None, 3/6),

        ('blue', 'basic', 'basic', None, 4/6),
        ('blue', 'basic', 'vanguard', None, 1/6),
        ('blue', 'basic', 'bang', None, 1/6),

        ('blue', 'wrench', 'basic', None, 1/6),
        ('blue', 'wrench', 'wrench', None, 3/6),
        ('blue', 'wrench', 'vanguard', None, 1/6),
        ('blue', 'wrench', 'bang', None, 1/6),

        ('blue', 'computer', 'basic', None, 1/6),
        ('blue', 'computer', 'computer', None, 3/6),
        ('blue', 'computer', 'vanguard', None, 1/6),
        ('blue', 'computer', 'bang', None, 1/6),

        ('blue','science','basic', None, 1/6),
        ('blue','science','science', None, 3/6),
        ('blue','science','vanguard', None, 1/6),
        ('blue','science','bang', None, 1/6),

        ('blue', 'vanguard', 'basic', None, 0),
        ('blue', 'vanguard', 'wrench', None, 0),
        ('blue', 'vanguard', 'computer', None, 0),
        ('blue', 'vanguard', 'science', None, 0),
        ('blue', 'vanguard', 'vanguard', None, 2/6),
        ('blue', 'vanguard', 'double-vanguard', None, 1/6),
        ('blue', 'vanguard', 'bang', None, 3/6),
)

@pytest.mark.parametrize('color,icon,face,conversions,expect', _test_die_roll_probability)
def test_die_roll_probability(color, icon, face, conversions, expect):
    assert Die(color, icon, conversions=conversions).roll_probability(face) == expect

_test_prod = (
        ([], 1),
        ([1], 1),
        ([2], 2),
        ([2, 3], 6),
        ([2, 3, 4], 24),
)

@pytest.mark.parametrize('nums,expect', _test_prod)
def test_prod(nums,expect):
    assert prod(nums) == expect

_test_choose = (
        (0, 0, 1),
        (1, 0, 1),
        (1, 1, 1),
        (2, 0, 1),
        (2, 1, 2),
        (2, 2, 1),
        (3, 0, 1),
        (3, 1, 3),
        (3, 2, 3),
        (3, 3, 1),
        (4, 0, 1),
        (4, 1, 4),
        (4, 2, 6),
        (4, 3, 4),
        (4, 4, 1),
        (5, 0, 1),
        (5, 1, 5),
        (5, 2, 10),
        (5, 3, 10),
        (5, 4, 5),
        (5, 5, 1),
        (6, 0, 1),
        (6, 1, 6),
        (6, 2, 15),
        (6, 3, 20),
        (6, 4, 15),
        (6, 5, 6),
        (6, 6, 1),
        (7, 0, 1),
        (7, 1, 7),
        (7, 2, 21),
        (7, 3, 35),
        (7, 4, 35),
        (7, 5, 21),
        (7, 6, 7),
        (7, 7, 1),
)

@pytest.mark.parametrize('n,k,expect', _test_choose)
def test_choose(n, k, expect):
    assert choose(n, k) == expect

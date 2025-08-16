import pytest

from probability import Die, BasicDie, IconDie, VanguardDie, calculate_probability

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
        ('red', 'basic', 'basic', 4/6),
        ('red', 'basic', 'vanguard', 1/6),
        ('red', 'basic', 'bang', 1/6),

        ('red', 'strength', 'basic', 1/6),
        ('red', 'strength', 'strength', 3/6),
        ('red', 'strength', 'vanguard', 1/6),
        ('red', 'strength', 'bang', 1/6),

        ('red', 'shield', 'basic', 1/6),
        ('red', 'shield', 'shield', 3/6),
        ('red', 'shield', 'vanguard', 1/6),
        ('red', 'shield', 'bang', 1/6),

        ('red', 'pickaxe', 'basic', 1/6),
        ('red', 'pickaxe', 'pickaxe', 3/6),
        ('red', 'pickaxe', 'vanguard', 1/6),
        ('red', 'pickaxe', 'bang', 1/6),

        ('red', 'vanguard', 'basic', 0),
        ('red', 'vanguard', 'strength', 0),
        ('red', 'vanguard', 'shield', 0),
        ('red', 'vanguard', 'pickaxe', 0),
        ('red', 'vanguard', 'vanguard', 2/6),
        ('red', 'vanguard', 'double-vanguard', 1/6),
        ('red', 'vanguard', 'bang', 3/6),

        ('green', 'basic', 'basic', 4/6),
        ('green', 'basic', 'vanguard', 1/6),
        ('green', 'basic', 'bang', 1/6),

        ('green', 'compass', 'basic', 1/6),
        ('green', 'compass', 'compass', 3/6),
        ('green', 'compass', 'vanguard', 1/6),
        ('green', 'compass', 'bang', 1/6),

        ('green', 'eyeball', 'basic', 1/6),
        ('green', 'eyeball', 'eyeball', 3/6),
        ('green', 'eyeball', 'vanguard', 1/6),
        ('green', 'eyeball', 'bang', 1/6),

        ('green', 'dna', 'basic', 1/6),
        ('green', 'dna', 'dna', 3/6),
        ('green', 'dna', 'vanguard', 1/6),
        ('green', 'dna', 'bang', 1/6),

        ('green', 'vanguard', 'basic', 0),
        ('green', 'vanguard', 'compass', 0),
        ('green', 'vanguard', 'eyeball', 0),
        ('green', 'vanguard', 'dna', 0),
        ('green', 'vanguard', 'vanguard', 2/6),
        ('green', 'vanguard', 'double-vanguard', 1/6),
        ('green', 'vanguard', 'bang', 3/6),

        ('blue', 'basic', 'basic', 4/6),
        ('blue', 'basic', 'vanguard', 1/6),
        ('blue', 'basic', 'bang', 1/6),

        ('blue', 'wrench', 'basic', 1/6),
        ('blue', 'wrench', 'wrench', 3/6),
        ('blue', 'wrench', 'vanguard', 1/6),
        ('blue', 'wrench', 'bang', 1/6),

        ('blue', 'computer', 'basic', 1/6),
        ('blue', 'computer', 'computer', 3/6),
        ('blue', 'computer', 'vanguard', 1/6),
        ('blue', 'computer', 'bang', 1/6),

        ('blue','science','basic' ,1/6 ),
        ('blue','science','science' ,3/6 ),
        ('blue','science','vanguard' ,1/6 ),
        ('blue','science','bang' ,1/6 ),

        ('blue', 'vanguard', 'basic', 0),
        ('blue', 'vanguard', 'wrench', 0),
        ('blue', 'vanguard', 'computer', 0),
        ('blue', 'vanguard', 'science', 0),
        ('blue', 'vanguard', 'vanguard', 2/6),
        ('blue', 'vanguard', 'double-vanguard', 1/6),
        ('blue', 'vanguard', 'bang', 3/6),
)

@pytest.mark.parametrize('color,icon,face,expect', _test_die_roll_probability)
def test_die_roll_probability(color, icon, face, expect):
    assert Die(color, icon).roll_probability(face) == expect

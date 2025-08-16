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

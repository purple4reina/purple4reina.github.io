import pytest
import random

from probability import Die, BasicDie, IconDie, VanguardDie, DiceRoller, Result

class COLOR:
    red = 'red'
    green = 'green'
    blue = 'blue'

class ICON:
    basic = 'basic'
    vanguard = 'vanguard'
    double_vanguard = 'double-vanguard'
    bang = 'bang'

    strength = 'strength'
    shield = 'shield'
    pickaxe = 'pickaxe'
    compass = 'compass'
    eyeball = 'eyeball'
    dna = 'dna'
    wrench = 'wrench'
    computer = 'computer'
    science = 'science'

class DIE:
    red_basic = (COLOR.red, ICON.basic)
    red_strength = (COLOR.red, ICON.strength)
    red_shield = (COLOR.red, ICON.shield)
    red_pickaxe = (COLOR.red, ICON.pickaxe)
    red_vanguard = (COLOR.red, ICON.vanguard)

    green_basic = (COLOR.green, ICON.basic)
    green_compass = (COLOR.green, ICON.compass)
    green_eyeball = (COLOR.green, ICON.eyeball)
    green_dna = (COLOR.green, ICON.dna)
    green_vanguard = (COLOR.green, ICON.vanguard)

    blue_basic = (COLOR.blue, ICON.basic)
    blue_wrench = (COLOR.blue, ICON.wrench)
    blue_computer = (COLOR.blue, ICON.computer)
    blue_science = (COLOR.blue, ICON.science)
    blue_vanguard = (COLOR.blue, ICON.vanguard)

class FACE:
    red_basic = (COLOR.red, ICON.basic)
    red_strength = (COLOR.red, ICON.strength)
    red_shield = (COLOR.red, ICON.shield)
    red_pickaxe = (COLOR.red, ICON.pickaxe)
    red_vanguard = (COLOR.red, ICON.vanguard)
    red_double_vanguard = (COLOR.red, ICON.double_vanguard)
    red_bang = (COLOR.red, ICON.bang)

    green_basic = (COLOR.green, ICON.basic)
    green_compass = (COLOR.green, ICON.compass)
    green_eyeball = (COLOR.green, ICON.eyeball)
    green_dna = (COLOR.green, ICON.dna)
    green_vanguard = (COLOR.green, ICON.vanguard)
    green_double_vanguard = (COLOR.green, ICON.double_vanguard)
    green_bang = (COLOR.green, ICON.bang)

    blue_basic = (COLOR.blue, ICON.basic)
    blue_wrench = (COLOR.blue, ICON.wrench)
    blue_computer = (COLOR.blue, ICON.computer)
    blue_science = (COLOR.blue, ICON.science)
    blue_vanguard = (COLOR.blue, ICON.vanguard)
    blue_double_vanguard = (COLOR.blue, ICON.double_vanguard)
    blue_bang = (COLOR.blue, ICON.bang)

class CONVERSION:
    red_strength = {'color': COLOR.red, 'icon': ICON.strength}
    red_shield = {'color': COLOR.red, 'icon': ICON.shield}
    red_pickaxe = {'color': COLOR.red, 'icon': ICON.pickaxe}
    red_compass = {'color': COLOR.red, 'icon': ICON.compass}
    red_eyeball = {'color': COLOR.red, 'icon': ICON.eyeball}
    red_dna = {'color': COLOR.red, 'icon': ICON.dna}
    red_wrench = {'color': COLOR.red, 'icon': ICON.wrench}
    red_computer = {'color': COLOR.red, 'icon': ICON.computer}
    red_science = {'color': COLOR.red, 'icon': ICON.science}

    green_strength = {'color': COLOR.green, 'icon': ICON.strength}
    green_shield = {'color': COLOR.green, 'icon': ICON.shield}
    green_pickaxe = {'color': COLOR.green, 'icon': ICON.pickaxe}
    green_compass = {'color': COLOR.green, 'icon': ICON.compass}
    green_eyeball = {'color': COLOR.green, 'icon': ICON.eyeball}
    green_dna = {'color': COLOR.green, 'icon': ICON.dna}
    green_wrench = {'color': COLOR.green, 'icon': ICON.wrench}
    green_computer = {'color': COLOR.green, 'icon': ICON.computer}
    green_science = {'color': COLOR.green, 'icon': ICON.science}

    blue_strength = {'color': COLOR.blue, 'icon': ICON.strength}
    blue_shield = {'color': COLOR.blue, 'icon': ICON.shield}
    blue_pickaxe = {'color': COLOR.blue, 'icon': ICON.pickaxe}
    blue_compass = {'color': COLOR.blue, 'icon': ICON.compass}
    blue_eyeball = {'color': COLOR.blue, 'icon': ICON.eyeball}
    blue_dna = {'color': COLOR.blue, 'icon': ICON.dna}
    blue_wrench = {'color': COLOR.blue, 'icon': ICON.wrench}
    blue_computer = {'color': COLOR.blue, 'icon': ICON.computer}
    blue_science = {'color': COLOR.blue, 'icon': ICON.science}

@pytest.fixture(scope='function', autouse=True)
def random_seed():
    random.seed(1)

_test_die_classes = (
        (COLOR.red, ICON.basic, BasicDie),
        (COLOR.red, ICON.strength, IconDie),
        (COLOR.red, ICON.shield, IconDie),
        (COLOR.red, ICON.pickaxe, IconDie),
        (COLOR.red, ICON.vanguard, VanguardDie),

        (COLOR.green, ICON.basic, BasicDie),
        (COLOR.green, ICON.compass, IconDie),
        (COLOR.green, ICON.eyeball, IconDie),
        (COLOR.green, ICON.dna, IconDie),
        (COLOR.green, ICON.vanguard, VanguardDie),

        (COLOR.blue, ICON.basic, BasicDie),
        (COLOR.blue, ICON.wrench, IconDie),
        (COLOR.blue, ICON.computer, IconDie),
        (COLOR.blue, ICON.science, IconDie),
        (COLOR.blue, ICON.vanguard, VanguardDie),
)

@pytest.mark.parametrize('color,icon,expect', _test_die_classes)
def test_die_classes(color, icon, expect):
    die = Die(color, icon)
    assert isinstance(die, expect)
    assert die.color == color
    assert die.icon == icon

    for _ in range(100):
        result = die.roll()
        assert isinstance(result, str)
        assert result in die.faces

def test_dice_roller_roll(monkeypatch):
    roller = DiceRoller.from_inputs({
        'dice': [
            {'color': COLOR.red, 'icon': ICON.basic},
            {'color': COLOR.green, 'icon': ICON.compass},
            {'color': COLOR.blue, 'icon': ICON.science},
        ],
        'fails': [ICON.bang],
        'successes': [ICON.vanguard],
        'conversion': {'color': COLOR.red, 'icon': ICON.compass},
    })

    roll_calls = []
    def mock_roll(self):
        roll_calls.append((self.color, self.icon))
        return ICON.vanguard
    monkeypatch.setattr(Die, 'roll', mock_roll)

    result = roller.roll()

    assert roll_calls == [DIE.red_basic, DIE.green_compass, DIE.blue_science]

    assert isinstance(result, Result)

    assert result.fails == [ICON.bang]
    assert result.successes == [ICON.vanguard]
    assert result.conversion == {'color': COLOR.red, 'icon': ICON.compass}

    assert len(result.result) == 3
    assert result.result[0] == FACE.red_vanguard
    assert result.result[1] == FACE.green_vanguard
    assert result.result[2] == FACE.blue_vanguard

_test_result_fail = (
        ([FACE.red_basic], [], False),
        ([FACE.red_strength], [], False),
        ([FACE.red_shield], [], False),
        ([FACE.red_pickaxe], [], False),
        ([FACE.red_vanguard], [], False),
        ([FACE.red_double_vanguard], [], False),
        ([FACE.red_bang], [], False),

        ([FACE.green_basic], [], False),
        ([FACE.green_compass], [], False),
        ([FACE.green_eyeball], [], False),
        ([FACE.green_dna], [], False),
        ([FACE.green_vanguard], [], False),
        ([FACE.green_double_vanguard], [], False),
        ([FACE.green_bang], [], False),

        ([FACE.blue_basic], [], False),
        ([FACE.blue_wrench], [], False),
        ([FACE.blue_computer], [], False),
        ([FACE.blue_science], [], False),
        ([FACE.blue_vanguard], [], False),
        ([FACE.blue_double_vanguard], [], False),
        ([FACE.blue_bang], [], False),

        ([FACE.red_basic], [ICON.bang], False),
        ([FACE.red_strength], [ICON.bang], False),
        ([FACE.red_shield], [ICON.bang], False),
        ([FACE.red_pickaxe], [ICON.bang], False),
        ([FACE.red_vanguard], [ICON.bang], False),
        ([FACE.red_double_vanguard], [ICON.bang], False),
        ([FACE.red_bang], [ICON.bang], True),

        ([FACE.green_basic], [ICON.bang], False),
        ([FACE.green_compass], [ICON.bang], False),
        ([FACE.green_eyeball], [ICON.bang], False),
        ([FACE.green_dna], [ICON.bang], False),
        ([FACE.green_vanguard], [ICON.bang], False),
        ([FACE.green_double_vanguard], [ICON.bang], False),
        ([FACE.green_bang], [ICON.bang], True),

        ([FACE.blue_basic], [ICON.bang], False),
        ([FACE.blue_wrench], [ICON.bang], False),
        ([FACE.blue_computer], [ICON.bang], False),
        ([FACE.blue_science], [ICON.bang], False),
        ([FACE.blue_vanguard], [ICON.bang], False),
        ([FACE.blue_double_vanguard], [ICON.bang], False),
        ([FACE.blue_bang], [ICON.bang], True),

        ([FACE.red_basic, FACE.red_basic], [ICON.bang], False),
        ([FACE.red_basic, FACE.red_strength], [ICON.bang], False),
        ([FACE.red_basic, FACE.red_shield], [ICON.bang], False),
        ([FACE.red_basic, FACE.red_pickaxe], [ICON.bang], False),
        ([FACE.red_basic, FACE.red_vanguard], [ICON.bang], False),
        ([FACE.red_basic, FACE.red_double_vanguard], [ICON.bang], False),
        ([FACE.red_basic, FACE.red_bang], [ICON.bang], True),
        ([FACE.red_basic, FACE.green_basic], [ICON.bang], False),
        ([FACE.red_basic, FACE.green_compass], [ICON.bang], False),
        ([FACE.red_basic, FACE.green_eyeball], [ICON.bang], False),
        ([FACE.red_basic, FACE.green_dna], [ICON.bang], False),
        ([FACE.red_basic, FACE.green_vanguard], [ICON.bang], False),
        ([FACE.red_basic, FACE.green_double_vanguard], [ICON.bang], False),
        ([FACE.red_basic, FACE.green_bang], [ICON.bang], True),
        ([FACE.red_basic, FACE.blue_basic], [ICON.bang], False),
        ([FACE.red_basic, FACE.blue_wrench], [ICON.bang], False),
        ([FACE.red_basic, FACE.blue_computer], [ICON.bang], False),
        ([FACE.red_basic, FACE.blue_science], [ICON.bang], False),
        ([FACE.red_basic, FACE.blue_vanguard], [ICON.bang], False),
        ([FACE.red_basic, FACE.blue_double_vanguard], [ICON.bang], False),
        ([FACE.red_basic, FACE.blue_bang], [ICON.bang], True),
)

@pytest.mark.parametrize('result,fails,expect', _test_result_fail)
def test_result_fail(result, fails, expect):
    assert Result(result, fails=fails).fail() is expect

_test_result_success = (
        ([], [], None, False),
        ([], [ICON.strength], None, False),

        ([FACE.red_basic], [ICON.basic], None, True),
        ([FACE.red_basic], [ICON.strength], None, False),
        ([FACE.red_strength], [ICON.strength], None, True),
        ([FACE.red_strength], [ICON.compass], None, False),
        ([FACE.red_vanguard], [ICON.basic], None, True),
        ([FACE.red_vanguard], [ICON.strength], None, True),
        ([FACE.red_vanguard], [ICON.vanguard], None, True),
        ([FACE.red_double_vanguard], [ICON.strength], None, True),
        ([FACE.red_double_vanguard], [ICON.vanguard], None, True),

        ([FACE.red_basic], [ICON.basic], CONVERSION.red_strength, True),
        ([FACE.red_basic], [ICON.strength], CONVERSION.red_strength, True),
        ([FACE.red_basic], [ICON.shield], CONVERSION.red_strength, False),
        ([FACE.red_basic], [ICON.strength], CONVERSION.green_strength, False),

        ([FACE.red_strength, FACE.green_bang], [ICON.strength], None, True),
        ([FACE.red_strength, FACE.green_dna], [ICON.shield], None, False),
        ([FACE.red_strength, FACE.green_dna], [ICON.shield], CONVERSION.red_shield, False),
)

@pytest.mark.parametrize('result,successes,conversion,expect', _test_result_success)
def test_result_success(result,successes,conversion,expect):
    assert Result(result, successes=successes, conversion=conversion).success() is expect

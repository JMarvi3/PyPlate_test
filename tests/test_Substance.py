import pytest
from pyplate.pyplate import Substance


def test_make_solid():
    """

    Tests creating a solid `Substance`.

    """
    # Argument types checked
    with pytest.raises(TypeError, match="Name must be a str"):
        Substance.solid(1, 1)
    with pytest.raises(ValueError, match="Name must not be empty"):
        Substance.solid('', 1)
    with pytest.raises(TypeError, match="Molecular weight must be a float"):
        Substance.solid('water', '1')
    # Arguments are sane
    with pytest.raises(ValueError, match="Molecular weight must be positive"):
        Substance.solid('water', -1)
    with pytest.raises(ValueError, match="Molecular weight must be positive"):
        Substance.solid('water', 0)


def test_solid(salt):
    """

    Tests that members of a solid `Substance` are correct.

    """
    assert salt.name == 'NaCl'
    assert salt.mol_weight == 58.4428


def test_make_liquid():
    """

    Tests creating a liquid `Substance`.

    """
    # Argument types checked
    with pytest.raises(TypeError, match="Name must be a str"):
        Substance.liquid(1, 1, 1)
    with pytest.raises(ValueError, match="Name must not be empty"):
        Substance.liquid('', 1, 1)
    with pytest.raises(TypeError, match="Molecular weight must be a float"):
        Substance.liquid('water', '1', 1)
    with pytest.raises(TypeError, match="Density must be a float"):
        Substance.liquid('water', 1, '1')
    # Arguments are sane
    with pytest.raises(ValueError, match="Molecular weight must be positive"):
        Substance.liquid('water', -1, 1)
    with pytest.raises(ValueError, match="Molecular weight must be positive"):
        Substance.liquid('water', 0, 1)
    with pytest.raises(ValueError, match="Density must be positive"):
        Substance.liquid('water', 1, -1)
    with pytest.raises(ValueError, match="Density must be positive"):
        Substance.liquid('water', 1, 0)


def test_liquid(water):
    """

    Tests that members of a liquid `Substance` are correct.

    """
    assert water.name == 'H2O'
    assert water.mol_weight == 18.0153
    assert water.density == 1


def test_make_enzyme():
    """

    Tests creating an enzyme `Substance`.

    """
    # Argument types checked
    with pytest.raises(TypeError, match="Name must be a str"):
        Substance.enzyme(1)
    with pytest.raises(ValueError, match="Name must not be empty"):
        Substance.enzyme('')


def test_enzyme(lipase):
    """

    Tests that members of an enzyme `Substance` are correct.

    """
    assert lipase.name == 'lipase'


def test_is_solid(salt, water, lipase):
    """

    Tests that is_solid() returns the correct values.

    """
    assert salt.is_solid() is True
    assert water.is_solid() is False
    assert lipase.is_solid() is False


def test_is_liquid(salt, water, lipase):
    """

    Tests that is_liquid() returns the correct values.

    """
    assert salt.is_liquid() is False
    assert water.is_liquid() is True
    assert lipase.is_liquid() is False


def test_is_enzyme(salt, water, lipase):
    """

    Tests that is_enzyme() returns the correct values.

    """
    assert salt.is_enzyme() is False
    assert water.is_enzyme() is False
    assert lipase.is_enzyme() is True

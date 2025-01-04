from app.src.space_object.planet import Planet
from app.src.space_object.base import SpaceObject
import pytest


def test_planet_init():
    test = Planet(SpaceObject())
    assert test.orbital_speed > 0 and test.distance > 0 and test.prev_planet > 0


def test_spaceobject_init():
    with pytest.raises(Exception) as e_info:
        Planet(SpaceObject(size=0))
    assert str(e_info.value) == 'Size can\'t be negative number or zero!'



def test_velocity():
    """ Test if raised exception on negative velocity. """
    with pytest.raises(Exception) as e_info:
        Planet(SpaceObject(), orbital_speed=-15)
    assert str(e_info.value) == 'Velocity can\'t be negative number or zero!'


def test_distance():
    """ Test if raised exception on negative distance. """
    with pytest.raises(Exception) as e_info:
        Planet(SpaceObject(), distance=-15)
    assert str(e_info.value) == 'Distance can\'t be negative number or zero!'


def test_prev_planet():
    """ Test if raised exception on negative distance to previous planet. """
    with pytest.raises(Exception) as e_info:
        Planet(SpaceObject(), prev_planet=-15)
    assert str(e_info.value) == 'Distance to previous planet can\'t be negative number or zero!'

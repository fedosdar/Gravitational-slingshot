import pytest
from app.src.space_object.base import SpaceObject


def test_spaceobject_init():
    t = SpaceObject()
    assert t.size > 0 and t.mass > 0 and t.gravitation > 0


def test_spaceobject_init_par():
    t = SpaceObject(15, 43, 52)
    assert t.size > 0 and t.mass > 0 and t.gravitation > 0


def test_size():
    """ Test if raised exception on negative size. """
    with pytest.raises(Exception) as e_info:
        SpaceObject(size=-15)
    assert str(e_info.value) == 'Size can\'t be negative number or zero!'


def test_mass():
    """ Test if raised exception on negative mass. """
    with pytest.raises(Exception) as e_info:
        SpaceObject(mass=-15)
    assert str(e_info.value) == 'Mass can\'t be negative number or zero!'


def test_gravity():
    """ Test if raised exception on negative gravity. """
    with pytest.raises(Exception) as e_info:
        SpaceObject(gravitation=-15)
    assert str(e_info.value) == 'Gravity can\'t be negative number or zero!'


# def test_image_path():
#     try:
#         test = SpaceObject()
#         test.load_image('aaa.png')
#     except FileNotFoundError:
#         assert True

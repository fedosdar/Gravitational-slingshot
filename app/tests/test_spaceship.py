from app.src.spaceship import Spaceship
from app.src.planetary_system import PlanetarySystem
import pytest


def test_spaceship_init_solar_sys():
    sol_sys = PlanetarySystem()
    test = Spaceship(sol_sys)
    assert test.starting_planet == sol_sys.planets[2]


# Fix approximation
# def test_spaceship_init_random_sys():
#     sol_sys = PlanetarySystem(solar_system=False)
#     test = Spaceship(sol_sys, solar_system=False)
#     for planet in sol_sys.planets:
#         print(round(planet.mass, 2), round(test.starting_planet.mass, 2))
#         if round(planet.mass, 2) == round(test.starting_planet.mass, 2) and round(planet.size, 2) == round(test.starting_planet.size, 2):
#             assert True
#         else:
#             assert False
#

from app.src.planetary_system import PlanetarySystem
import numpy as np


def test_init_solar_system():
    sol_sys = PlanetarySystem(solar_system=True)
    assert len(sol_sys.planets) == 8
    assert sol_sys.star.mass == 332.95


def test_init_random_system_size():
    sol_sys = PlanetarySystem(solar_system=False)
    assert 1 <= len(sol_sys.planets) <= 10 and sol_sys.star is not None


def test_star_mass():
    sol_sys = PlanetarySystem(solar_system=False)
    masses = [sol_sys.star.mass]
    for i in sol_sys.planets:
        masses.append(i.mass)
    assert np.amax(masses) == sol_sys.star.mass


def test_star_gravity():
    sol_sys = PlanetarySystem(solar_system=False)
    gravities = [sol_sys.star.gravitation]
    for i in sol_sys.planets:
        gravities.append(i.gravitation)
    assert np.max(gravities) == sol_sys.star.gravitation

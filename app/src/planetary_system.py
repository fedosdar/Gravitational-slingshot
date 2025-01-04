""" Class represents planetary system object. """
import pygame
import numpy as np
from app.src.space_object.base import SpaceObject
from app.src.space_object.planet import Planet
import app.src.generator as generator


class PlanetarySystem:
    def __init__(self, solar_system=True):
        """
        Constructor for initializing planetary system

        :param solar_system: True if needed solary system, False if random system
        """
        if solar_system:
            # TODO: config.py
            self.star = SpaceObject(109.2 / 2, 332.95, 274)

            # !!! All data from NASA or Wikipedia
            mercury = Planet(SpaceObject(0.38 * 10, 0.06, 3.7),
                             47.36 * 0.0005, 0.4,
                             self.star.size)

            venus = Planet(SpaceObject(0.95 * 10, 0.82, 8.87),
                           35.02 * 0.0005, 0.7,
                           mercury.prev_planet + mercury.size)

            earth = Planet(SpaceObject(1 * 10, 1, 9.81),
                           29.78 * 0.0005, 1,
                           venus.prev_planet + venus.size)

            mars = Planet(SpaceObject(0.53 * 10, 0.1, 3.72),
                          24.07 * 0.0005, 1.65,
                          earth.prev_planet + earth.size)

            jupiter = Planet(SpaceObject(10.97 * 5, 317.8, 24.79),
                             13.07 * 0.0005, 5.2,
                             mars.prev_planet + mars.size)

            saturn = Planet(SpaceObject(9.14 * 5, 95.16, 10.44),
                            9.68 * 0.0005, 9.58,
                            jupiter.prev_planet + jupiter.size)

            uranus = Planet(SpaceObject(4 * 5, 14.54, 8.69),
                            6.80 * 0.0005, 19.19,
                            saturn.prev_planet + saturn.size)

            neptune = Planet(SpaceObject(3.88 * 5, 17.15, 11.15),
                             5.43 * 0.0005, 30.07,
                             uranus.prev_planet + uranus.size)

            self.planets = np.array([mercury, venus, earth, mars,
                                     jupiter, saturn, uranus, neptune])

        else:
            # Random system
            # Generate random number of the planets
            num = generator.generate_integer(1, 10)

            sizes = np.empty((num + 1))
            masses = np.empty((num + 1))
            for i in range(num + 1):
                sizes[i] = generator.generate_integer(1, 110)
                masses[i] = generator.generate_float(100, 500)

            # The star has to be with the largest mass & gravity -> the largest mass & size, as gravity is size * 5
            self.star = SpaceObject(np.amax(sizes), np.amax(masses), np.amax(sizes) * 5)

            # Delete max size & mass from lists
            index = np.argmax(sizes)
            sizes = np.delete(sizes, index)
            index = np.argmax(masses)
            masses = np.delete(masses, index)

            # Create velocities & distances for planet
            velocities = np.empty(num)
            distances = np.empty(num)
            for i in range(num):
                velocities[i] = generator.generate_float(0.1, 100) * 0.005
                distances[i] = generator.generate_float(0.1, 50)

            # The farthest planet has the largest velocity
            velocities = np.sort(velocities, kind='mergesort')
            velocities = np.flip(velocities)
            distances = np.sort(distances, kind='mergesort')

            # Save size of the previous planet (to correlate distances)
            prev_planet = 0
            prev_planet += self.star.size

            # Create 1st planet
            obj = SpaceObject(sizes[0], masses[0], sizes[0] * 5)
            planet = Planet(obj,
                            velocities[0], distances[0], prev_planet)
            planet_list = [planet]

            # Create planets from 2nd
            for i in range(1, num):
                prev_planet += sizes[i - 1] + distances[i - 1] * 10
                obj = SpaceObject(sizes[i], masses[i], sizes[i] * 1.5)
                planet = Planet(obj,
                                velocities[i], distances[i],
                                prev_planet)

                planet_list.append(planet)
            self.planets = planet_list

    def update(self) -> None:
        """
        Update planets on screen.
        """
        for planet in self.planets:
            planet.update()

    def create_images(self, solar_system=True) -> None:
        """
        Create images for every planet.

        :param solar_system: True to create solar system images.
        """
        if solar_system:
            self.star.load_image('app/assets/0.png')
            for i in range(len(self.planets)):
                self.planets[i].load_image('app/assets/{0}.png'.format(i + 1))
        else:
            self.star.generate_image()
            for planet in self.planets:
                planet.generate_image()

    def draw(self, screen: pygame.Surface) -> None:
        """
        Draw planetary system on display.
        :param screen: surface on which planetary system will be drawn.
        """
        screen.blit(self.star.surf, (screen.get_rect().center[0] - self.star.surf.get_width() / 2,
                                     screen.get_rect().center[1] - self.star.surf.get_height() / 2))
        for planet in self.planets:
            screen.blit(planet.surf, planet.pos)

"""
Class represent one type of space object - planet.
"""
import pygame
import numpy as np
import app.src.space_object.base as base


class Planet(base.SpaceObject):
    def __init__(self, space_object: base.SpaceObject, orbital_speed=1.0, distance=1.0, prev_planet=1.0):
        """
        Constructor for Planet class. Distance is in AU (astronomical units)

        :param space_object: parent object of the planet
        :param orbital_speed: velocity of the planet
        :param distance: distance to the system star
        :param prev_planet: distance to the previous planet
        """
        if orbital_speed <= 0:
            raise Exception('Velocity can\'t be negative number or zero!')
        if distance <= 0:
            raise Exception('Distance can\'t be negative number or zero!')
        if prev_planet <= 0:
            raise Exception('Distance to previous planet can\'t be negative number or zero!')

        super(Planet, self).__init__(space_object.size, space_object.mass,
                                     space_object.gravitation)

        self.prev_planet = prev_planet
        self.distance = distance * 10 + prev_planet + self.size

        self.orbital_speed = orbital_speed
        self.angle = np.radians(0)

        self.pos = (0, 0)

    def update(self) -> None:
        """
        Move planet around its axis and around the star of the system.
        Based on basic trigonometrical equation with unit circle.
        """
        self.angle += self.orbital_speed

        new_x = pygame.display.get_surface().get_rect().center[0] + self.distance * np.cos(self.angle)
        new_y = pygame.display.get_surface().get_rect().center[1] + self.distance * np.sin(self.angle)

        self.pos = (new_x - self.surf.get_width() / 2, new_y - self.surf.get_width() / 2)

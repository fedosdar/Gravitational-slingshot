""" Class represent spacecraft. """
import pygame
import numpy as np
from app.src.planetary_system import PlanetarySystem
from app.src.generator import generate_integer

class Spaceship:
    def __init__(self, planetary_system: PlanetarySystem, solar_system=True):
        """
        Constructor for initializing spaceship.
        :param planetary_system: planetary system in which spacecraft is located
        :param solar_system: True if system is solar
        """
        self.surf = None

        # Can be change
        self.mass = 10e-22

        if solar_system:
            self.starting_planet = planetary_system.planets[2]
        else:
            # Choosing starting planet with random
            index = generate_integer(0, len(planetary_system.planets) - 1)
            self.starting_planet = planetary_system.planets[index]

        self.pos = (self.starting_planet.pos[0] / 2,
                    self.starting_planet.pos[1] / 2)
        self.velocity_vector = pygame.Vector2(20, 0)

        self.started = False

    def create_image(self) -> None:
        """
        Load image of the spacecraft.
        """
        self.surf = pygame.image.load('app/assets/spaceship.png').convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (13, 20))

    def draw(self, screen: pygame.Surface) -> None:
        """
        Draw spacecraft on the Surface.
        :param screen: Surface for drawing
        """
        screen.blit(self.surf, self.pos)

    def launch(self) -> None:
        """
        Change flag to started. Means start of the motion.
        """
        self.started = True

    def set_velocity(self, x: float, y: float) -> None:
        """
        Set velocity vector for spacecraft.
        :param x: x-coordinate of the vector
        :param y: y-coordinate of the vector
        """
        x -= self.pos[0]
        y -= self.pos[1]
        self.velocity_vector = pygame.Vector2(x, y)

    def calculate_force(self, pos: (float, float), mass: float, gravity: float) -> None:
        """
        Calculate gravity forces on the ship.
        :param pos: position of the space object
        :param mass: mass of the space object
        :param gravity: gravity of the space object
        """
        # distance between the star & the spacecraft in x-axis & y-axis
        dx = self.pos[0] - pos[0]
        dy = self.pos[1] - pos[1]
        r = np.sqrt(np.power(dx, 2) + np.power(dy, 2))

        # angle between the star & the spacecraft.
        # Can be used arctan(dy / dx), arcos(dx / r2 ** 0.5), arcsin atd.
        angle = np.arctan2(dy, dx)

        # gravitational force in every axis using gravity equation for vectors
        fx = (-1) * gravity * mass * self.mass * dx / np.power(r, 3)
        fy = (-1) * gravity * mass * self.mass * dy / np.power(r, 3)

        # acceleration given by gravitational force. F = m * a -> a = F / m
        ax = fx / self.mass
        ay = fy / self.mass

        # new velocity vector with acceleration * t (to scale speed)
        self.velocity_vector[0] += ax * 0.001
        self.velocity_vector[1] += ay * 0.001

        self.pos = ((self.pos[0] + self.velocity_vector[0] * 0.001),
                    (self.pos[1] + self.velocity_vector[1] * 0.001))

    def update(self, planetary_system: PlanetarySystem) -> None:
        """
        Update position of the spacecraft in the planetary system.
        :param planetary_system: planetary system where is spacecraft located
        """
        if not self.started:
            self.pos = (self.starting_planet.pos[0] - self.surf.get_width() / 2,
                        self.starting_planet.pos[1] - self.surf.get_height() / 2)
        else:
            # star gravity
            self.calculate_force(pygame.display.get_surface().get_rect().center,
                                 planetary_system.star.mass,
                                 planetary_system.star.gravitation)
            # planets gravity
            for planet in planetary_system.planets:
                self.calculate_force(planet.pos,
                                     planet.mass,
                                     planet.gravitation)

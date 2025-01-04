""" Class represent every space object in the game such as planets, stars etc. """
import pygame
import app.src.generator as generator


class SpaceObject(pygame.sprite.Sprite):
    def __init__(self, size=0.1, mass=0.1, gravitation=0.1):
        """
        Constructor for initializing space object.

        :param size: size of the object in pixels
        :param mass: mass of the object, correlation with earth mass
        :param gravitation: gravity force of the planet
        """
        super(SpaceObject, self).__init__()

        if size <= 0:
            raise Exception('Size can\'t be negative number or zero!')
        if mass <= 0:
            raise Exception('Mass can\'t be negative number or zero!')
        if gravitation <= 0:
            raise Exception('Gravity can\'t be negative number or zero!')

        self.surf = pygame.Surface((size, size), pygame.SRCALPHA)
        self.surf.set_colorkey((0, 0, 0))
        self.surf.fill((0, 0, 0))

        self.size = size

        self.mass = mass
        self.gravitation = gravitation

    def load_image(self, image: str) -> None:
        """
        Load image for sprite from file. If there is no file in directory, create random image for space object.

        :param image: path to the image
        """
        try:
            self.surf = pygame.image.load(image).convert_alpha()
        except FileNotFoundError:
            self.generate_image()
        self.surf = pygame.transform.scale(self.surf,
                                           (self.size,
                                            self.size))
        # self.rect = self.surf.get_rect()

    def generate_image(self) -> None:
        """
        Generate image for sprite. Choose random image from assets for object.
        """
        index = generator.generate_integer(0, 8)
        self.load_image('app/assets/{0}.png'.format(index))

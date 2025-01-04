import sys
import pygame
from app.src.planetary_system import PlanetarySystem
from app.src.spaceship import Spaceship


def velocity_setter(screen: pygame.Surface, planet_sys: PlanetarySystem, spaceship: Spaceship) -> (float, float):
    """
    Display of the setting velocity vector.
    :param screen: displaying Surface
    :param planet_sys: planetary system of the game
    :param spaceship: spacecraft of the player
    :return (x,y) - coordinates of the velocity vector (direction from spacecraft)
    """
    clock = pygame.time.Clock()
    click = False

    running = True
    # main loop
    while running:
        screen.fill((0, 0, 0))

        # add button
        velocity_button = pygame.Rect(screen.get_width() - 200 - 50,
                                      screen.get_height() - 50 - 150,
                                      200, 50)

        velocity_surf = pygame.image.load('app/assets/velocity.png')

        mx, my = pygame.mouse.get_pos()

        pygame.draw.rect(screen, (50, 0, 0), velocity_button)

        screen.blit(velocity_surf, (screen.get_width() - 250 - 50, screen.get_height() - 50 - 150))

        # setting velocity
        if click:
            if velocity_button.collidepoint((mx, my)):
                return 0, 0
            return mx, my

        # event handler
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        # image update
        planet_sys.draw(screen)
        spaceship.draw(screen)
        pygame.display.update()
        clock.tick(60)

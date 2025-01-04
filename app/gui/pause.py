import sys
import pygame
from app.src.planetary_system import PlanetarySystem
from app.src.spaceship import Spaceship


def pause(screen: pygame.Surface, planet_sys: PlanetarySystem, spaceship: Spaceship):
    """
    Pause the game.
    :param screen: Surface for drawing
    :param planet_sys: planetary system of the game
    :param spaceship: spaceship of the player
    """
    clock = pygame.time.Clock()
    click = False

    running = True
    # main loop
    while running:
        screen.fill((0, 0, 0))

        # create button to unpause
        pause_button = pygame.Rect(screen.get_width() - 200 - 50,
                                   screen.get_height() - 50 - 50,
                                   200, 50)

        pause_surf = pygame.image.load('app/assets/pause.png')

        mx, my = pygame.mouse.get_pos()

        pygame.draw.rect(screen, (50, 0, 0), pause_button)

        screen.blit(pause_surf, (screen.get_width() - 250 - 50, screen.get_height() - 50 - 50))

        # unpause game
        if pause_button.collidepoint((mx, my)) and click:
            running = False

        # event handler
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        # updating display
        planet_sys.draw(screen)
        spaceship.draw(screen)
        pygame.display.update()
        clock.tick(60)

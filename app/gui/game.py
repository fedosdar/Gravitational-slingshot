import pygame
from app.src.planetary_system import PlanetarySystem
from app.src.spaceship import Spaceship
import app.gui.pause as pause
from app.gui.velocity_setter import velocity_setter


def game(screen: pygame.Surface, solar_system=True):
    """
    Create game display.
    :param screen: Surface for drawing
    :param solar_system: True of game will be in solar system
    """
    clock = pygame.time.Clock()
    launched = False

    # generate system
    if solar_system:
        planet_sys = PlanetarySystem(solar_system=True)
        planet_sys.create_images()
        spaceship = Spaceship(planet_sys, solar_system=True)
    else:
        planet_sys = PlanetarySystem(solar_system=False)
        planet_sys.create_images(solar_system=False)
        spaceship = Spaceship(planet_sys, solar_system=False)

    spaceship.create_image()

    click = False

    # main loop
    running = True
    while running:
        screen.fill((0, 0, 0))

        # add buttons
        exit_button = pygame.Rect(screen.get_width() - 250 - 50,
                                  50,
                                  250, 50)
        pause_button = pygame.Rect(screen.get_width() - 250 - 50,
                                   screen.get_height() - 50 - 50,
                                   250, 50)
        velocity_button = pygame.Rect(screen.get_width() - 250 - 50,
                                      screen.get_height() - 50 - 150,
                                      250, 50)

        exit_surf = pygame.image.load('app/assets/exit.png')
        pause_surf = pygame.image.load('app/assets/pause.png')
        velocity_surf = pygame.image.load('app/assets/velocity.png')

        mx, my = pygame.mouse.get_pos()

        pygame.draw.rect(screen, (0, 0, 0), exit_button)
        pygame.draw.rect(screen, (0, 0, 0), pause_button)
        pygame.draw.rect(screen, (0, 0, 0), velocity_button)

        screen.blit(exit_surf, (screen.get_width() - 250 - 50, 50))
        screen.blit(pause_surf, (screen.get_width() - 250 - 50, screen.get_height() - 50 - 50))
        screen.blit(velocity_surf, (screen.get_width() - 250 - 50, screen.get_height() - 50 - 150))

        # exit to main menu
        if exit_button.collidepoint((mx, my)) and click:
            running = False
        # pause
        if pause_button.collidepoint((mx, my)) and click:
            pause.pause(screen, planet_sys, spaceship)
        # set velocity vector for the spacecraft
        if velocity_button.collidepoint((mx, my)) and click and not launched:
            launched = True
            velocity = velocity_setter(screen, planet_sys, spaceship)
            spaceship.set_velocity(velocity[0], velocity[1])
            spaceship.launch()

        # event handler
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        # updating positions
        planet_sys.update()
        spaceship.update(planet_sys)
        planet_sys.draw(screen)
        spaceship.draw(screen)

        pygame.display.update()
        clock.tick(60)

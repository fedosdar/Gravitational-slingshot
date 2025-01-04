import sys
import pygame
import app.gui.game as game


def main_menu():
    """
    Display main menu of the game.
    """
    clock = pygame.time.Clock()

    # set sreen
    flags = pygame.RESIZABLE
    screen = pygame.display.set_mode((0, 0), flags)

    click = False
    running = True
    # main loop
    while running:
        # fill with background color
        screen.fill((0, 0, 0))

        # rectangles for buttons
        gravity_slingshot = pygame.Rect((screen.get_width() - 500) / 2,
                                        100,
                                        500, 50)
        solar_sys_start = pygame.Rect((screen.get_width() - 250) / 2,
                                      200,
                                      250, 50)
        random_sys_start = pygame.Rect((screen.get_width() - 250) / 2,
                                       300,
                                       250, 50)
        exit_button = pygame.Rect((screen.get_width() - 250) / 2,
                                  400,
                                  250, 50)

        # add images for buttons
        text_surf = pygame.image.load('app/assets/texxt_box.png')
        sol_sys = pygame.image.load('app/assets/solar_system.png')
        rand_sys = pygame.image.load('app/assets/random_system.png')
        exit_surf = pygame.image.load('app/assets/exit.png')

        mx, my = pygame.mouse.get_pos()

        # drawing rectangles
        pygame.draw.rect(screen, (0, 0, 0), gravity_slingshot)
        pygame.draw.rect(screen, (0, 0, 0), solar_sys_start)
        pygame.draw.rect(screen, (0, 0, 0), random_sys_start)
        pygame.draw.rect(screen, (0, 0, 0), exit_button)

        screen.blit(text_surf, ((screen.get_width() - 500) / 2, 100))
        screen.blit(sol_sys, ((screen.get_width() - 250) / 2, 200))
        screen.blit(rand_sys, ((screen.get_width() - 250) / 2, 300))
        screen.blit(exit_surf, ((screen.get_width() - 250) / 2, 400))

        # create new game in the solar system
        if solar_sys_start.collidepoint((mx, my)) and click:
            game.game(screen, solar_system=True)
        # create new game in the random system
        if random_sys_start.collidepoint((mx, my)) and click:
            game.game(screen, solar_system=False)
        # exit from the game
        if exit_button.collidepoint((mx, my)) and click:
            pygame.quit()
            sys.exit()

        # event handler
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(60)


main_menu()

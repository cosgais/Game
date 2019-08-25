import pygame
from pygame.locals import *
import constants as c

import global_vars as g

import menu

class Game:
    def __init__(self):
        # initialize the pygame module
        pygame.init()

        # create a surface on screen that has the size of 800 x 600
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        pygame.display.flip()

        c.SCREENRECT.width, c.SCREENRECT.height = pygame.display.get_surface().get_size()
        self.menu = menu.Menu()
        # define a variable to control the main loop
        self.running = True


    def update(self, dt):
        # update keyboard state and mouse position
        g.KEYSTATE = pygame.key.get_pressed()
        g.MOUSEPOS = pygame.mouse.get_pos()
        self.menu.update(dt)

    def draw(self):
        # Do all of the drawing
        self.menu.draw(self.screen)
        # Tell pygame to show all the beautiful things we drew
        pygame.display.flip()

    def main(self):
        # game clock
        clock = pygame.time.Clock()
        # main loop
        while self.running:
            # event handling, gets all event from the eventqueue
            for event in pygame.event.get():
                # only do something if the event is of type QUIT
                if event.type == pygame.QUIT:
                    # change the value to False, to exit the main loop
                    self.running = False

            self.update(clock.tick(c.FPS))
            if g.KEYSTATE[pygame.K_ESCAPE]:
                self.running = False
            self.draw()


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    game = Game()
    # call the main function
    game.main()

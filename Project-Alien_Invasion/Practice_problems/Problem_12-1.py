# Problem 12-1
import pygame
import sys
import os
from pathlib import Path

file_path = Path("C:/Users/jshih/mu_code/Code/Python_Crash_Course/Project-Alien_Invasion/Project-Alien_Invasion/Practice_problems")
os.chdir(file_path)



class screen_test:
    """Generate a screen for practice problem 12-1"""

    def __init__(self):
        """Initialize the screen test"""
        pygame.init()
        self.screen = pygame.display.set_mode((200, 200))
        pygame.display.set_caption("TEST")
        self.bg_color = (0,0,230)
        self.stickman = Stick(self)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.flip()

            self.screen.fill(self.bg_color)

            self.stickman.blitme()



class Stick:
    """Class to manage stickman"""
    def __init__(self, t):
        self.screen = t.screen
        self.screen_rect= t.screen.get_rect()

        #load stickman
        self.image = pygame.image.load("bmp_images/stickman.bmp")
        self.rect = self.image.get_rect()

        #stickman goes to midleft
        self.rect.midleft = self.screen_rect.midleft
        
    def blitme(self):
        """Draw the stickman at current location."""
        self.screen.blit(self.image, self.rect)
if __name__ == '__main__':
    t = screen_test()
    t.run_game()


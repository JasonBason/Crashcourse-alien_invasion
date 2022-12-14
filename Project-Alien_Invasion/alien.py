import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """ A Class to represent a single alien fleet."""
    
    def __init__(self, ai_game):
        """ Initializes the alien and sets its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        
        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images_bmp/alien_small.bmp')
        self.rect = self.image.get_rect()
        
        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)
    
    def update(self):
        """Move the alien to the right."""
        self.x += (self.settings.alien_speed *
                   self.settings.fleet_direction)
        self.rect.x = self.x
    
    def check_edges(self):
        """Return right_edge if alien is at the edge of the screen"""
        screen_rect = self.screen.get_rect()
        if (self.rect.right >= screen_rect.right) or self.rect.left <= 0:
            return True
        

       

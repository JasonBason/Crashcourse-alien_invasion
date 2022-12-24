import pygame.font
from pygame.sprite import Group
from ship import Ship


class Scoreboard:
    """A class for scoreboard"""
    def __init__(self, ai_game):
        """Create instance of scorboard for the game"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        self.ai_game = ai_game
        
        # Define text qualities
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None, 48)
        
        #Prep score images
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()
        
    def prep_score(self):
        # Turn the score into a rendered image
        #score_str = str(self.stats.score)
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        
        self.score_img = self.font.render(score_str,
                                        True,
                                        self.text_color,
                                        self.settings.bg_color)
        
        # Display score to right
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right -20
        self.score_rect.top = 20
        #print('print test')
    
    def prep_high_score(self):
        # Turn the high score into a rendered image
        rounded_high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(rounded_high_score)
        self.high_score_img = self.font.render(high_score_str,
                                               True,
                                               self.text_color,
                                               self.settings.bg_color)
        
        # Display above and middle
        self.high_score_img_rect = self.high_score_img.get_rect()
        self.high_score_img_rect.centerx = self.screen_rect.centerx
        self.high_score_img_rect.top = self.screen_rect.top

    def prep_level(self):
        # show the player the current level
        level_str = str(self.stats.level)
        self.level_img = self.font.render(level_str,
                                          True,
                                          self.text_color,
                                          self.settings.bg_color)
        
        # place level on the right
        self.level_img_rect = self.level_img.get_rect()
        self.level_img_rect.right = self.screen_rect.right - 20
        self.level_img_rect.top = self.score_rect.bottom +10

    def prep_ships(self):
        """ Show how many ships remain"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
        
        
        print('test')
        
    def show_score(self):
        # Display the scores and level and ships left
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_img, self.high_score_img_rect)
        self.screen.blit(self.level_img, self.level_img_rect)
        self.ships.draw(self.screen)
        
    def check_high_score(self):
        # Check to see if the highscore should be updated
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
 
        
        

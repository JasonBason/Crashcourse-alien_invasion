import pygame.font

class Scoreboard:
    """A class for scoreboard"""
    def __init__(self, ai_game):
        """Create instance of scorboard for the game"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        
        # Define text qualities
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None, 48)
        
        #Prep score method
        self.prep_score()
        #self.score_rect.center = self.screen_rect.center

        
    def prep_score(self):
        # Turn the score into a rendered image
        score_str = str(self.stats.score)
        self.score_img = self.font.render(score_str,
                                        True,
                                        self.text_color,
                                        self.settings.bg_color)
        
        # Display score to right
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right -20
        self.score_rect.top = 20
        print('print test')

        
    def show_score(self):
        # Display the score
        self.screen.blit(self.score_img, self.score_rect)
 
        
        

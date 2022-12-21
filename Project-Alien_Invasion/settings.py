class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings"""
        #Screen settings
        self.screen_width = 600#1280
        self.screen_height = 600#720
        self.bg_color = (230,230,230)
        
        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 1
        
        # Bullet settings
        self.bullet_speed = .50
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (160,30,30)
        self.bullets_allowed = 3
        
        # Alien settings
        self.alien_speed = 0.1
        self.fleet_drop_speed = 50
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        
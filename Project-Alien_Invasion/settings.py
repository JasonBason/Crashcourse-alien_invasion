class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's static settings"""
        #Screen settings
        self.screen_width = 600#1280
        self.screen_height = 600#720
        self.bg_color = (230,230,230)
        
        # Ship settings
        self.ship_limit = 1
        
        # Bullet settings
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (160,30,30)
        self.bullets_allowed = 3
        # Alien settings

        self.fleet_drop_speed = 50

        # how quickly the game speeds up
        self.speedup_scale = 1.1
        
        # Initialize the dynamic settings
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = .50
        self.alien_speed = 0.1
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        
        # scoring
        self.alien_points = 50
        
    def increase_speed(self):
        """Increase the speed of ships, bullets, etc"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
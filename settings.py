import pygame
class Settings:
    """A class to store all setting for alien invasion"""

    def __init__(self):
        """Initialize the games static settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.bg_image = pygame.image.load("Images/LZP_bild.bmp")

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullets_allowed = 3

        # Alien settings
        self.fleet_drop_speed = 10

        # Full screen?
        self.fullscreen_flag = False

        # How quickly the game speeds up
        self.speedup_scale = 1.1

        # How quickly the alien points increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game"""
        self.ship_speed = 1.5
        self.bullet_speed = 2.0
        self.alien_speed = 1.0

        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        # here we do an explicit type conversion to only have integer scores

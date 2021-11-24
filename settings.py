import pygame 
class Settings:
    """A class to store all setting for alien invasion"""

    def __init__(self):
        """Initialize the games settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.bg_image = pygame.image.load("Images/LZP_bild.bmp")
        # Ship settings
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullets_allowed = 3

        # Full screen?
        self.fullscreen_flag = False

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """"A class to manage the bullets fired"""

    def __init__(self, ai_game):
        """create a bullet at the ships position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = pygame.image.load("Images/TucanBullets.bmp")

        # Get the rectangle from the image and position it correctly
        self.rect = self.image.get_rect()
        self.rect.midbottom = ai_game.ship.rect.midtop

        # Store the bullet's position as a decimal value
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen"""
        # Update the decimal position of the bullet.
        self.y -= self.settings.bullet_speed
        #Update the rectangle position
        self.rect.y = int(self.y)

    def draw_bullet(self):
        """Draw the bullet to the screen"""
        self.screen.blit(self.image, self.rect)

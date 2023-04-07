import pygame
#from sonic_runner.components.power_ups.lives import 
from sonic_runner.utils.constants import SCREEN_WIDTH, SONIC_DEAD
class Obstacle:
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.lives = 3

    def update(self, game_speed, player):
        self.rect.x -= game_speed
        if self.rect.colliderect(player.sonic_rect):
            if(not player.supersonic):
                self.image = SONIC_DEAD
                pygame.time.delay(500)
                player.sonic_dead = True

    def draw(self, screen):
        screen.blit(self.image, self.rect)
    

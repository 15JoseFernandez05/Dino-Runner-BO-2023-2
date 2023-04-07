import random
import pygame
from sonic_runner.components import text_utils
from sonic_runner.components.power_ups.power_up import PowerUp
from sonic_runner.utils.constants import RINGS, RING_TYPE, SCREEN_WIDTH
class Rings(PowerUp):
    def __init__(self):
        self.image = RINGS[0]
        self.type = RING_TYPE
        self.ring = 0
        self.rings = 0
        super().__init__(self.image, self.type)
        select_position = random.randint(0,2)
        if select_position == 0:
            self.rect.y = 250
        elif select_position == 1:
            self.rect.y = 275
        else:
            self.rect.y = 300
        self.step_index = 0
        self.levitate_ring =True

    def update(self, game_speed, player):
        if self.levitate_ring:
            self.levitate()
        if self.step_index >= 20:
            self.step_index = 0
        if player.sonic_rect.colliderect(self.rect):
            self.ring += 1
        return super().update(game_speed, player)
    
    def levitate(self):
        if self.step_index < 5:
            self.image = RINGS[0]
        elif self.step_index > 5 and self.step_index < 10:
            self.image = RINGS[1]
        elif self.step_index > 10 and self.step_index < 15:
            self.image = RINGS[2]
        else:
            self.image = RINGS[3]
        self.step_index += 1
    

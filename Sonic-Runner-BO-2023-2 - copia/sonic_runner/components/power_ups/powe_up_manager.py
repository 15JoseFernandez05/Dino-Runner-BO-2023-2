import random
from sonic_runner.components.power_ups.rings import Rings
from sonic_runner.components.power_ups.lives import Live
from sonic_runner.components.power_ups.supersonic import SuperSonic
class PowerUpManager:
    
    def __init__(self):
        self.power_ups = []

    def update(self, game_speed, points, player):
        self.select_power_up = random.randint(0,2)
        if len(self.power_ups) == 0 and points % 200 == 0:
            if self.select_power_up == 0:
                self.power_ups.append(Rings()) 
            elif self.select_power_up == 1:
                self.power_ups.append(SuperSonic()) 
            else: 
                self.power_ups.append(Live())
        for power_up in self.power_ups:
            if power_up.used or power_up.rect.x < -power_up.rect.width:
                self.power_ups.pop()
            if power_up.used:
                player.set_power_up(power_up)
            power_up.update(game_speed, player)

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)
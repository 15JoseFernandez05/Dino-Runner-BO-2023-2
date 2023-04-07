import random
from sonic_runner.components.obstacles.obstacle import Obstacle
from sonic_runner.utils.constants import BEE

class Bee(Obstacle):
    def __init__(self):
        image = BEE[0]
        super().__init__(image)
        select_position = random.randint(0,2)
        if select_position == 0:
            self.rect.y = 250
        elif select_position == 1:
            self.rect.y = 275
        else:
            self.rect.y = 300
        self.step_index = 0
        self.flying =True
    
    def update(self, game_speed, player):
        if self.flying:
            self.fly()
        if self.step_index >= 10:
            self.step_index = 0
        return super().update(game_speed, player)
    
    def fly(self):
        if self.step_index < 2:
            self.image = BEE[0]
        elif self.step_index > 2 and self.step_index < 4:
            self.image = BEE[1]
        elif self.step_index > 4 and self.step_index < 6:
            self.image = BEE[2]
        else:
            self.image = BEE[3]
        self.step_index += 1

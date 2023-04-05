import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD

class Bird(Obstacle):
    def __init__(self):
        image = BIRD[0]
        super().__init__(image)
        select_position = random.randint(0,2)
        if select_position == 0:
            self.rect.y = 250
        elif select_position == 1:
            self.rect.y = 200
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
        self.image = BIRD[0] if self.step_index < 5 else BIRD[1]
        self.step_index += 1

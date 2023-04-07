import random
from sonic_runner.components.obstacles.obstacle import Obstacle
from sonic_runner.utils.constants import LARGE_ENEMY, SMALL_ENEMY

class Enemy(Obstacle):
    Y_POS_SMALL_ENEMY = 325
    Y_POS_LARGE_ENEMY = 300
    def __init__(self):
        sw = random.randint(0, 1)
        if sw == 0:
            self.type = random.randint(0, 2)
            image = SMALL_ENEMY[self.type]
            super().__init__(image)
            self.rect.y = self.Y_POS_SMALL_ENEMY
        else:
            self.type = random.randint(0, 2)
            if self.type == 2:
                self.Y_POS_LARGE_ENEMY = 325
            image = LARGE_ENEMY[self.type]
            super().__init__(image)
            self.rect.y = self.Y_POS_LARGE_ENEMY
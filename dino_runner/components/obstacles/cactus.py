import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS

class Cactus(Obstacle):
    Y_POS_CACTUS = 325
    Y_POS_LARGE_CACTUS = 300
    def __init__(self):
        sw = random.randint(0, 1)
        if sw == 0:
            self.type = random.randint(0, 2)
            image = SMALL_CACTUS[self.type]
            super().__init__(image)
            self.rect.y = self.Y_POS_CACTUS
        else:
            self.type = random.randint(0, 2)
            image = LARGE_CACTUS[self.type]
            super().__init__(image)
            self.rect.y = self.Y_POS_LARGE_CACTUS
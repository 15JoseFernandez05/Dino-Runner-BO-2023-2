import random
from sonic_runner.components.obstacles.enemies import Enemy
from sonic_runner.components.obstacles.bee import Bee

class ObstacleManager:
    def __init__(self):
        self.obstacles = []
    
    def update(self, game_speed, player):
        select_obstacle = random.randint(0,1)
        if len(self.obstacles) == 0:
            self.obstacles.append(Enemy()) if select_obstacle == 0 else self.obstacles.append(Bee())
        for obstacle in self.obstacles:
            if obstacle.rect.x < -obstacle.rect.width:
                self.obstacles.pop()
            if player.sonic_rect.colliderect(obstacle.rect):
                if player.supersonic:
                    self.obstacles.remove(obstacle)
            obstacle.update(game_speed, player)

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
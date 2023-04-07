import pygame
import os
from sonic_runner.components import text_utils
from sonic_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, BG2, MENU, SOUNDS
from sonic_runner.components.sonic import Sonic
from sonic_runner.components.obstacles.obstacle_manager import ObstacleManager
from sonic_runner.components.power_ups.powe_up_manager import PowerUpManager
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = False
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.x_pos_bg2 = 0
        self.y_pos_bg2 = 10
        self.player = Sonic()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.points = 0
        self.dead_count = 0
        self.max = 0
        self.rings = 0
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.play(-1)
    def run(self):
        # Game loop: events - update - draw
        self.running = True
        while self.running:
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
            if event.type == pygame.KEYDOWN and not self.playing:
                self.playing = True
                self.reset()

    def update(self):
        if self.playing:
            user_input = pygame.key.get_pressed()
            self.player.update(user_input)
            self.obstacle_manager.update(self.game_speed, self.player)
            self.power_up_manager.update(self.game_speed, self.points, self.player)
            self.points += 1
            if self.points % 200 == 0:
                self.game_speed += 1
            if self.player.sonic_dead:
                self.playing = False
                self.dead_count += 1

    def draw(self):
        if self.playing:
            self.clock.tick(FPS)
            self.draw_background()
            self.player.draw(self.screen)
            self.obstacle_manager.draw(self.screen)
            self.power_up_manager.draw(self.screen)
            self.draw_score()
        else:
            self.draw_menu()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg < -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
        image_width = BG2.get_width()
        self.screen.blit(BG2, (self.x_pos_bg2, self.y_pos_bg2))
        self.screen.blit(BG2, (image_width + self.x_pos_bg2, self.y_pos_bg2))
        if self.x_pos_bg2 < -image_width:
            self.screen.blit(BG2, (image_width + self.x_pos_bg2, self.y_pos_bg2))
            self.x_pos_bg2 = 0
        self.x_pos_bg2 -= self.game_speed
    
    def draw_score(self):
        score, score_rect = text_utils.get_message('Points: '+str(self.points),20, 1000, 40)
        self.screen.blit(score, score_rect)
        ring, ring_rect = text_utils.get_message('Rings: '+str(self.rings),20, 1000, 70)
        self.screen.blit(ring, ring_rect)
        if self.player.supersonic:
            time_to_show = round((self.player.time_up_power_up - pygame.time.get_ticks())//1000,2)
            if time_to_show >=0:
                power, power_rect = text_utils.get_message('Invencible Time: '+str(time_to_show),20, 1000, 100)
                self.screen.blit(power, power_rect)

    def draw_menu(self):
        blue_color = (0, 0, 255)
        self.screen.fill(blue_color)
        self.print_menu_element()

    def print_menu_element(self):
        if self.dead_count == 0:
            text, text_rect = text_utils.get_message('Press any key to start', 30)
            self.screen.blit(text, text_rect)
        else:
            if self.points > self.max:
                self.max = self.points
            text, text_rect = text_utils.get_message('Press any key to restart', 30)
            score, score_rect = text_utils.get_message('Your score: ' +str(self.points), 30, height=SCREEN_HEIGHT//2 -50)
            dead, dead_rect = text_utils.get_message('Try: ' +str(self.dead_count), 30, height=SCREEN_HEIGHT//2)
            max, max_rect = text_utils.get_message('Best Score: ' +str(self.max), 30, height=SCREEN_HEIGHT//2 + 50)
            self.screen.blit(text, text_rect)
            self.screen.blit(score, score_rect)
            self.screen.blit(dead, dead_rect)
            self.screen.blit(max, max_rect)
    
    def reset(self):
        self.game_speed = 20
        self.cloud_speed = 10
        self.player =  Sonic()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.points = 0
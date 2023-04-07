import pygame
from sonic_runner.utils.constants import (SONIC_RUNNING, SONIC_JUMPING, SONIC_DUCKING, LIVE_TYPE, 
                                          RING_TYPE, SOUNDS, SUPER_SONIC, DEFAULT_TYPE, SUPER_SONIC_TYPE)


class Sonic:
    X_POS = 80
    Y_POS = 315
    Y_POS_DUCK = 340
    JUMP_VEL = 8.5

    def __init__(self):
        self.image = SONIC_RUNNING[0]
        self.type = DEFAULT_TYPE
        #self.sounds = SOUNDS[0]
        self.sonic_rect = self.image.get_rect()
        self.sonic_rect.x = self.X_POS
        self.sonic_rect.y = self.Y_POS
        self.step_index = 0
        self.sonic_run = True
        self.sonic_duck = False
        self.sonic_jump = False
        self.jump_vel = self.JUMP_VEL
        self.sonic_dead = False
        self.lives = 3
        self.supersonic = False
        self.time_up_power_up = 0

    def update(self, user_input):
        if self.sonic_jump:
            self.jump()
        if self.sonic_duck:
            self.duck()
        if self.sonic_run:
            self.run()

        if user_input[pygame.K_DOWN] and not self.sonic_jump:
            self.sonic_run = False
            self.sonic_duck = True
            self.sonic_jump = False
        elif user_input[pygame.K_UP] and not self.sonic_jump:
            self.sonic_run = False
            self.sonic_duck = False
            self.sonic_jump = True
        elif not self.sonic_jump:
            self.sonic_run = True
            self.sonic_duck = False
            self.sonic_jump = False

        if self.step_index >= 20:
            self.step_index = 0
        if self.supersonic:
            time_to_show = round((self.time_up_power_up - pygame.time.get_ticks())/1000, 2)
            if time_to_show < 0:
                self.reset()

    def draw(self, screen):
        screen.blit(self.image, self.sonic_rect)

    def run(self):
        if self.step_index < 5:
            self.image = SONIC_RUNNING[0]
        elif self.step_index > 5 and self.step_index < 10:
            self.image = SONIC_RUNNING[1]
        elif self.step_index > 10 and self.step_index < 15:
            self.image = SONIC_RUNNING[2]
        else :
            self.image = SONIC_RUNNING[3]
        self.sonic_rect = self.image.get_rect()
        self.sonic_rect.x = self.X_POS
        self.sonic_rect.y = self.Y_POS
        self.step_index += 1

    def duck(self):
        if self.step_index < 5:
            self.image = SONIC_DUCKING[0]
        elif self.step_index > 5 and self.step_index < 10:
            self.image = SONIC_DUCKING[1]
        elif self.step_index > 10 and self.step_index < 15:
           self.image = SONIC_DUCKING[2]
        elif self.step_index > 15 and self.step_index < 20:
            self.image = SONIC_DUCKING[3]
        else :
            self.image = SONIC_DUCKING[4]
        self.sonic_rect = self.image.get_rect()
        self.sonic_rect.x = self.X_POS
        self.sonic_rect.y = self.Y_POS_DUCK
        self.step_index += 1

    def jump(self):
        self.image = SONIC_JUMPING
        if self.sonic_jump:
            self.sonic_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < -self.JUMP_VEL:
            self.sonic_rect.y = self.Y_POS
            self.sonic_jump = False
            self.jump_vel = self.JUMP_VEL
    
    def set_power_up(self, power_up):
        if power_up.type == RING_TYPE:
            self.type = RING_TYPE
        if power_up.type == LIVE_TYPE:
            self.type = LIVE_TYPE
        if power_up.type == SUPER_SONIC_TYPE:
            self.type = SUPER_SONIC_TYPE
            self.supersonic = True
            self.time_up_power_up = power_up.time_up
    
    def reset(self):
        self.type = DEFAULT_TYPE
        self.supersonic = False
        self.time_up_power_up = 0

